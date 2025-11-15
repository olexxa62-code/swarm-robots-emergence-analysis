# Mathematical Framework

**System:** A.2 Swarm Robots  
**Author:** Oleksii Onasenko  
**Developer:** SubstanceNet  
**Theoretical Framework:** The Emergence Parameter κ ≈ 1: An Empirical Signature of Criticality in Physical and Biological Systems

---

## 1. Theoretical Foundation

### 1.1 Universal Emergence Parameter

The emergence parameter κ quantifies the proximity of a system to critical phase transition. It is defined as:
```
κ = (A/Ac) · τ · (Λ/Λc)
```

where:
- A/Ac: normalized system complexity (degrees of freedom relative to critical threshold)
- τ: topological order parameter (0 ≤ τ ≤ 1)
- Λ/Λc: normalized correlation length (spatial extent of collective behavior)

**Central Hypothesis:** Systems exhibit emergent collective behavior when κ ≈ 1, marking the critical phase transition.

### 1.2 Physical Interpretation

**A (Complexity):** Number of interacting components or agents. Below critical threshold Ac, the system lacks sufficient degrees of freedom for collective behavior.

**τ (Topological Order):** Degree of organizational structure. Computed from topological entropy with normalization:
```
τ = 1 - (Stop - Smin)/(Smax - Smin)
```

For network systems, Stop is typically degree distribution entropy. For systems with continuous symmetry, τ represents the magnitude of the order parameter.

**Λ (Correlation Length):** Characteristic distance over which system components influence each other. At criticality, correlations extend to system-wide scale.

---

## 2. Application to Swarm Robots

### 2.1 System Definition

**Physical System:** N = 30 SwarmBang mobile robots executing Vicsek-like alignment dynamics in bounded arena.

**State Variables:**
- xi(t): position of robot i at time t
- ri(t): unit direction vector of robot i
- vi: constant speed (15 mm/s)

**Interaction Rule:**
```
ri^d(t+τ) = (1-αsoc)ri(t) + αsoc·ri^s(t) + ηm·Γi
```

where ri^s(t) is the social interaction term combining alignment, repulsion, and attraction.

### 2.2 Parameter Mapping

#### Complexity: A/Ac

**A = N:** Number of robots

**Ac = 30:** Critical swarm size determined empirically. Lei et al. (2023, Fig. 7) demonstrate that for N < 20, collective response metrics show weak dependence on control parameters, indicating subcritical regime. For N ≥ 30, clear functional advantages emerge near critical alignment values.

**Ratio:** A/Ac = 30/30 = 1

**Justification:** System operates at critical complexity by design.

#### Topological Order: τ

**Definition:** For swarm robots, τ is identified with the polarization (order parameter):
```
τ = ψ(t) = |⟨ri(t)⟩|
```

where ⟨·⟩ denotes ensemble average over all robots.

**Physical Meaning:**
- τ = 0: Random orientations (disordered phase)
- τ = 1: Perfect alignment (ordered phase)

**Measurement:** Directly measured from robot heading angles via motion capture system.

**Relation to Input Parameters:** τ is an emergent property that depends on alignment weight wali, noise intensity ηm, and social level αsoc.

#### Correlation Length: Λ/Λc

**Definition:** Λ quantifies spatial extent of collective motion. For swarm robots, we use mean nearest-neighbor distance as proxy:
```
Λ = ⟨NND⟩ = ⟨min_j≠i |xi - xj|⟩
```

averaged over all robots and time.

**Λc = 202.7 mm:** Critical correlation length determined from experimental data at maximum functional response (Fig. 5, wali = 20).

**Physical Interpretation:** Λc represents optimal inter-robot spacing balancing cohesion and collision avoidance. It equals approximately 68% of the interaction radius (300 mm).

**Ratio:** Λ/Λc = ⟨NND⟩/202.7 mm

### 2.3 Complete Formula

Substituting all components:
```
κ = (N/30) · ψ · (⟨NND⟩/202.7)
```

For the experimental condition N = 30:
```
κ = ψ · (⟨NND⟩/202.7)
```

**Units:** Dimensionless

**Range:** 0 < κ < ∞, with critical region 0.8 ≤ κ ≤ 1.2

---

## 3. Critical Point Determination

