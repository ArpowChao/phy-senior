# Current Magnetic Effect Content and Diagram Addition Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add detailed explanation sections (Explanation of Principles, Clarifying Details, Application Examples) and a high-quality side-by-side SVG diagram for Oersted's Current Magnetic Effect (電流磁效應, N20) in `gsat_physics_review.html`.

**Architecture:** 
1. Define `magnetismSectionHtml()` in `gsat_physics_review.html` and inject it under `N20`.
2. Define `diagN20()` in `gsat_physics_review.html` and register it in `makers`.

**Tech Stack:** JavaScript, HTML5, SVG.

---

### Task 1: Create magnetismSectionHtml() & Inject into specialHtml

**Files:**
- Modify: [gsat_physics_review.html](file:///f:/Program/phy-senior/gsat_physics_review.html)

- [ ] **Step 1: Define magnetismSectionHtml()**
  Define `magnetismSectionHtml()` in [gsat_physics_review.html](file:///f:/Program/phy-senior/gsat_physics_review.html) right after `electrostaticsSectionHtml()`:
  ```javascript
          function magnetismSectionHtml() {
              return `
                  <div class="handout-section-title" style="margin-top: 1.5rem;">💡 核心觀念解析：厄斯特的發現與安培右手定則</div>
                  <p class="content-subtitle">厄斯特於 1820 年偶然發現通電導線會使下方的磁針發生偏轉，揭開了「電生磁」的序幕，成為建立電動力學的第一座橋梁。磁場方向由安培右手定則判定：</p>
                  
                  <div class="edu-card" style="margin-bottom: 1.5rem;">
                      <h4 style="margin-top:0; color:var(--primary-blue);">1. 載流直導線的磁場與右手定則</h4>
                      <p style="font-size:0.92rem; line-height:1.6; color:var(--text-main);">
                          <b>直導線右手定則</b>：右手大拇指指向<b>電流 $I$</b> 的方向，四指彎曲環繞導線的方向即為<b>磁場 $B$</b> 的方向。
                      </p>
                      <ul style="font-size:0.92rem; line-height:1.6; color:var(--text-main); padding-left:1.25rem;">
                          <li><b>磁場形態</b>：以導線為中心的同心圓。距離導線愈近，磁場愈強。</li>
                          <li><b>視角符號（必考）</b>：為在二維紙面上作圖，物理學規定：
                              <br>• <b>$\odot$（圓圈內點）</b>：代表電流或磁場方向<b>垂直穿出紙面</b>（如箭頭迎面飛來）。
                              <br>• <b>$\otimes$（圓圈內叉）</b>：代表電流或磁場方向<b>垂直穿入紙面</b>（如箭尾背向飛去）。
                          </li>
                      </ul>
                  </div>

                  <div class="edu-card" style="margin-bottom: 1.5rem;">
                      <h4 style="margin-top:0; color:var(--primary-blue);">2. 載流螺線管（線圈）的磁場與右手定則</h4>
                      <p style="font-size:0.92rem; line-height:1.6; color:var(--text-main);">
                          當直導線繞成螺旋狀時，各圈導線產生的磁場會在管內疊加，形成極為均勻的平行磁場。
                      </p>
                      <ul style="font-size:0.92rem; line-height:1.6; color:var(--text-main); padding-left:1.25rem;">
                          <li><b>螺線管右手定則</b>：右手四指順著<b>線圈上的電流 $I$</b> 環繞彎曲，大拇指所指的方向即為<b>管內磁場 $B$</b> 的方向（等效於電磁鐵的 N 極端）。</li>
                          <li><b>內外部磁場對照</b>：外部磁力線由 N 極出發、收於 S 極；<b>內部磁力線則平行且緊密，由 S 極指向 N 極</b>，形成一條完整的閉合曲線。</li>
                      </ul>
                  </div>

                  <div class="handout-section-title">🔍 載流導線磁場形態與作圖剖析</div>
                  <div class="edu-table-container">
                      <table class="edu-table">
                          <thead>
                              <tr>
                                  <th style="width: 25%">導線形態</th>
                                  <th style="width: 40%">磁力線幾何形狀</th>
                                  <th style="width: 35%">大考作圖與磁場強度特徵</th>
                              </tr>
                          </thead>
                          <tbody>
                              <tr>
                                  <td><b>載流直導線</b></td>
                                  <td>以導線為同心圓中心，磁場平面與導線垂直。</td>
                                  <td>大考常用 $\\odot$ 與 $\\otimes$ 畫出導線截面，判斷兩側磁場疊加（如同向電流相吸、反向電流相斥的定性判斷）。</td>
                              </tr>
                              <tr>
                                  <td><b>載流單圓環導線</b></td>
                                  <td>靠近導線處為同心圓，圓環中心處磁力線收斂為一條垂直通過環心的直線。</td>
                                  <td>大考主要考察環心處的磁場方向判定。大拇指指環心磁場，四指順著圓環電流環繞。</td>
                              </tr>
                              <tr>
                                  <td><b>載流螺線管 (電磁鐵)</b></td>
                                  <td><b>管內</b>：平行且均勻的強磁場。<br><b>管外</b>：與條形磁鐵（Bar Magnet）磁場完全相同。</td>
                                  <td>管內磁場方向為 <b>S $\\to$ N</b>。管內磁場強度與電流大小、單位長度圈數成正比，與管子長度無關。</td>
                              </tr>
                          </tbody>
                      </table>
                  </div>

                  <div class="handout-section-title">📝 生活應用與電磁鐵增強實戰</div>
                  <div class="edu-card" style="margin-bottom: 2rem;">
                      <div style="font-weight: 700; color: var(--accent-rose); margin-bottom: 0.5rem;">⚡ 電磁起重機與馬達的物理本質</div>
                      <p style="font-size: 0.92rem; line-height: 1.6; color: var(--text-main);">
                          電流磁效應是現代電機與生活科技的基石：
                      </p>
                      <ul style="font-size:0.92rem; line-height:1.6; color:var(--text-main); padding-left:1.25rem; margin-bottom:1rem;">
                          <li><b>電磁鐵 (Electromagnet)</b>：在載流螺線管中套入一個<b>軟鐵芯 (Soft Iron Core)</b>。通電時，軟鐵芯被急速磁化，使整體磁場增強數千倍；斷電時，軟鐵芯迅速退磁，磁性消失。此即為「可控制磁性」的磁鐵。
                              <br>• <i>增強磁場三要素</i>：<b>① 增加電流 $I$</b>；<b>② 增加單位長度的線圈圈數 $n$</b>；<b>③ 套入高導磁材料（如鐵芯）</b>。
                              <br>• <i>生活實例</i>：電磁起重機（吸放廢鐵）、傳統電鈴、磁浮列車。
                          </li>
                          <li><b>電動機 (馬達) 與揚聲器 (喇叭)</b>：馬達是利用「電流在磁場中受磁力作用（載流導線受力 $F = ILB$）」來產生旋轉力矩，將電能轉換為機械能；喇叭則是利用變動電流在磁場中受力，帶動紙盆振動發聲。
                          </li>
                      </ul>
                  </div>
              `;
          }
  ```

- [ ] **Step 2: Inject magnetismSectionHtml() into specialHtml**
  In [gsat_physics_review.html](file:///f:/Program/phy-senior/gsat_physics_review.html) around line 3117 (under `N19` entry), add `+ (nodeId === 'N20' ? magnetismSectionHtml() : '')`:
  ```javascript
              const specialHtml = (nodeId === 'N01' ? siSectionHtml() : '')
                  + (nodeId === 'N02' ? scaleSectionHtml() : '')
                  + (nodeId === 'N06' ? matterSectionHtml() : '')
                  + (nodeId === 'N03' ? kinematicsGraphsHtml() : '')
                  + (nodeId === 'N07' ? keplerSectionHtml() : '')
                  + (nodeId === 'N19' ? electrostaticsSectionHtml() : '')
                  + (nodeId === 'N20' ? magnetismSectionHtml() : '') // New injection
                  + (nodeId === 'N18' ? emSpectrumSectionHtml() : '')
                  + (nodeId === 'N23' ? photoelectricSectionHtml() : '')
                  + (nodeId === 'N28' ? blackbodyQuantumSectionHtml() : '')
                  + (nodeId === 'N27' ? fourForcesSectionHtml() : '');
  ```

---

### Task 2: Implement diagN20() and Register in makers

**Files:**
- Modify: [gsat_physics_review.html](file:///f:/Program/phy-senior/gsat_physics_review.html)

- [ ] **Step 1: Add diagN20() function definition**
  Define `diagN20()` in [gsat_physics_review.html](file:///f:/Program/phy-senior/gsat_physics_review.html) right before `diagN21()` or right after `diagN19_fieldLines()`:
  ```javascript
          function diagN20() {
              let s = '';
              // Middle divider
              s += `<line x1="260" y1="20" x2="260" y2="220" stroke="${DG.grid}" stroke-width="1.2" stroke-dasharray="4 3"/>`;
              
              // Titles
              s += dgTxt(130, 28, '載流直導線的環形磁場', { fs: 11.5, b: 1, fill: DG.ink });
              s += dgTxt(390, 28, '載流螺線管的磁場 (等效條形磁鐵)', { fs: 11.5, b: 1, fill: DG.ink });

              // Left Side: Straight Wire
              const cx = 130, cy = 120;
              const wireColor = '#64748b';
              
              // Draw back half of concentric magnetic field lines (y < cy)
              s += `<path d="M ${cx - 24} ${cy} A 24 7 0 0 1 ${cx + 24} ${cy}" fill="none" stroke="${DG.green}" stroke-width="1.5" stroke-dasharray="3 2"/>`;
              s += `<path d="M ${cx - 42} ${cy + 25} A 42 12 0 0 1 ${cx + 42} ${cy + 25}" fill="none" stroke="${DG.green}" stroke-width="1.5" stroke-dasharray="3 2"/>`;
              s += `<path d="M ${cx - 60} ${cy - 25} A 60 17 0 0 1 ${cx + 60} ${cy - 25}" fill="none" stroke="${DG.green}" stroke-width="1.5" stroke-dasharray="3 2"/>`;

              // Draw the wire
              s += `<line x1="${cx}" y1="42" x2="${cx}" y2="198" stroke="${wireColor}" stroke-width="5" stroke-linecap="round"/>`;
              s += dgArrow(cx, 170, cx, 65, DG.rose, 2.2); // Current arrow
              s += dgTxt(cx - 18, 56, 'I', { fill: DG.rose, b: 1, fs: 13 });
              s += dgTxt(cx + 36, 178, '電流方向', { fill: DG.rose, fs: 10 });

              // Draw front half of magnetic field lines (y > cy) with arrows pointing left (counter-clockwise)
              s += `<path d="M ${cx + 24} ${cy}" A 24 7 0 0 1 ${cx - 24} ${cy}" fill="none" stroke="${DG.green}" stroke-width="1.5"/>`;
              s += dgArrow(cx + 2, cy + 7, cx - 2, cy + 7, DG.green, 1.5);
              s += dgTxt(cx + 36, cy + 10, 'B', { fill: DG.green, b: 1, fs: 11 });

              s += `<path d="M ${cx + 42} ${cy + 25} A 42 12 0 0 1 ${cx - 42} ${cy + 25}" fill="none" stroke="${DG.green}" stroke-width="1.5"/>`;
              s += dgArrow(cx + 2, cy + 25 + 12, cx - 2, cy + 25 + 12, DG.green, 1.5);

              s += `<path d="M ${cx + 60} ${cy - 25} A 60 17 0 0 1 ${cx - 60} ${cy - 25}" fill="none" stroke="${DG.green}" stroke-width="1.5"/>`;
              s += dgArrow(cx + 2, cy - 25 + 17, cx - 2, cy - 25 + 17, DG.green, 1.5);

              // Right Side: Solenoid
              const mx = 390, my = 120;
              const mw = 76, mh = 26;
              
              // Draw S-N field lines outside solenoid N (left) -> S (right)
              s += `<path d="M ${mx - 32} ${my - mh/2} C ${mx - 32} 55, ${mx + 32} 55, ${mx + 32} ${my - mh/2}" fill="none" stroke="${DG.green}" stroke-width="1.5"/>`;
              s += dgArrow(mx - 2, 69, mx + 2, 69, DG.green, 1.5);
              
              s += `<path d="M ${mx - 32} ${my + mh/2} C ${mx - 32} 185, ${mx + 32} 185, ${mx + 32} ${my + mh/2}" fill="none" stroke="${DG.green}" stroke-width="1.5"/>`;
              s += dgArrow(mx - 2, 171, mx + 2, 171, DG.green, 1.5);

              // Draw field lines inside (S to N: Right to Left)
              s += `<line x1="${mx + 45}" y1="${my}" x2="${mx - 45}" y2="${my}" stroke="${DG.green}" stroke-width="1.2" stroke-dasharray="3 2"/>`;
              s += dgArrow(mx + 5, my, mx - 5, my, DG.green, 1.2);
              
              s += `<line x1="${mx + 40}" y1="${my - 6}" x2="${mx - 40}" y2="${my - 6}" stroke="${DG.green}" stroke-width="1.2" stroke-dasharray="3 2"/>`;
              s += dgArrow(mx + 5, my - 6, mx - 5, my - 6, DG.green, 1.2);
              
              s += `<line x1="${mx + 40}" y1="${my + 6}" x2="${mx - 40}" y2="${my + 6}" stroke="${DG.green}" stroke-width="1.2" stroke-dasharray="3 2"/>`;
              s += dgArrow(mx + 5, my + 6, mx - 5, my + 6, DG.green, 1.2);

              // Draw N/S labels
              s += dgTxt(mx - 54, my + 4, 'N', { fill: DG.rose, b: 1, fs: 13 });
              s += dgTxt(mx + 54, my + 4, 'S', { fill: DG.ink, b: 1, fs: 13 });

              // Draw Solenoid Windings
              const xs = [350, 370, 390, 410, 430];
              // Back half of windings (drawn first)
              xs.forEach(x => {
                  s += `<path d="M ${x} 107 A 12 18 0 0 0 ${x} 133" fill="none" stroke="${wireColor}" stroke-width="2.2" stroke-dasharray="3 2" opacity="0.65"/>`;
              });

              // Draw core cylinder behind front wires
              s += `<rect x="${mx - 45}" y="${my - 12}" width="90" height="24" rx="2" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1" opacity="0.8"/>`;
              
              // Front half of windings (slanted, going up-right)
              xs.forEach((x, idx) => {
                  if (idx < xs.length - 1) {
                      s += `<path d="M ${x} 133 L ${x + 20} 107" fill="none" stroke="${wireColor}" stroke-width="3" stroke-linecap="round"/>`;
                      s += dgArrow(x + 7, 124, x + 13, 116, DG.rose, 1.2);
                  }
              });

              // Leads
              s += `<line x1="335" y1="152" x2="350" y2="133" stroke="${wireColor}" stroke-width="3" stroke-linecap="round"/>`;
              s += dgArrow(335, 152, 344, 140, DG.rose, 1.2);
              
              s += `<line x1="430" y1="107" x2="445" y2="88" stroke="${wireColor}" stroke-width="3" stroke-linecap="round"/>`;
              s += dgArrow(430, 107, 439, 95, DG.rose, 1.2);
              
              s += dgTxt(332, 164, 'I (入)', { fill: DG.rose, fs: 9.5 });
              s += dgTxt(452, 82, 'I (出)', { fill: DG.rose, fs: 9.5 });

              return dgCard('載流直導線與螺線管的磁場對照圖（安培右手定則）', dgSvg(520, 240, s),
                  '直導線：以大拇指指向電流，四指環繞方向即為同心圓磁場 B。螺線管：以四指環繞線圈電流，大拇指所指即為內部磁場方向（等效 N 極端，磁力線由 S 指向 N 閉合）。');
          }
  ```

- [ ] **Step 2: Register diagN20 in makers**
  In [gsat_physics_review.html](file:///f:/Program/phy-senior/gsat_physics_review.html) (around line 6095), add `N20: diagN20` to `const makers`:
  ```javascript
  const makers = { N04: diagN04, N05: diagN05, N07: diagN07, N14: diagN14, N15: diagN15, N16: diagN16, N17: diagN17, N19: diagN19, N20: diagN20, N21: diagN21, N23: diagN23, N24: diagN24, N26: diagN26, N28: diagN28 };
  ```

---

### Task 3: Commit and Verify

- [ ] **Step 1: Commit the changes**
  Run:
  ```bash
  git add gsat_physics_review.html
  git commit -m "feat: add magnetismSectionHtml and diagN20 to current magnetic effect section"
  ```

- [ ] **Step 2: Verify locally**
  Refresh the page on N20, confirm formula card, key features, SVG diagram, and custom comparison and application sections render properly.
