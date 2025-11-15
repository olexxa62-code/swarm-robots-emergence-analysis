# Experimental Setup and Data Source

**System:** A.2 Swarm Robots  
**Author:** Oleksii Onasenko  
**Developer:** SubstanceNet  
**Theoretical Framework:** The Emergence Parameter κ ≈ 1: An Empirical Signature of Criticality in Physical and Biological Systems

---

## 1. Data Provenance

### 1.1 Primary Source

**Publication:**  
Lei, X., Xiang, Y., Duan, M., & Peng, X. (2023). Exploring the criticality hypothesis using programmable swarm robots with Vicsek-like interactions. Journal of the Royal Society Interface, 20(207), 20230176.

**DOI:** https://doi.org/10.1098/rsif.2023.0176

**Supplementary Materials:**  
Available at Royal Society Interface website, including:
- Raw experimental data (MATLAB .mat format)
- Video recordings of robot experiments
- Complete parameter specifications

### 1.2 Experimental Platform

**Robot Hardware:** SwarmBang mobile robots
- Dimensions: 80 mm × 80 mm × 60 mm
- Drive system: Two-wheeled differential drive
- Speed: Constant v0 = 15 mm/s
- Maximum angular velocity: 0.4 rad/s

**Arena:**
- Size: 6.0 m × 6.0 m
- Surface: Flat, obstacle-free
- Boundaries: Enclosed walls

**Tracking System:**
- Motion capture: NOKOV system with 16 cameras
- Precision: Sub-millimeter position accuracy
- Frequency: Real-time tracking at 100 Hz
- Additional: CCD camera for video recording

---

## 2. Behavioral Model

### 2.1 Control Architecture

**Update Cycle:** Discrete time steps with interval τ = 0.2 seconds

**Decision Process:**
1. Sense: Robot i detects positions and headings of neighbors within radius r0 = 300 mm
2. Compute: Calculate desired direction ri^d(t+τ) based on social interactions
3. Act: Adjust angular velocity to align with desired direction

**Communication:** Centralized broadcasting of position data, but decision-making is fully decentralized.

### 2.2 Interaction Rules

**Social Interaction Term:**
```
ri^s(t) = wali · Σj exp(-dij/Dali) · rj(t) + Σj βij(t) · (xj - xi)/dij
```

where:
- wali: alignment weight (control parameter)
- Dali: alignment scale (50 mm, fixed)
- βij(t): distance-dependent repulsion-attraction function

**Repulsion-Attraction Function:**
```
βij(t) = -wrep·exp(-dij/Drep) + watt·exp(-dij/Datt)
```

with wrep = 20, Drep = 100 mm (short-range repulsion) and watt = 1, Datt = 400 mm (long-range attraction).

**Desired Direction:**
```
ri^d(t+τ) = (1-αsoc)·ri(t) + αsoc·ri^s(t)/|ri^s(t)| + ηm·Γi
```

where:
- αsoc: social level (attention to neighbors), αsoc ∈ [0,1]
- ηm: motion noise intensity, ηm ∈ [0,1]
- Γi: uniform random noise vector

---

## 3. Experimental Conditions

### 3.1 Fixed Parameters

**Population:**
- Number of robots: N = 30
- Initial configuration: Random positions in circular region, random orientations

**Behavioral:**
- Social level: αsoc = 1.0 (full attention to neighbors)
- Motion noise: ηm = 0 (noise-free condition)
- Action cycle: τ = 0.2 s

**Physical:**
- Speed: v0 = 15 mm/s (constant)
- Alignment scale: Dali = 50 mm
- Repulsion: wrep = 20, Drep = 100 mm
- Attraction: watt = 1, Datt = 400 mm

### 3.2 Variable Parameters

**Primary Control Parameter: Alignment Weight wali**

Experimental values:
- Figure 5 (Response): [10, 17, 20, 30, 40, 50, 65, 85, 100, 120, 150]
- Figure 8 (Evasion): [5, 15, 20, 25, 30, 40, 50, 70, 100, 150]

Total: 21 distinct experimental conditions (11 from Fig. 5, 10 from Fig. 8)

---

## 4. Experimental Protocols

### 4.1 Figure 5: Collective Response to Stimuli

**Task:** Robots collectively respond to periodic directional stimuli

**Setup:**
- One robot designated as "informed" (can detect stimulus)
- Remaining 29 robots are "uninformed" (respond via social coupling)
- Stimulus: Light source alternating between two positions every 200 time steps (40 s)
- Required action: 120-degree collective turn

**Duration:** 1600 time steps (320 seconds) per trial

**Measured Quantities:**
- G_OP: Polarization time series, ψ(t)
- G_ACC: Response accuracy time series, acc(t)
- G_NND: Nearest neighbor distance matrix, NND(t,i)

**Response Accuracy:**
```
acc(t) = (1/(N-1)) · Σi≠g ri(t)·e(t)
```

where g is the informed robot and e(t) is the stimulus direction.

### 4.2 Figure 8: Collective Evasion from Predator

**Task:** Robots collectively evade a faster-moving "predator"

**Setup:**
- Predator robot: Speed vp = 24 mm/s (1.6× faster than prey)
- Predator behavior: Chase nearest robot
- One robot has extended detection range: Desp = 1000 mm (informed)
- Other robots: Desp = 300 mm (standard) or 30 mm (minimal)
- Escape rule: Move opposite to predator when detected

