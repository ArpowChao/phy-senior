# -*- coding: utf-8 -*-
"""
防回歸檢查腳本 —— 每次（尤其是 GPT/Gemini）大改後跑一次：python check.py
檢查項目：
  1. 超綱禁用詞（課綱紅線，必修=Ⅴc；詳見記憶與 108課綱全/00-*.pdf）
  2. JS 字串內單反斜線 LaTeX（\frac 會被吃成 form-feed，必須寫 \\frac）
  3. 殘留控制字元（form-feed / vertical-tab）
  4. JS 語法（node --check）
  5. examPractice ↔ examSolutions 鍵一一對應
  6. 歷屆題裁切圖檔案存在
  7. SVG 標籤開閉平衡
exit code 0 = 全過；1 = 有 FAIL。
"""
import io
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
ROOT = Path(__file__).parent
FILES = [ROOT / "gsat_physics_review.html",
         *sorted((ROOT / "data").glob("*.js"))]

failures = []
warnings = []


def fail(msg):
    failures.append(msg)
    print(f"  ✗ FAIL: {msg}")


def warn(msg):
    warnings.append(msg)
    print(f"  ⚠ WARN: {msg}")


def ok(msg):
    print(f"  ✓ {msg}")


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


texts = {f: f.read_text(encoding="utf-8") for f in FILES}

# ---------------------------------------------------------------- 1. 禁用詞
print("[1] 超綱禁用詞掃描")
BS = chr(92)
# (pattern, 說明)。動量單獨列為 WARN（物質波 λ=h/p 脈絡屬必修，需人工判斷）。
BANNED = [
    (r"磁通量", "磁通量（選修 PKc-Ⅴa，改用「磁力線/磁場變化」）"),
    (r"ΔΦ|\\Delta\s*\\Phi", "法拉第定律 ΔΦ（選修）"),
    (r"Φ\s*[=＝]\s*BA", "Φ＝BA（選修）"),
    (r"衝量", "衝量（選修 PEb-Ⅴa）"),
    (r"mv\s*[²2]\s*/\s*r|\\frac\{mv\^2\}\{r\}", "向心力公式 mv²/r（必修不涉及公式計算）"),
    (r"Δy\s*[=＝]\s*Lλ/d|\\frac\{L\\lambda\}\{d\}", "雙狹縫條紋間距公式（選修）"),
    (r"法拉第定律", "法拉第定律（選修，冷次定律才是必修）"),
    (r"摩擦係數|μN|\\mu\s*N", "摩擦係數（學測不涉及）"),
    (r"熱力學第一定律", "熱力學第一定律（已議定刪除，用能量觀點）"),
    (r"質能等價", "應寫「質能互換」"),
    (r"胡克定律", "應寫「虎克定律」"),
]
# 否定/排雷句屬刻意說明（「學測不涉及摩擦係數」「不需要摩擦係數」），不算違規
NEGATION = re.compile(r"不涉及|不需要|不需|不用|不使用|沒有|非必修|選修")
hit = False
for f, text in texts.items():
    for pat, desc in BANNED:
        for m in re.finditer(pat, text):
            ctx = text[max(0, m.start() - 45):m.end() + 45].replace("\n", " ")
            if NEGATION.search(ctx):
                continue
            hit = True
            fail(f"{f.name}:{line_of(text, m.start())} {desc} → 「{m.group(0)}」")
    # 動量：角動量(克卜勒註記已議定保留)與物質波/誘答脈絡屬合法，其餘列 WARN 人工判斷
    for m in re.finditer(r"(?<![能角])動量", text):
        ctx = text[max(0, m.start() - 45):m.end() + 45].replace("\n", " ")
        if re.search(r"物質波|德布羅意|波長|λ|\\lambda|h/p|h/mv|誘答|" + NEGATION.pattern, ctx):
            continue
        warn(f"{f.name}:{line_of(text, m.start())} 出現「動量」請人工確認脈絡：…{ctx}…")
if not hit:
    ok("無禁用詞")

# ------------------------------------------- 2. 單反斜線 LaTeX（JS 字串殺手）
print("[2] 單反斜線 LaTeX 偵測")
LATEX_CMDS = (r"frac|circ|theta|eta|lambda|nu|pi|alpha|beta|gamma|Delta|delta|"
              r"times|cdot|propto|sqrt|sin|cos|tan|text|mathrm|vec|approx|neq|"
              r"leq|geq|infty|sum|int|rightarrow|Rightarrow|quad|degree|Phi|phi")
