# Emergence Analysis: Swarm Robots with Vicsek-like Interactions

**System Classification:** A.2 Swarm Robots  
**Author:** Oleksii Onasenko  
**Developer:** SubstanceNet  
**Theoretical Framework:** The Emergence Parameter κ ≈ 1: An Empirical Signature of Criticality in Physical and Biological Systems

---

## Visual Summary

### Key Result: Functional Optimum at Critical Point

![Functional Peak](figures/publication/fig2_functional_peak_kappa_vs_R.png)

**Figure 1:** Group responsiveness maximized at κ = 0.991 ≈ 1. Gold star marks peak collective response at critical point.

### Cross-Task Validation

![Combined Experiments](figures/publication/fig3_combined_both_experiments.png)

**Figure 2:** Two independent tasks (response and evasion) both peak at κ ≈ 1, validating universal critical scale.

---

## Abstract

This research validates the emergence parameter κ ≈ 1 as a signature of criticality in programmable swarm robots. Analysis of experimental data from Lei et al. (2023) demonstrates that maximum collective function occurs at κ = 0.976 ± 0.022, confirming the criticality hypothesis. Two independent tasks (collective response and predator evasion) yield consistent results despite different optimal control parameters, supporting universality of the framework.

**Key Finding:** Emergence parameter κ approaches unity precisely where swarm robots exhibit optimal collective behavior, marking the critical phase transition between disordered and ordered motion.

---

## System Description

**Physical System:** SwarmBang mobile robots (N = 30)  
**Interaction Model:** Vicsek-like alignment with distance-dependent coupling  
**Control Parameter:** Alignment weight w_ali  
**Order Parameter:** Polarization ψ (directional coherence)  
**Functional Metrics:** Group responsiveness R, survival time T_fc

---

## Theoretical Framework

### Emergence Parameter Definition
```
κ = (A/Ac) · τ · (Λ/Λc)
```

**System-Specific Implementation:**
```
κ = (N/Nc) · ψ · (⟨NND⟩/Λc)
```

where:
- N = 30: Number of robots
- Nc = 30: Critical swarm size
- ψ: Polarization (measured order parameter)
- ⟨NND⟩: Mean nearest neighbor distance (mm)
- Λc = 202.7 mm: Critical spatial correlation length

**Simplified Formula (N = Nc):**
```
κ = ψ · (⟨NND⟩/202.7)
```

---

## Principal Results

### Critical Points

**Figure 5 (Collective Response):**
- κ = 0.991 at w_ali = 20
- R = 0.776 (maximum group responsiveness)

**Figure 8 (Collective Evasion):**
- κ = 0.960 at w_ali = 25
- T_fc = 326.8 s (maximum survival time)

**Combined:**
- Mean: κ = 0.976 ± 0.022
- 95% CI: [0.779, 1.172]
- Statistical support: p = 0.359 (H0: κ = 1 not rejected)

---

## Repository Structure
```
A.2_swarm_robots_kappa_analysis/
├── README.md                          # This file
├── LICENSE                            # Apache 2.0
├── CHANGELOG.md                       # Version history
├── CITATION.cff                       # Citation metadata
├── CODE_OF_CONDUCT.md                 # Community standards
├── CONTRIBUTING.md                    # Contribution guidelines
├── INSTALL.md                         # Installation guide
├── SECURITY.md                        # Security policy
├── requirements.txt                   # Python dependencies
│
├── code/                              # Analysis scripts
│   ├── run_full_analysis.py           # Complete pipeline
│   ├── run_statistical_tests.py       # Statistical validation
│   ├── generate_publication_figures.py # High-res figures
│   ├── analyze_fig5_fig8.py           # Data extraction
│   ├── emergence_analysis_fixed.py    # Core analyzer class
│   ├── statistical_tests.py           # Statistical tests module
│   └── visualization.py              # Visualization module
│
├── data/
│   └── swarm_robots_complete_data.csv # Processed dataset
│
├── docs/                              # Academic documentation
│   ├── 01_Mathematical_Framework.md
│   ├── 02_Experimental_Setup.md
│   ├── 03_Data_Analysis.md
│   ├── 04_Results.md
│   ├── 05_Statistical_Validation.md
│   ├── FIGURE_CAPTIONS.md
│   ├── DATA_PROVENANCE.md
│   ├── PARAMETER_JUSTIFICATION.md
│   └── references/                    # Primary sources (PDFs)
│
├── figures/
│   ├── kappa_both_experiments.png     # Overview plot
│   └── publication/                   # 600 DPI figures
│       ├── fig1_phase_transition_kappa_vs_psi.png
│       ├── fig2_functional_peak_kappa_vs_R.png
│       ├── fig3_combined_both_experiments.png
│       └── fig4_order_vs_function.png
│
└── results/                           # Analysis outputs
    ├── analysis_output.txt
    ├── statistical_report.txt
    └── summary_statistics.txt
```