**Duration:** Variable (until first capture or 2000 steps maximum)

**Measured Quantities:**
- G_OP: Polarization time series, ψ(t)
- G_NND: Nearest neighbor distance (minimum per timestep)
- T_fc: First capture time (survival duration)

**Performance Metric:** Longer T_fc indicates better collective evasion.

---

## 5. Data Extraction and Processing

### 5.1 File Formats

**Figure 5 Data:**
- File: robData_aliWeight_OP_ACC_NND.mat
- Format: MATLAB v7.3 (HDF5)
- Size: 3.8 MB
- Structure: Cell arrays with time series for each wali condition

**Figure 8 Data:**
- File: robData_aliWeight_Desp=300_FCT_OP_Dnn.mat
- Format: MATLAB v7.3 (HDF5)
- Size: 7.6 KB
- Structure: Pre-aggregated statistics per condition

### 5.2 Metric Computation

**Polarization ψ:**
```
ψ(t) = |Σi ri(t)| / N
```

Time-averaged value computed excluding initial relaxation period (first 200 steps).

**Mean Nearest Neighbor Distance:**
```
⟨NND⟩ = ⟨min_j≠i |xi(t) - xj(t)|⟩_{t,i}
```

Averaged over robots and time (excluding relaxation).

**Group Responsiveness R:**
```
R = ⟨acc(t)⟩_t
```

Time-averaged response accuracy for uninformed robots only.

**First Capture Time T_fc:**
```
T_fc = min{t : dg,p(t) < contact_threshold}
```

where dg,p is the distance between predator and nearest prey robot.

### 5.3 Data Quality

**Figure 5:**
- Complete time series available (1600 steps)
- High temporal resolution
- Full spatial information (all robot positions)

**Figure 8:**
- Only summary statistics provided (mean values)
- Minimum nearest-neighbor distance (not mean)
- Requires correction for ⟨NND⟩ estimation

**Correction Factor:** 
From Figure 5 analysis, d_nn / ⟨NND⟩ = 0.741 ± 0.038 for ordered states (ψ > 0.8).

Applied to Figure 8: ⟨NND⟩ ≈ d_nn / 0.741

---

## 6. Experimental Limitations

### 6.1 Sample Size

**Number of conditions:** 11 (Fig. 5) + 10 (Fig. 8) = 21 total

**Replicates:** Not specified in dataset. Assuming single trial per condition or pre-averaged results.

**Statistical power:** Limited for hypothesis testing (n=2 critical points identified).

### 6.2 Parameter Space

**Fixed N:** Cannot test scaling with swarm size.

**Fixed ηm, αsoc:** Only one noise/social level condition analyzed in detail.

**Discrete wali:** Control parameter sampled discretely, limiting precision of critical point localization.

### 6.3 Measurement Constraints

**Figure 8 limitation:** Only minimum NND available, not full distribution. Estimation of ⟨NND⟩ introduces ~4% uncertainty based on correction factor variability.

**Finite duration:** Experiments limited to 1600 steps. Transient effects may not fully decay.

**Boundary effects:** Arena walls may influence spatial distribution near edges.

---

## 7. Data Validation

### 7.1 Cross-checks with Publication

**Figure 5 (wali = 20):**
- Published: ψ ≈ 0.99, R ≈ 0.78
- Our extraction: ψ = 0.991, R = 0.776
- Agreement: Excellent

**Figure 8 (wali = 25):**
- Published: T_fc ≈ 330 s
- Our extraction: T_fc = 326.8 s  
- Agreement: Within 1%

### 7.2 Physical Constraints

All extracted values satisfy physical constraints:
- 0 ≤ ψ ≤ 1 (polarization bounded)
- -1 ≤ acc ≤ 1 (response accuracy bounded)
- d_nn > 80 mm (minimum spacing to avoid collisions)
- ⟨NND⟩ < 3000 mm (arena dimension)

### 7.3 Consistency Checks

**Phase transition location:** Multiple metrics (ψ, R, T_fc) show consistent critical region at wali ∈ [20, 30].

**Scaling relations:** ψ increases monotonically with wali for wali > 17, as expected for order parameter.

---

## 8. Reproducibility

### 8.1 Data Availability

**Original data:** Available from Royal Society Interface supplementary materials (DOI: 10.1098/rsif.2023.0176)

**Processed data:** Included in this repository as swarm_robots_complete_data.csv

**Processing code:** Python scripts provided for full data extraction and analysis pipeline

### 8.2 Computational Requirements

**Software:**
- Python 3.8+
- Libraries: numpy, pandas, h5py, matplotlib, scipy

**Hardware:** Minimal (standard laptop sufficient)

**Runtime:** Complete analysis executes in under 1 minute

---

## 9. Summary

The experimental setup provides:

1. High-quality data from physical robot experiments (not simulation)
2. Two independent tasks (response and evasion) for validation
3. Systematic variation of control parameter (wali) across wide range
4. Direct measurement of order parameter (ψ) and functional metrics (R, T_fc)
5. Sufficient precision to test κ ≈ 1 hypothesis

**Limitations:** Sample size limited, some experimental conditions not varied, Figure 8 data requires correction for full analysis.

---

**Document Version:** 1.0  
**Last Updated:** November 15, 2025  
**Author:** Oleksii Onasenko  
**Developer:** SubstanceNet
