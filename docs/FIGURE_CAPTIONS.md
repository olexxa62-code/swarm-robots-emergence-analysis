# Figure Captions

**System:** A.2 Swarm Robots  
**Author:** Oleksii Onasenko  
**Developer:** SubstanceNet  
**Resolution:** 600 DPI (publication quality)

---

## Figure 1: Phase Transition - Order Parameter vs Emergence Parameter

**File:** `publication/fig1_phase_transition_kappa_vs_psi.png`

**Caption:**

Phase transition in swarm robot collective motion. Polarization ψ (order parameter) exhibits sharp transition as emergence parameter κ crosses unity. Blue circles with connecting line represent experimental data points from Lei et al. (2023, Figure 5) with varying alignment weight w_ali ∈ [10, 150]. Orange dashed vertical line marks critical point at κ = 1, with shaded region (0.8 ≤ κ ≤ 1.2) indicating critical regime. Transition occurs over narrow range Δκ ≈ 0.2, demonstrating abrupt shift from disordered motion (ψ < 0.3, κ < 0.8) to ordered collective motion (ψ > 0.98, κ > 0.8). Data: N = 30 robots, η_m = 0 (no noise), α_soc = 1.0 (full social attention).

**Key Observations:**
- Subcritical regime (κ < 0.8): ψ ≈ 0.15-0.20 (random orientations)
- Critical transition: κ ≈ 0.68 → 0.99 yields Δψ = 0.78
- Supercritical regime (κ > 1.0): ψ saturates at 0.99 (perfect alignment)

**Statistical Notes:**
- Transition sharpness: Δκ/κ_c ≈ 20%
- Sample size: n = 11 conditions
- Measurement precision: δψ < 0.01

---

## Figure 2: Functional Optimum - Group Responsiveness vs Emergence Parameter

**File:** `publication/fig2_functional_peak_kappa_vs_R.png`

**Caption:**

Collective response accuracy maximized at critical point. Group responsiveness R (fraction of accurate collective response to periodic directional stimuli) plotted against emergence parameter κ. Blue circles show experimental measurements for 11 alignment conditions. Orange dashed line marks theoretical critical point κ = 1, with shaded critical region (0.8 ≤ κ ≤ 1.2). Gold star with black edge indicates maximum responsiveness: R = 0.776 at κ = 0.991, occurring at alignment weight w_ali = 20. Yellow annotation box highlights peak location. Functional response declines for both κ < 1 (insufficient order) and κ > 1.2 (excessive rigidity). This non-monotonic relationship demonstrates that optimal collective function requires critical balance captured by κ ≈ 1, not merely maximal order.

**Key Results:**
- Maximum: R = 0.776 at κ = 0.991 (deviation from κ = 1: 0.9%)
- Subcritical: R ≈ 0.03 for κ < 0.8 (29-fold lower than peak)
- Post-critical decline: R decreases to 0.66 at κ = 7.4

**Physical Interpretation:**
- Low κ: Insufficient alignment prevents information propagation
- κ ≈ 1: Optimal balance of coherence and flexibility
- High κ: Over-alignment creates inertia, slowing collective reorientation

---

## Figure 3: Cross-Task Validation - Two Independent Experiments

**File:** `publication/fig3_combined_both_experiments.png`

**Caption:**

Criticality hypothesis validated across two independent collective tasks. (a) Collective response task (Figure 5): Group responsiveness R peaks at κ = 0.991 (blue circles). (b) Collective evasion task (Figure 8): Survival time T_fc maximized at κ = 0.960 (purple squares). Both panels show orange dashed vertical line at κ = 1 with shaded critical region (0.8 ≤ κ ≤ 1.2). Gold stars mark functional optima. Despite different tasks, different optimal control parameters (w_ali = 20 vs 25), and different order parameter values (ψ = 0.991 vs 0.897), both experiments yield maximum function at κ ≈ 1, demonstrating universality of critical length scale Λ_c = 202.7 mm determined from panel (a) and successfully applied to independent experiment in panel (b).

**Panel (a) - Response Task:**
- Stimulus: Periodic 120° directional changes every 200 steps
- Metric: R = response accuracy of 29 uninformed robots
- Peak: R = 0.776 at κ = 0.991

**Panel (b) - Evasion Task:**
- Stimulus: Faster-moving predator (v_p = 1.6 × v_prey)
- Metric: T_fc = time until first robot captured
- Peak: T_fc = 326.8 s at κ = 0.960

