# Kepler's Second Law Diagram Angle Adjustment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Modify the SVG swept sector angles for Kepler's Second Law in `gsat_physics_review.html` to make the left sector narrower and the right sector proportionally smaller for visual balance.

**Architecture:** Edit the static Javascript function `diagN07` within the single-page HTML file.

**Tech Stack:** HTML5, Inline JavaScript, Inline SVG.

## Global Constraints
- Do not affect any other diagram or layout styling.
- Keep the script syntax simple and vanilla JS.

---

### Task 1: Update Kepler's Second Law Diagram Angles

**Files:**
- Modify: `gsat_physics_review.html:5699-5700`

**Interfaces:**
- Consumes: None
- Produces: None

- [ ] **Step 1: Modify left and right sector angles**
  In [gsat_physics_review.html](file:///f:/Program/phy-senior/gsat_physics_review.html) around line 5699, modify:
  ```javascript
  s += sector(150, 210, 'rgba(37,99,235,0.16)', DG.blue);
  s += sector(-16, 16, 'rgba(5,150,105,0.16)', DG.green);
  ```
  to:
  ```javascript
  s += sector(160, 200, 'rgba(37,99,235,0.16)', DG.blue);
  s += sector(-12, 12, 'rgba(5,150,105,0.16)', DG.green);
  ```

- [ ] **Step 2: Commit the changes**
  Run:
  ```bash
  git add gsat_physics_review.html
  git commit -m "style: adjust Kepler's Second Law diagram angles for visual balance"
  ```