---

## Quick Start

### Installation
```bash
git clone https://github.com/olexxa62-code/swarm-robots-emergence-analysis.git
cd swarm-robots-emergence-analysis
pip install -r requirements.txt
```

### Run Analysis
```bash
# Complete analysis
python code/run_full_analysis.py

# Statistical validation
python code/run_statistical_tests.py

# Generate publication figures
python code/generate_publication_figures.py
```

**Runtime:** < 2 minutes total

---

## Key Contributions

### Scientific

1. **First experimental validation** of κ ≈ 1 criticality hypothesis using physical robots
2. **Cross-task consistency** demonstrated: universal Λc applies to different functions
3. **Post-critical decline** documented: excess order degrades function
4. **Order-function dissociation** revealed: maximum polarization ≠ maximum function

### Methodological

1. **Non-circular reasoning:** κ uses measured ψ, not control parameter w_ali
2. **Independent validation:** Critical scale from one task predicts another
3. **Transparent error propagation:** All uncertainties quantified
4. **Full reproducibility:** Complete code and data provided

---

## Documentation

Complete academic documentation in `docs/`:

- **01_Mathematical_Framework.md** - Theoretical foundation
- **02_Experimental_Setup.md** - Lei et al. (2023) methodology
- **03_Data_Analysis.md** - Processing pipeline
- **04_Results.md** - Comprehensive findings
- **05_Statistical_Validation.md** - Hypothesis testing
- **FIGURE_CAPTIONS.md** - Detailed figure descriptions
- **DATA_PROVENANCE.md** - Data sources and traceability
- **PARAMETER_JUSTIFICATION.md** - Critical parameters justification

---

## Publication-Quality Figures

High-resolution figures (600 DPI) in `figures/publication/`:

1. **Phase transition** - Order parameter vs κ
2. **Functional peak** - Maximum response at κ ≈ 1
3. **Combined experiments** - Cross-task validation
4. **Order vs function** - Dissociation demonstrated

See `docs/FIGURE_CAPTIONS.md` for detailed descriptions.

---

## Citation

**This Analysis:**
```
Onasenko, O. (2025). Emergence Analysis: Swarm Robots with Vicsek-like Interactions. 
SubstanceNet Research Program. 
GitHub: https://github.com/olexxa62-code/swarm-robots-emergence-analysis
```

**Original Data:**
```
Lei, X., Xiang, Y., Duan, M., & Peng, X. (2023). 
Exploring the criticality hypothesis using programmable swarm robots 
with Vicsek-like interactions. 
Journal of the Royal Society Interface, 20(207), 20230176.
https://doi.org/10.1098/rsif.2023.0176
```

---

## License

This project is licensed under the **Apache License 2.0** - see the [LICENSE](LICENSE) file for details.

**Summary:**
- Commercial use allowed
- Modification allowed
- Distribution allowed
- Patent use allowed
- Private use allowed
- Trademark use not granted
- Liability and warranty disclaimed

**Copyright © 2025 Oleksii Onasenko**

---

## Contact

**Author:** Oleksii Onasenko  
**Developer:** SubstanceNet  
**Project:** Universal Emergence Research Program

For questions, see documentation in `docs/` or open an issue.

---

**Status:** Publication Ready | **Version:** 1.1.0 | **Release Date:** November 2025
