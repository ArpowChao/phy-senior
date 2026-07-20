# Electrostatics and Electric Field Addition Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Electric Field and Electric Field Lines content (including Magnetic Field analogy and applications) to the Electrostatics and Coulomb's Law (N19) section.

**Architecture:** Add a formula card in `data/modulesData.js`, add `electrostaticsSectionHtml()` in `gsat_physics_review.html`, and inject it into `renderNodeView()`.

**Tech Stack:** JavaScript, HTML5, MathJax (LaTeX).

## Global Constraints
- Ensure all LaTeX symbols are correctly escaped with double backslashes in JS strings (e.g. `\\frac`).
- Align headings with standard rules: `💡 核心觀念解析：...`, `🔍 電場與磁場的特性對照`, `📝 生活應用與避雷針原理`.

---

### Task 1: Add Electric Field Definition Formula Card
**Files:**
- Modify: `data/modulesData.js:551-552`

- [ ] **Step 1: Edit modulesData.js to add formula card**
  In [modulesData.js](file:///f:/Program/phy-senior/data/modulesData.js), insert the formula object under `formulas` for module 6:
  ```javascript
              {node: 'N19',
                  name: "電場定義",
                  formula: "E = \\frac{F}{q}",
                  desc: "電場為單位正電荷在該點所受的靜電力。電場的方向規定為正電荷在該點的受力方向。"
              },
  ```

---

### Task 2: Implement Electrostatics Section HTML & Injection
**Files:**
- Modify: `gsat_physics_review.html:3115-3116`
- Modify: `gsat_physics_review.html:5622-5623`

- [ ] **Step 1: Add electrostaticsSectionHtml() definition**
  In [gsat_physics_review.html](file:///f:/Program/phy-senior/gsat_physics_review.html), insert the `electrostaticsSectionHtml()` function right before `fourForcesSectionHtml()` or `const DG`:
  ```javascript
          function electrostaticsSectionHtml() {
              return `
                  <div class="handout-section-title" style="margin-top: 1.5rem;">💡 核心觀念解析：電場與電力線的物理本質</div>
                  <p class="content-subtitle">在物理學中，電荷之間的靜電力是如何跨越空間發揮作用的？「場」的概念是解決超距力本質的關鍵橋樑，我們常將其與磁場進行類比：</p>
                  
                  <div class="edu-card" style="margin-bottom: 1.5rem;">
                      <h4 style="margin-top:0; color:var(--primary-blue);">1. 從「超距力」到「場 (Field)」的抽象建立</h4>
                      <p style="font-size:0.92rem; line-height:1.6; color:var(--text-main);">
                          庫侖定律描述了兩個靜止電荷間的交互作用力，但電荷如何「得知」另一個電荷的存在？
                      </p>
                      <ul style="font-size:0.92rem; line-height:1.6; color:var(--text-main); padding-left:1.25rem;">
                          <li><b>場的觀點</b>：帶電體 $Q$ 會在其周圍空間建立<b>電場 (Electric Field)</b>。當另一個電荷 $q$ 進入此空間時，它是與該處的「電場」發生局部交互作用，進而受到靜電力 $F = qE$。</li>
                          <li><b>磁場的類比</b>：正如磁鐵在其周圍空間建立<b>磁場 (Magnetic Field)</b>，並對放入其中的磁極或電流施加磁力。場是物質存在的一種形式，具有能量與動量。</li>
                      </ul>
                  </div>

                  <div class="edu-card" style="margin-bottom: 1.5rem;">
                      <h4 style="margin-top:0; color:var(--primary-blue);">2. 力線的引入：電場與磁場的幾何視覺化</h4>
                      <p style="font-size:0.92rem; line-height:1.6; color:var(--text-main);">
                          法拉第首創用「力線」來定性描繪場的強弱與方向：
                      </p>
                      <ul style="font-size:0.92rem; line-height:1.6; color:var(--text-main); padding-left:1.25rem;">
                          <li><b>電力線 (Electric Field Lines)</b>：用以描繪電場分佈的假想曲線。電力線的切線方向代表該點的電場方向（即正電荷受力方向）；電力線的疏密程度代表電場強度（越密越強）。</li>
                          <li><b>磁力線 (Magnetic Field Lines)</b>：用以描繪磁場分佈的假想曲線。與電力線相似，其切線代表磁場方向，疏密代表磁場強度。</li>
                      </ul>
                  </div>

                  <div class="handout-section-title">🔍 電場與磁場的特性對照</div>
                  <div class="edu-table-container">
                      <table class="edu-table">
                          <thead>
                              <tr>
                                  <th style="width: 20%">比較項目</th>
                                  <th style="width: 40%">電場與電力線 (Electrostatics)</th>
                                  <th style="width: 40%">磁場與磁力線 (Magnetism)</th>
                              </tr>
                          </thead>
                          <tbody>
                              <tr>
                                  <td><b>場的定義</b></td>
                                  <td>單位正試驗電荷受到的靜電力：$E = F/q$。</td>
                                  <td>由磁針 N 極受力方向定義磁場方向（量值與電流受力有關）。</td>
                              </tr>
                              <tr>
                                  <td><b>基本源頭</b></td>
                                  <td><b>正、負電荷</b>（存在單一正電荷或單一負電荷，即「電單極子」）。</td>
                                  <td><b>N、S 磁極</b>（自然界中不存在單一磁極，即「磁單極子」不存在，必成對出現）。</td>
                              </tr>
                              <tr>
                                  <td><b>力線起點與終點</b></td>
                                  <td>發自<b>正電荷</b>（或無限遠），終止於<b>負電荷</b>（或無限遠）。電力線為<b>非封閉曲線</b>。</td>
                                  <td>在外部由 <b>N 極指向 S 極</b>，內部由 <b>S 極指向 N 極</b>。磁力線為<b>封閉曲線</b>。</td>
                              </tr>
                              <tr>
                                  <td><b>共同特性</b></td>
                                  <td colspan="2" style="text-align: center;">① 力線的<b>切線方向</b>為該點的場方向。&nbsp;&nbsp;&nbsp;&nbsp;② 力線的<b>疏密程度</b>代表場的強弱。<br>③ 空間中任兩條力線<b>絕不相交</b>（否則交點會有兩個場方向，物理上不成立）。</td>
                              </tr>
                          </tbody>
                      </table>
                  </div>

                  <div class="handout-section-title">📝 生活應用與避雷針原理</div>
                  <div class="edu-card" style="margin-bottom: 2rem;">
                      <div style="font-weight: 700; color: var(--accent-rose); margin-bottom: 0.5rem;">⚡ 尖端放電與靜電屏蔽在生活中的實踐</div>
                      <p style="font-size: 0.92rem; line-height: 1.6; color: var(--text-main);">
                          電場與電力線的規律能完美解釋大考常考的靜電現象：
                      </p>
                      <ul style="font-size:0.92rem; line-height:1.6; color:var(--text-main); padding-left:1.25rem; margin-bottom:1rem;">
                          <li><b>尖端放電 (Tip Discharge)</b>：帶電導體表面各處的電荷分佈不均勻，<b>曲率半徑愈小（愈尖銳）的地方，電荷密度愈高</b>。因此，尖端附近的電場極強，容易使周圍空氣分子游離而發生放電現象。
                              <br>• <i>大考實例</i>：<b>避雷針</b>的頂端非常尖銳，當雷雲接近時，避雷針藉由尖端放電將雷雲的電荷緩慢中和，或將閃電直接引導至地面，保護建築物。沈括《夢溪筆談》中記載雷擊僅燒毀木材卻未熔化金屬，即與放電路徑與電磁阻抗有關。
                          </li>
                          <li><b>靜電屏蔽 (Electrostatic Shielding)</b>：一個封閉的金屬空腔導體，在達到靜電平衡時，<b>金屬內部的電場恆為零</b>，內部電力線為零。所有多餘的電荷只會分佈在導體的外表面。
                              <br>• <i>大考實例</i>：<b>防靜電工作服</b>中織有金屬細絲，形成屏蔽網，保護穿戴者免受外部強電場的靜電放電干擾；汽車或飛機遭遇雷擊時，金屬車殼／機身會將電流引導至外表面並流走，車內／機艙內部的人安全無虞。
                          </li>
                      </ul>
                  </div>
              `;
          }
  ```

- [ ] **Step 2: Inject electrostaticsSectionHtml() into specialHtml**
  In [gsat_physics_review.html](file:///f:/Program/phy-senior/gsat_physics_review.html) around line 3115, add `+ (nodeId === 'N19' ? electrostaticsSectionHtml() : '')`:
  ```javascript
              const specialHtml = (nodeId === 'N01' ? siSectionHtml() : '')
                  + (nodeId === 'N02' ? scaleSectionHtml() : '')
                  + (nodeId === 'N06' ? matterSectionHtml() : '')
                  + (nodeId === 'N03' ? kinematicsGraphsHtml() : '')
                  + (nodeId === 'N07' ? keplerSectionHtml() : '')
                  + (nodeId === 'N19' ? electrostaticsSectionHtml() : '') // New injection
                  + (nodeId === 'N18' ? emSpectrumSectionHtml() : '')
                  + (nodeId === 'N23' ? photoelectricSectionHtml() : '')
                  + (nodeId === 'N28' ? blackbodyQuantumSectionHtml() : '')
                  + (nodeId === 'N27' ? fourForcesSectionHtml() : '');
  ```

---

### Task 3: Commit and Verify
- [ ] **Step 1: Commit all changes**
  Run:
  ```bash
  git add gsat_physics_review.html data/modulesData.js
  git commit -m "feat: add Electric Field & Lines analogy and comparison to Electrostatics (N19)"
  ```

- [ ] **Step 2: Manual verification**
  Open the file locally and check that both Coulomb's Law and Electric Field Definition cards show up under N19, and the new subsections are rendered correctly.
