# Electrostatics and Electric Field Section Design Spec

## Goal
Add detailed content for "Electric Field" (電場) and "Electric Field Lines" (電力線) to the "Electrostatics and Coulomb's Law" (靜電與庫侖定律, N19) section, utilizing a clear analogy to "Magnetic Field" (磁場) and "Magnetic Field Lines" (磁力線).

## Target Files
1. [gsat_physics_review.html](file:///f:/Program/phy-senior/gsat_physics_review.html)
2. [modulesData.js](file:///f:/Program/phy-senior/data/modulesData.js)

## Proposed Design

### 1. Core Formula Card Addition
In [modulesData.js](file:///f:/Program/phy-senior/data/modulesData.js), we will add a second formula card under the node `N19` to represent the core definition of the Electric Field:
- **Name**: `電場的定義`
- **Formula**: `E = \\frac{F}{q}`
- **Description**: `電場定義為單位正電荷在該點所受的靜電力。電場的方向規定為正電荷在該點的受力方向。`

### 2. Custom HTML Section for Node N19
In [gsat_physics_review.html](file:///f:/Program/phy-senior/gsat_physics_review.html), we will define a new function `electrostaticsSectionHtml()` that returns the HTML for three layers of detailed information matching our information architecture rules:
- **💡 核心觀念解析：電場與電力線的物理本質** (Explanation of Principles):
  - Discuss the transition from "action-at-a-distance" (超距力) to "field" (場) theory.
  - Formulate the analogy of electric field/lines to magnetic field/lines.
- **🔍 電場與磁場的特性對照** (Clarifying Details):
  - Create a structured table comparing Electric Field vs. Magnetic Field, and Electric Field Lines vs. Magnetic Field Lines (monopoles vs. dipoles, loop structure, tangent/density rules, no crossing).
- **📝 生活應用與避雷針原理** (Application Examples):
  - Connect concepts to "Tip Discharge" (尖端放電) with applications like lightning rods (避雷針) and Shen Kuo's *Mengxi Bitan* recording.
  - Connect to "Electrostatic Shielding" (靜電屏蔽) with applications like anti-static clothing (防靜電工作服) and metal shells.

### 3. Inject Special HTML for Node N19
In the `renderNodeView(nodeId)` function in [gsat_physics_review.html](file:///f:/Program/phy-senior/gsat_physics_review.html), we will inject the new section when `nodeId === 'N19'`:
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

## Verification
- Load `gsat_physics_review.html` in a web browser.
- Navigate to node **N19 靜電與庫侖定律**.
- Verify that:
  - The formula cards contain both Coulomb's Law and the Electric Field Definition.
  - The special sections are rendered below the formula cards in the correct hierarchical order:
    1. 💡 核心觀念解析
    2. 🔍 電場與磁場的特性對照 (Table)
    3. 📝 生活應用與避雷針原理
