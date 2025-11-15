# Data Analysis and Processing Pipeline

**System:** A.2 Swarm Robots  
**Author:** Oleksii Onasenko  
**Developer:** SubstanceNet  
**Theoretical Framework:** The Emergence Parameter κ ≈ 1: An Empirical Signature of Criticality in Physical and Biological Systems

---

## 1. Overview

This document describes the complete data processing pipeline from raw experimental measurements to final κ values and statistical analysis.

---

## 2. Data Loading

### 2.1 Source Files

**Figure 5 Data:**
```
File: robData_aliWeight_OP_ACC_NND.mat
Format: MATLAB v7.3 (HDF5 structure)
Access: h5py library in Python
```

**Figure 8 Data:**
```
File: robData_aliWeight_Desp=300_FCT_OP_Dnn.mat
Format: MATLAB v7.3 (HDF5 structure)  
Access: h5py library in Python
```

### 2.2 Data Structure

**Figure 5 Variables:**
- align_weight: Array of wali values (11 conditions)
- G_OP: Cell array of polarization time series
- G_ACC: Cell array of response accuracy time series
- G_NND: Cell array of nearest neighbor distance matrices (time × robots)

**Figure 8 Variables:**
- align_weight: Array of wali values (10 conditions)
- G_meanOP: Pre-averaged polarization values
- G_meanDNN: Pre-averaged minimum nearest neighbor distances
- G_FCT: First capture time values

---

## 3. Metric Calculation

### 3.1 Polarization (Order Parameter)

**Definition:**
```
ψ(t) = |Σi ri(t)| / N
```

**Procedure (Figure 5):**
1. Load G_OP[k] for condition k
2. Extract time series: ψ(t), t ∈ [1, 1600]
3. Exclude relaxation period: t < 200
4. Compute time average: ψ̄_k = mean(ψ(t)), t ≥ 200

**Procedure (Figure 8):**
1. Load G_meanOP[k] directly (already averaged)
2. No further processing required

**Physical Interpretation:**
- ψ = 0: Disordered state (random orientations)
- ψ = 1: Ordered state (perfect alignment)

### 3.2 Mean Nearest Neighbor Distance

**Definition:**
```
⟨NND⟩ = ⟨min_j≠i |xi(t) - xj(t)|⟩
```

where average is taken over robots i and time t.

**Procedure (Figure 5):**
1. Load G_NND[k]: matrix of shape (time_steps, N_robots)
2. For each time step t: compute NND(t,i) = min_j≠i |xi(t) - xj(t)|
3. Compute mean across robots: ⟨NND⟩(t) = mean_i(NND(t,i))
4. Exclude relaxation: t < 200
5. Compute time average: ⟨NND⟩_k = mean_t(⟨NND⟩(t)), t ≥ 200

**Procedure (Figure 8):**

Figure 8 provides only minimum nearest neighbor distance per timestep (d_nn), not the full distribution.

Correction required:
```
⟨NND⟩ ≈ d_nn / correction_factor
```

**Correction factor determination:**

From Figure 5 data at ordered states (ψ > 0.8), compute:
```
correction_factor = ⟨d_nn / ⟨NND⟩⟩ over ordered conditions
```

Result: correction_factor = 0.741 ± 0.038

Applied to Figure 8:
```
⟨NND⟩_k = G_meanDNN[k] / 0.741
```

**Uncertainty:** ±4% from variability in correction factor.

### 3.3 Group Responsiveness

**Definition (Figure 5 only):**
```
R = ⟨acc(t)⟩_t
```

where acc(t) is response accuracy of uninformed robots:
```
acc(t) = (1/(N-1)) · Σ_{i≠g} ri(t)·e(t)
```

**Procedure:**
1. Load G_ACC[k]: response accuracy time series
2. Exclude relaxation period: t < 200
3. Compute time average: R_k = mean(acc(t)), t ≥ 200

**Physical Interpretation:**
- R = -1: Moving opposite to stimulus
- R = 0: No collective response
- R = +1: Perfect collective alignment with stimulus

### 3.4 First Capture Time

**Definition (Figure 8 only):**
```
T_fc = time until predator captures first robot
```

**Procedure:**
1. Load G_FCT[k] directly (already computed)
2. Convert from steps to seconds: T_fc (seconds) = G_FCT[k] × 0.2

**Physical Interpretation:** Longer T_fc indicates better collective evasion capability.

---

## 4. Emergence Parameter Calculation

### 4.1 Formula Application

For all experimental conditions:
```
κ = (N/Nc) · ψ · (⟨NND⟩/Λc)
```

With N = Nc = 30:
```
κ = ψ · (⟨NND⟩/202.7)
```

### 4.2 Critical Length Scale

**Λc = 202.7 mm** determined from Figure 5 at maximum response:

**Determination procedure:**
1. Compute R for all wali values
2. Identify wali* = argmax_wali R(wali)
3. Result: wali* = 20, R_max = 0.776
4. Define: Λc = ⟨NND⟩(wali = 20) = 202.7 mm

**Validation:** Apply Λc to Figure 8 data and verify κ ≈ 1 at maximum T_fc.

### 4.3 Complete Dataset

Output format (CSV):
```
experiment, wali, N, ψ, ⟨NND⟩, d_nn, R, T_fc, κ, regime
```

Total: 21 rows (11 from Fig5, 10 from Fig8)

---

## 5. Regime Classification

### 5.1 Criteria

Based on κ value:

**Subcritical:** κ < 0.8
- Characteristics: Low ψ, disordered motion, minimal function