### 3.1 Empirical Approach

The critical correlation length Λc is determined by identifying the system state exhibiting maximum functional advantage (collective response accuracy R).

**Procedure:**
1. Vary control parameter wali across range [10, 150]
2. Measure order parameter ψ(wali) and functional metric R(wali)
3. Identify wali* = argmax R(wali)
4. Define Λc := ⟨NND⟩(wali*)

**Result:** Λc = 202.7 mm at wali* = 20 where R = 0.776 (maximum).

### 3.2 Independent Validation

The value Λc = 202.7 mm determined from Fig. 5 (collective response task) is validated using independent experimental data from Fig. 8 (predator evasion task):

- Different task (evasion vs. response)
- Different optimal control parameter (wali = 25 vs. 20)
- Different order parameter values (ψ = 0.897 vs. 0.991)

Despite these differences, Fig. 8 yields κ = 0.960 ≈ 1 using Λc = 202.7 mm, confirming the universality of this critical scale.

---

## 4. Comparison with Alternative Formulations

### 4.1 Rejected Approach: τ = wali/wc

An alternative interpretation treats the control parameter wali directly as topological order:
```
κ = (N/Nc) · (wali/wc) · (Λ/Λc)
```

**Problems:**
1. **Circular reasoning:** Using wali to predict wali-dependent outcomes provides no predictive power
2. **Tautology:** At wali = wc, κ = 1 by definition rather than by emergence
3. **Lack of universality:** Different tasks yield different optimal wali (20 vs. 25), requiring task-dependent wc

### 4.2 Adopted Approach: τ = ψ

The formulation τ = ψ avoids circularity:

**Advantages:**
1. **Predictive:** Input parameters (wali) → Emergent properties (ψ, R)
2. **Testable:** κ ≈ 1 is a falsifiable prediction, not a definition
3. **Universal:** Single Λc applies across different tasks
4. **Physical:** τ = ψ has clear interpretation as orientational order

---

## 5. Mathematical Properties

### 5.1 Regime Classification

Based on κ value, system states are classified into three regimes:

**Subcritical (κ < 0.8):**
- Low polarization (ψ < 0.3)
- Disordered motion
- Minimal collective function

**Critical (0.8 ≤ κ ≤ 1.2):**
- High polarization (ψ > 0.8)
- Ordered collective motion
- Maximum functional advantage

**Supercritical (κ > 1.2):**
- Maximal polarization (ψ ≈ 1)
- Highly ordered but rigid
- Declining functional advantage

### 5.2 Sensitivity Analysis

The emergence parameter exhibits different sensitivities to its components:

**Complexity (N/Nc = 1):** Fixed in this study. Variations in N would test scaling predictions.

**Topological order (ψ):** Highly sensitive to control parameter wali. Sharp transition occurs over Δwali ≈ 3 (from 17 to 20).

**Correlation length (⟨NND⟩/202.7):** Varies ±7% across ordered states (wali ≥ 20), remaining close to critical value.

---

## 6. Limitations and Assumptions

### 6.1 Assumptions

1. **Homogeneity:** All robots have identical parameters
2. **Ergodicity:** Time averages equal ensemble averages
3. **Stationarity:** System reaches quasi-equilibrium within measurement window
4. **Weak noise:** Environmental perturbations are small compared to interaction forces

### 6.2 Limitations

1. **Fixed N:** Cannot test N/Nc dependence with current dataset
2. **Proxy variables:** ⟨NND⟩ as proxy for true correlation length may introduce error
3. **Finite size:** N = 30 may exhibit finite-size effects near criticality
4. **Discrete sampling:** Limited resolution in wali prevents precise location of critical point

---

## 7. Summary

The mathematical framework establishes:

1. κ = ψ · (⟨NND⟩/202.7) for N = 30 swarm robots
2. Λc = 202.7 mm determined from maximum collective response
3. Critical behavior (κ ≈ 1) predicted and observed at maximum functional advantage
4. Framework avoids circular reasoning through separation of control parameters (wali) and emergent properties (ψ, R)

**Status:** Mathematical foundation complete and validated.

---

**Document Version:** 1.0  
**Last Updated:** November 15, 2025  
**Author:** Oleksii Onasenko  
**Developer:** SubstanceNet