single_bs = re.compile("(?<!" + BS * 2 + ")" + BS * 2 + "(?:" + LATEX_CMDS + r")\b")
hit = False
for f, text in texts.items():
    for m in re.finditer(single_bs, text):
        # HTML 檔中，非 <script> 區（如 CSS/註解）不會進 JS 字串——但本專案 LaTeX 只該出現在 JS 字串，全檔檢查。
        hit = True
        fail(f"{f.name}:{line_of(text, m.start())} 單反斜線 LaTeX 「{m.group(0)}」（JS 字串須寫成 {BS}{BS}…）")
if not hit:
    ok("無單反斜線 LaTeX")

# ---------------------------------------------------------- 3. 控制字元
print("[3] 控制字元（form-feed / vertical-tab）")
hit = False
for f, text in texts.items():
    for ch, name in ((chr(12), "form-feed"), (chr(11), "vertical-tab")):
        idx = text.find(ch)
        if idx >= 0:
            hit = True
            fail(f"{f.name}:{line_of(text, idx)} 含 {name}（通常是單反斜線 LaTeX 被跳脫的產物）")
if not hit:
    ok("無控制字元")

# ---------------------------------------------------------- 4. JS 語法
print("[4] node --check 語法")
tmpdir = Path(tempfile.mkdtemp())
targets = []
html_text = texts[ROOT / "gsat_physics_review.html"]
inline = "\n;\n".join(re.findall(r"<script>(.*?)</script>", html_text, re.S))
p = tmpdir / "inline.js"
p.write_text(inline, encoding="utf-8")
targets.append(("gsat_physics_review.html <script>", p))
targets += [(f.name, f) for f in FILES if f.suffix == ".js"]
for label, path in targets:
    r = subprocess.run(["node", "--check", str(path)],
                       capture_output=True, text=True, shell=True)
    if r.returncode != 0:
        fail(f"{label} 語法錯誤：{(r.stderr or r.stdout).strip().splitlines()[-1][:200]}")
    else:
        ok(f"{label} 語法 OK")

# --------------------------------- 5. examPractice ↔ examSolutions 鍵對應
print("[5] examPractice ↔ examSolutions 鍵對應")
ep = texts[ROOT / "data" / "examPractice.js"]
es = texts[ROOT / "data" / "examSolutions.js"]
practice_keys = set()
for m in re.finditer(r"year:\s*'([^']+)'\s*,\s*q:\s*'([^']+)'", ep):
    practice_keys.add(f"{m.group(1)}_{m.group(2)}")
sol_keys = set(re.findall(r"'([^']+)':\s*\{\s*ans:", es))
if not practice_keys or not sol_keys:
    fail(f"鍵抽取失敗（practice={len(practice_keys)}, solutions={len(sol_keys)}），檢查資料格式是否被改")
else:
    missing = practice_keys - sol_keys
    orphan = sol_keys - practice_keys
    if missing:
        fail(f"{len(missing)} 題缺詳解：{sorted(missing)[:8]}{'…' if len(missing) > 8 else ''}")
    if orphan:
        warn(f"{len(orphan)} 筆詳解無對應題目：{sorted(orphan)[:8]}")
    if not missing:
        ok(f"{len(practice_keys)} 題皆有詳解")

# ---------------------------------------------------------- 6. 裁切圖存在
print("[6] 歷屆題裁切圖檔案")
crops_dir = ROOT / "assets" / "exam_crops"
crop_prefix = dict(re.findall(r"'([^']+)':\s*\{[^}]*?crop:\s*'([^']+)'", html_text))
missing_imgs = []
for key in practice_keys:
    pk, q = key.split("_", 1)
    prefix = crop_prefix.get(pk, pk)
    if not (crops_dir / f"{prefix}_{q}.png").exists():
        missing_imgs.append(f"{prefix}_{q}.png")
if crop_prefix and not missing_imgs:
    ok(f"{len(practice_keys)} 張主裁切圖齊全")
elif not crop_prefix:
    warn("抓不到 examPapers 的 crop 欄位，跳過圖檔檢查")
else:
    for name in sorted(missing_imgs):
        fail(f"缺裁切圖 assets/exam_crops/{name}")

# ---------------------------------------------------------- 7. SVG 平衡
print("[7] SVG 標籤平衡")
hit = False
for f, text in texts.items():
    o, c = text.count("<svg"), text.count("</svg>")
    if o != c:
        hit = True
        fail(f"{f.name} <svg>×{o} 與 </svg>×{c} 不平衡")
if not hit:
    ok("SVG 開閉平衡")

# ---------------------------------------------------------------- 結果
print()
if failures:
    print(f"✗ {len(failures)} 項 FAIL，{len(warnings)} 項 WARN")
    sys.exit(1)
print(f"✓ 全部通過（{len(warnings)} 項 WARN 供人工參考）")