**Critical:** 0.8 ≤ κ ≤ 1.2
- Characteristics: High ψ, ordered motion, optimal function

**Supercritical:** κ > 1.2
- Characteristics: Maximal ψ, highly ordered, declining function

### 5.2 Classification Results

**Figure 5:**
- Subcritical: wali ∈ {10, 17} (2 conditions)
- Critical: wali ∈ {20, 30, 40, 50, 65, 85, 100, 120, 150} (9 conditions)

**Figure 8:**
- Subcritical: wali ∈ {5, 15} (2 conditions)  
- Critical: wali ∈ {20, 25, 30, 40, 50, 70, 100, 150} (8 conditions)

---

## 6. Critical Point Identification

### 6.1 Figure 5 (Response Task)

**Procedure:**
1. Compute R for all conditions
2. Identify maximum: idx_max = argmax R
3. Extract values at maximum:
   - wali_crit = wali[idx_max] = 20
   - κ_crit = κ[idx_max] = 0.991
   - R_max = R[idx_max] = 0.776

**Interpretation:** System exhibits optimal collective response at κ ≈ 1.

### 6.2 Figure 8 (Evasion Task)

**Procedure:**
1. Compute T_fc for all conditions
2. Identify maximum: idx_max = argmax T_fc
3. Extract values at maximum:
   - wali_crit = wali[idx_max] = 25
   - κ_crit = κ[idx_max] = 0.960
   - T_fc_max = T_fc[idx_max] = 326.8 s

**Interpretation:** System exhibits optimal collective evasion at κ ≈ 1.

### 6.3 Combined Analysis

**Critical κ values:**
- Figure 5: κ = 0.991
- Figure 8: κ = 0.960
- Mean: κ = 0.976 ± 0.022

**Consistency:** Both independent tasks yield κ ≈ 1 at functional optimum.

---

## 7. Quality Control

### 7.1 Data Validation Checks

**Physical Constraints:**
- ψ ∈ [0,1]: All values satisfy
- R ∈ [-1,1]: All values satisfy
- ⟨NND⟩ > 80 mm: All values satisfy (collision avoidance)
- κ > 0: All values satisfy

**Consistency Checks:**
- Monotonic increase of ψ with wali for wali > 17: Confirmed
- Peak R occurs within ordered regime (ψ > 0.9): Confirmed
- ⟨NND⟩ variation within ±10% for ordered states: Confirmed

### 7.2 Error Propagation

**Source of uncertainty:**

For κ = ψ · (⟨NND⟩/202.7):

1. ψ measurement error: Negligible (≪1%)
2. ⟨NND⟩ measurement error (Fig5): ~1% (motion capture precision)
3. ⟨NND⟩ estimation error (Fig8): ~4% (correction factor uncertainty)
4. Λc determination error: ~1% (from ⟨NND⟩ at wali=20)

**Combined uncertainty:**
- Figure 5: Δκ/κ ≈ 2%
- Figure 8: Δκ/κ ≈ 5%

### 7.3 Reproducibility

**Deterministic calculations:** All metric computations are deterministic given input data.

**Code availability:** Complete processing pipeline provided in Python.

**Data availability:** Raw data accessible from publication supplementary materials.

---

## 8. Output Data Products

### 8.1 Primary Dataset

**File:** swarm_robots_complete_data.csv

**Format:** CSV with columns:
- experiment: 'fig5' or 'fig8'
- wali: Alignment weight
- N: Number of robots (30)
- psi: Polarization ψ
- NND_mean: Mean nearest neighbor distance ⟨NND⟩ (mm)
- NND_min: Minimum nearest neighbor distance d_nn (mm)
- R: Group responsiveness (Fig5 only)
- T_fc: First capture time (Fig8 only)
- kappa_correct: Emergence parameter κ
- regime: Classification (subcritical/critical/supercritical)

**Rows:** 21 (11 Fig5 + 10 Fig8)

### 8.2 Summary Statistics

**File:** results/summary_statistics.txt

**Content:**
- Critical κ values for both experiments
- Mean and standard deviation
- Regime-specific averages

### 8.3 Figures

**Generated visualizations:**
1. κ vs ψ (phase transition)
2. κ vs R (functional peak)
3. Combined phase diagram
4. wali comparison plots

---

## 9. Computational Workflow

### 9.1 Software Requirements

**Language:** Python 3.8+

**Required libraries:**
- numpy: Numerical computations
- pandas: Data manipulation
- h5py: MATLAB file reading
- matplotlib: Visualization
- scipy: Statistical tests

### 9.2 Execution Order

**Step 1:** Data loading (from .mat files)  
**Step 2:** Metric calculation (ψ, R, ⟨NND⟩, T_fc)  
**Step 3:** κ calculation (using Λc = 202.7 mm)  
**Step 4:** Critical point identification  
**Step 5:** Statistical analysis  
**Step 6:** Visualization  

**Total runtime:** < 1 minute on standard laptop

---

## 10. Summary

The data analysis pipeline:

1. Processes raw experimental data from Lei et al. (2023)
2. Computes order parameter (ψ), functional metrics (R, T_fc), and spatial correlation (⟨NND⟩)
3. Calculates emergence parameter κ using empirically determined Λc
4. Identifies critical points where κ ≈ 1 coincides with optimal function
5. Validates consistency across two independent experimental tasks

**Key result:** κ = 0.976 ± 0.022 at maximum collective function, confirming the criticality hypothesis.

---

**Document Version:** 1.0  
**Last Updated:** November 15, 2025  
**Author:** Oleksii Onasenko  
**Developer:** SubstanceNet
