#!/usr/bin/env python3
"""
Statistical validation for Swarm Robots κ analysis
Tests hypothesis: κ ≈ 1 at criticality

System Classification: A.2 swarm_robots_kappa_analysis
Author: Oleksii Onasenko
Developer: SubstanceNet
Theoretical Framework: The Emergence Parameter κ ≈ 1: An Empirical Signature of Criticality in Physical and Biological Systems
"""

import pandas as pd
import numpy as np
from scipy import stats
from pathlib import Path

print("="*80)
print("STATISTICAL VALIDATION: κ ≈ 1 HYPOTHESIS")
print("="*80)

# Load data
df = pd.read_csv('data/swarm_robots_complete_data.csv')
fig5 = df[df['experiment'] == 'fig5'].copy()
fig8 = df[df['experiment'] == 'fig8'].copy()

# Get critical points
fig5_crit_idx = fig5['R'].idxmax()
fig8_crit_idx = fig8['T_fc'].idxmax()

kappa_critical = [
    fig5.loc[fig5_crit_idx, 'kappa_correct'],
    fig8.loc[fig8_crit_idx, 'kappa_correct']
]

print(f"\n CRITICAL κ VALUES")
print("-"*80)
print(f"Fig5 (max R):    κ = {kappa_critical[0]:.3f}")
print(f"Fig8 (max T_fc): κ = {kappa_critical[1]:.3f}")
print(f"Mean:            κ = {np.mean(kappa_critical):.3f}")
print(f"Std:             σ = {np.std(kappa_critical, ddof=1):.3f}")

# Test 1: One-sample t-test (H0: κ = 1)
print(f"\n" + "="*80)
print("TEST 1: One-Sample t-test")
print("-"*80)
print("H0: κ = 1.0 at criticality")

t_stat, p_value = stats.ttest_1samp(kappa_critical, 1.0)

print(f"n = {len(kappa_critical)}")
print(f"t-statistic = {t_stat:.3f}")
print(f"p-value = {p_value:.4f}")

if p_value > 0.05:
    print(f" Cannot reject H0 (p > 0.05)")
    print(f" κ not significantly different from 1.0")
else:
    print(f" Reject H0 (p < 0.05)")
    print(f" κ significantly differs from 1.0")

# Test 2: 95% Confidence Interval
print(f"\n" + "="*80)
print("TEST 2: 95% Confidence Interval")
print("-"*80)

mean_kappa = np.mean(kappa_critical)
sem = stats.sem(kappa_critical)
ci = stats.t.interval(0.95, len(kappa_critical)-1, loc=mean_kappa, scale=sem)

print(f"Mean κ = {mean_kappa:.3f}")
print(f"SEM = {sem:.3f}")
print(f"95% CI: [{ci[0]:.3f}, {ci[1]:.3f}]")

if ci[0] <= 1.0 <= ci[1]:
    print(f" CI contains κ = 1.0")
    print(f" Consistent with hypothesis")
else:
    print(f"⚠  CI does not contain κ = 1.0")

# Test 3: Individual deviations
print(f"\n" + "="*80)
print("TEST 3: Individual Deviations from κ = 1")
print("-"*80)

for i, (exp, kappa) in enumerate([('Fig5', kappa_critical[0]), ('Fig8', kappa_critical[1])]):
    deviation = abs(kappa - 1.0)
    percent = deviation * 100
    print(f"{exp}: |κ - 1| = {deviation:.3f} ({percent:.1f}%)")

    print(f"⚠  Difference > 10%")

# Save report
report = []
report.append("="*80)
report.append("STATISTICAL VALIDATION REPORT: Swarm Robots κ Analysis")
report.append("="*80)
report.append("")
report.append("HYPOTHESIS: κ ≈ 1 at critical phase transition")
report.append("")
report.append("DATA:")
report.append(f"  Fig5 (response):  κ = {kappa_critical[0]:.3f}")
report.append(f"  Fig8 (evasion):   κ = {kappa_critical[1]:.3f}")
report.append(f"  Mean:             κ = {mean_kappa:.3f} ± {np.std(kappa_critical, ddof=1):.3f}")
report.append("")
report.append("RESULTS:")
report.append(f"  t-test (H0: κ=1): t={t_stat:.3f}, p={p_value:.4f}")
report.append(f"  95% CI: [{ci[0]:.3f}, {ci[1]:.3f}]")
report.append(f"  Contains κ=1: {'YES' if ci[0] <= 1.0 <= ci[1] else 'NO'}")
report.append("")
report.append("CONCLUSION:")
if p_value > 0.05 and ci[0] <= 1.0 <= ci[1]:
    report.append("   κ ≈ 1 hypothesis CONFIRMED")
    report.append("   Both statistical tests support κ = 1 at criticality")
else:
    report.append("  ⚠  Mixed results - requires further investigation")
report.append("")
report.append("="*80)

report_text = "\n".join(report)
print("\n" + report_text)

# Save
Path("results").mkdir(exist_ok=True)
with open('results/statistical_report.txt', 'w') as f:
    f.write(report_text)

print("\n Report saved to results/statistical_report.txt")
print("="*80)
