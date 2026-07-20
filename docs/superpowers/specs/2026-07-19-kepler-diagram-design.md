# Kepler's Second Law Diagram Angle Adjustment Design

## Goal
Adjust the angles of the swept sectors in Kepler's Second Law diagram (等面積律) to improve visual aesthetics:
1. Make the left (blue/purple) area angle smaller (narrower).
2. Scale down the right (green) area angle proportionally to maintain visual balance and the representation of equal area.

## Proposed Changes

### GSAT Physics Review HTML

#### [MODIFY] [gsat_physics_review.html](file:///f:/Program/phy-senior/gsat_physics_review.html)
Update the sector calls in `diagN07()`:
- Left sector (甲): change angle range from `150, 210` (60° span) to `160, 200` (40° span).
- Right sector (乙): change angle range from `-16, 16` (32° span) to `-12, 12` (24° span).

```javascript
// Before
s += sector(150, 210, 'rgba(37,99,235,0.16)', DG.blue);
s += sector(-16, 16, 'rgba(5,150,105,0.16)', DG.green);

// After
s += sector(160, 200, 'rgba(37,99,235,0.16)', DG.blue);
s += sector(-12, 12, 'rgba(5,150,105,0.16)', DG.green);
```

## Verification
- Reload the `gsat_physics_review.html` in a web browser.
- Scroll down to the **克卜勒第二定律：等面積律** diagram under module **N07**.
- Verify that both sectors are rendering correctly and that the left sector looks cleaner and narrower, with the overall diagram looking balanced.
