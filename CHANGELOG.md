# Changelog - Swarm Robots κ Analysis

## [2.0.0] - 2025-11-08

### 🎉 Major Update: Fig8 Correction

**BREAKTHROUGH:** Resolved Fig8 κ discrepancy (0.71 → 0.96)

#### Fixed
-  **Problem:** Fig8 gave κ = 0.71 (not ≈ 1)
- 🔍 **Root cause:** Used d_nn instead of ⟨NND⟩
-  **Solution:** Correction ratio d_nn/⟨NND⟩ = 0.741
-  **Result:** κ = 0.960 ≈ 1 for Fig8!

#### Added
- Complete CSV dataset (21 conditions, both experiments)
- `PARAMETER_JUSTIFICATION_EN.md` (258 lines)
- `analyze_fig5_fig8.py` - combined analysis
- `run_statistical_tests.py` - validation
- Statistical validation (t-test, CI)
- Bilingual documentation (EN + Ukrainian)

#### Changed
- Updated formula: κ = ψ × (⟨NND⟩/202.7)
- Fixed all file paths (from /home/claude/ to relative)
- Simplified analysis pipeline (CSV-based)

#### Results
- Fig5: κ = 0.991 
- Fig8: κ = 0.960 
- Mean: κ = 0.976 ± 0.022
- t-test: p = 0.359 (H0: κ=1 not rejected)
- 95% CI: [0.779, 1.172] (contains κ=1)

---

## [1.0.0] - 2025-11-07

### Initial Release

#### Features
- Fig5 analysis (collective response)
- κ calculation using simplified formula
- Basic visualization
- Documentation structure

#### Known Issues
- Fig8 not analyzed (addressed in 2.0.0)
- Formula oversimplified (corrected in 2.0.0)

---

## Future Plans

### [2.1.0] - Planned
- [ ] Enhanced visualizations (3D phase diagrams)
- [ ] Comparison with more systems
- [ ] Interactive dashboard

### [3.0.0] - Planned
- [ ] Integration into main paper
- [ ] Extended to variable N (10-100 robots)
- [ ] Real-world task experiments

---

**Maintainer:** Oleksii Onasenko  
**Status:** Publication Ready 