**Cross-Task Consistency:**
- Mean κ at optimum: 0.976 ± 0.022
- Relative deviation from κ = 1: 2.4%
- Single Λ_c applies to both tasks

---

## Figure 4: Order-Function Dissociation

**File:** `publication/fig4_order_vs_function.png`

**Caption:**

High polarization does not guarantee high functional response. Scatter plot shows group responsiveness R versus polarization ψ for 11 experimental conditions, color-coded by regime: red (subcritical, κ < 0.8), green (critical, 0.8 ≤ κ ≤ 1.2), blue (supercritical, κ > 1.2). Gold star marks critical point where κ ≈ 1. Key observation: multiple conditions achieve ψ ≈ 0.99 (near-perfect alignment) but exhibit widely varying responsiveness R ∈ [0.66, 0.78]. This dissociation demonstrates that maximum order (ψ → 1) is necessary but not sufficient for maximum function. Optimal performance requires specific balance between polarization and spatial correlation captured by κ = ψ × (⟨NND⟩/Λ_c) ≈ 1.

**Regime Characteristics:**

**Subcritical (red, κ < 0.8):**
- Low polarization: ψ < 0.3
- Minimal function: R ≈ 0.03
- Mechanism: Random motion prevents coordination

**Critical (green, 0.8 ≤ κ ≤ 1.2):**
- High polarization: ψ > 0.98
- Maximum function: R = 0.78 at κ = 0.99
- Mechanism: Coherence with flexibility

**Supercritical (blue, κ > 1.2):**
- Maximal polarization: ψ ≈ 0.99
- Declining function: R decreases to 0.66
- Mechanism: Excessive coupling reduces adaptability

**Statistical Correlation:**
- ψ vs R (all points): r = 0.994 (very strong)
- ψ vs R (ordered states only, ψ > 0.98): r = -0.73 (negative!)
- Interpretation: Within ordered regime, higher order correlates with lower function

---

## Supplementary Figure: Combined Analysis Overview

**File:** `kappa_both_experiments.png`

**Caption:**

Comprehensive comparison of emergence parameter κ across both experimental tasks. Left panel: κ versus alignment weight w_ali for collective response task (Figure 5, blue circles). Right panel: κ versus w_ali for collective evasion task (Figure 8, green circles). Orange dashed horizontal line marks critical value κ = 1 in both panels. This figure demonstrates that different tasks achieve criticality at different control parameter values (w_ali = 20 vs 25) through compensatory adjustments in polarization ψ and spatial correlation ⟨NND⟩, supporting robustness of κ framework.

---

## Technical Specifications

**All Figures:**
- Resolution: 600 DPI
- Format: PNG (lossless)
- Color space: RGB
- Font: Serif (publication standard)
- Grid: Light gray, dotted, alpha = 0.3

**Figure Dimensions:**
- Single panels (Fig 1, 2, 4): 8" × 6"
- Double panel (Fig 3): 12" × 5"

**Accessibility:**
- All text readable at journal column width (3.5")
- Color-blind friendly palette (tested)
- High contrast for black-and-white printing

---

## Data Sources

**Figure 1:** Lei et al. (2023), Figure 5, collective response experiment  
**Figure 2:** Lei et al. (2023), Figure 5, collective response experiment  
**Figure 3a:** Lei et al. (2023), Figure 5, collective response experiment  
**Figure 3b:** Lei et al. (2023), Figure 8, collective evasion experiment  
**Figure 4:** Lei et al. (2023), Figure 5, collective response experiment

**Original Publication:**  
Lei, X., Xiang, Y., Duan, M., & Peng, X. (2023). Exploring the criticality hypothesis using programmable swarm robots with Vicsek-like interactions. *Journal of the Royal Society Interface*, 20(207), 20230176.

**Analysis:**  
Onasenko, O. (2025). Emergence Analysis: Swarm Robots with Vicsek-like Interactions. SubstanceNet Research Program.

---

## Usage in Publications

These figures are designed for direct inclusion in academic manuscripts. Recommended usage:

**Main Text:**
- Figure 2 (functional peak) - PRIMARY RESULT
- Figure 3 (cross-task validation) - VALIDATION

**Supplementary:**
- Figure 1 (phase transition) - background
- Figure 4 (order-function dissociation) - detailed analysis

**Presentations:**
- Figure 2 with large font for talks
- Figure 3 for comprehensive overview

---

**Document Version:** 1.0  
**Last Updated:** November 15, 2025  
**Author:** Oleksii Onasenko  
**Developer:** SubstanceNet
