# Electric Field Lines Diagram Update Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Modify the Electric Field Lines diagram under N19 to focus on a single positive charge $+q$ (as required by the curriculum) and correct the Magnetic Field Lines diagram to loop properly from the ends of the bar magnet (N to S outside, S to N inside).

**Architecture:** Update `diagN19_fieldLines()` in `gsat_physics_review.html`.

**Tech Stack:** SVG, JavaScript.

---

### Task 1: Update diagN19_fieldLines() in HTML

**Files:**
- Modify: [gsat_physics_review.html](file:///f:/Program/phy-senior/gsat_physics_review.html)

- [ ] **Step 1: Rewrite diagN19_fieldLines()**
  In [gsat_physics_review.html](file:///f:/Program/phy-senior/gsat_physics_review.html), replace the body of `diagN19_fieldLines()` with:
  ```javascript
          function diagN19_fieldLines() {
              let s = '';
              // Middle divider
              s += `<line x1="260" y1="20" x2="260" y2="220" stroke="${DG.grid}" stroke-width="1.2" stroke-dasharray="4 3"/>`;
              
              // Titles
              s += dgTxt(130, 28, '單一正電荷的電力線 (放射狀、非閉合)', { fs: 11.5, b: 1, fill: DG.ink });
              s += dgTxt(390, 28, '條形磁鐵的磁力線 (外部 N→S、內部 S→N 閉合)', { fs: 11.5, b: 1, fill: DG.ink });

              // Left Side: Single Positive Charge
              const ex = 130, ey = 120;
              const rStart = 10;
              const rEnd = 54;
              const angles = [0, 45, 90, 135, 180, 225, 270, 315];
              
              angles.forEach(a => {
                  const rad = a * Math.PI / 180;
                  const x1 = ex + rStart * Math.cos(rad);
                  const y1 = ey + rStart * Math.sin(rad);
                  const x2 = ex + rEnd * Math.cos(rad);
                  const y2 = ey + rEnd * Math.sin(rad);
                  s += dgArrow(x1, y1, x2, y2, DG.blue, 1.5);
              });
              
              // Positive charge circle
              s += `<circle cx="${ex}" cy="${ey}" r="9" fill="${DG.rose}" stroke="#fff" stroke-width="1.2"/>` + dgTxt(ex, ey + 4, '+', { fill: '#fff', b: 1, fs: 13 });
              s += dgTxt(ex, ey - 14, '+q', { fs: 10.5, fill: DG.rose, b: 1 });

              // Right Side: Bar Magnet (N on Left, S on Right)
              const mx = 390, my = 120;
              const mw = 76, mh = 26;
              
              // Outside loops (N to S: Left to Right)
              // Loop 1 (Inner top)
              s += `<path d="M ${mx - 30} ${my - mh/2} C ${mx - 30} 50, ${mx + 30} 50, ${mx + 30} ${my - mh/2}" fill="none" stroke="${DG.green}" stroke-width="1.5"/>`;
              s += dgArrow(mx - 2, 64, mx + 2, 64, DG.green, 1.5);
              
              // Loop 2 (Outer top)
              s += `<path d="M ${mx - 38} ${my - mh/2 + 5} C ${mx - 60} 20, ${mx + 60} 20, ${mx + 38} ${my - mh/2 + 5}" fill="none" stroke="${DG.green}" stroke-width="1.5"/>`;
              s += dgArrow(mx - 2, 43, mx + 2, 43, DG.green, 1.5);
              
              // Loop 3 (Inner bottom)
              s += `<path d="M ${mx - 30} ${my + mh/2} C ${mx - 30} 190, ${mx + 30} 190, ${mx + 30} ${my + mh/2}" fill="none" stroke="${DG.green}" stroke-width="1.5"/>`;
              s += dgArrow(mx - 2, 176, mx + 2, 176, DG.green, 1.5);
              
              // Loop 4 (Outer bottom)
              s += `<path d="M ${mx - 38} ${my + mh/2 - 5} C ${mx - 60} 220, ${mx + 60} 220, ${mx + 38} ${my + mh/2 - 5}" fill="none" stroke="${DG.green}" stroke-width="1.5"/>`;
              s += dgArrow(mx - 2, 197, mx + 2, 197, DG.green, 1.5);

              // Inside lines (S to N: Right to Left)
              s += `<line x1="${mx + 38}" y1="${my}" x2="${mx - 38}" y2="${my}" stroke="${DG.green}" stroke-width="1.2" stroke-dasharray="3 2"/>`;
              s += dgArrow(mx + 5, my, mx - 5, my, DG.green, 1.2);
              
              s += `<line x1="${mx + 30}" y1="${my - 6}" x2="${mx - 30}" y2="${my - 6}" stroke="${DG.green}" stroke-width="1.2" stroke-dasharray="3 2"/>`;
              s += dgArrow(mx + 5, my - 6, mx - 5, my - 6, DG.green, 1.2);
              
              s += `<line x1="${mx + 30}" y1="${my + 6}" x2="${mx - 30}" y2="${my + 6}" stroke="${DG.green}" stroke-width="1.2" stroke-dasharray="3 2"/>`;
              s += dgArrow(mx + 5, my + 6, mx - 5, my + 6, DG.green, 1.2);

              // Magnet Body
              // Left Half: N (Red)
              s += `<path d="M ${mx - 38 + 2} ${my - mh/2} L ${mx} ${my - mh/2} L ${mx} ${my + mh/2} L ${mx - 38 + 2} ${my + mh/2} A 2 2 0 0 1 ${mx - 38} ${my + mh/2 - 2} L ${mx - 38} ${my - mh/2 + 2} A 2 2 0 0 1 ${mx - 38 + 2} ${my - mh/2} Z" fill="${DG.rose}" stroke="#334155" stroke-width="1.2"/>`;
              // Right Half: S (Ink/Blue)
              s += `<path d="M ${mx} ${my - mh/2} L ${mx + 38 - 2} ${my - mh/2} A 2 2 0 0 1 ${mx + 38} ${my - mh/2 + 2} L ${mx + 38} ${my + mh/2 - 2} A 2 2 0 0 1 ${mx + 38 - 2} ${my + mh/2} L ${mx} ${my + mh/2} Z" fill="${DG.ink}" stroke="#334155" stroke-width="1.2"/>`;
              
              // Labels
              s += dgTxt(mx - 19, my + 4, 'N', { fill: '#fff', b: 1, fs: 12.5 });
              s += dgTxt(mx + 19, my + 4, 'S', { fill: '#fff', b: 1, fs: 12.5 });
              
              return dgCard('電力線與磁力線之物理模型對照（單一電荷放射狀 vs. 磁鐵閉合迴圈）', dgSvg(520, 240, s),
                  '電力線發自正電荷指向無限遠（非封閉）；磁力線則為連續的封閉迴圈，外部由 N 極指向 S 極，內部由 S 極指向 N 極。課綱強調「單一電荷電力線」與「磁鐵磁力線」的定性對照。');
          }
  ```

---

### Task 2: Commit and Verify

- [ ] **Step 1: Commit the changes**
  Run:
  ```bash
  git add gsat_physics_review.html
  git commit -m "style: fix Electric and Magnetic Field Lines diagram path and representation"
  ```

- [ ] **Step 2: Verify locally**
  Confirm the single positive charge diagram and correct magnetic loops in the browser.
