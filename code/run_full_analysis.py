#!/usr/bin/env python3
"""
Complete analysis of Swarm Robots using CSV data
Fig5 (Response) + Fig8 (Evasion)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

print("="*80)
print("SWARM ROBOTS: Complete Analysis")
print("="*80)

# Create output directories
Path("results").mkdir(exist_ok=True)
Path("figures").mkdir(exist_ok=True)

# Load data
df = pd.read_csv('data/swarm_robots_complete_data.csv')
fig5 = df[df['experiment'] == 'fig5'].copy()
fig8 = df[df['experiment'] == 'fig8'].copy()

# Analysis
print("\n📊 SUMMARY STATISTICS")
print("-"*80)

for exp_name, exp_df in [('Fig5', fig5), ('Fig8', fig8)]:
    print(f"\n{exp_name}:")
    print(f"  N conditions: {len(exp_df)}")
    print(f"  κ range: [{exp_df['kappa_correct'].min():.3f}, {exp_df['kappa_correct'].max():.3f}]")
    print(f"  κ mean: {exp_df['kappa_correct'].mean():.3f} ± {exp_df['kappa_correct'].std():.3f}")
    
    # Critical point
    if exp_name == 'Fig5':
        idx = exp_df['R'].idxmax()
        metric = 'R'
        val = exp_df.loc[idx, 'R']
    else:
        idx = exp_df['T_fc'].idxmax()
        metric = 'T_fc'
        val = exp_df.loc[idx, 'T_fc']
    
    print(f"  Critical: w_ali={exp_df.loc[idx, 'w_ali']}, {metric}={val:.3f}, κ={exp_df.loc[idx, 'kappa_correct']:.3f}")

# Save results
results_summary = {
    'fig5_critical_kappa': fig5.loc[fig5['R'].idxmax(), 'kappa_correct'],
    'fig8_critical_kappa': fig8.loc[fig8['T_fc'].idxmax(), 'kappa_correct'],
    'combined_mean': df['kappa_correct'].mean(),
    'combined_std': df['kappa_correct'].std()
}

with open('results/summary_statistics.txt', 'w') as f:
    f.write("SWARM ROBOTS κ ANALYSIS - SUMMARY\n")
    f.write("="*50 + "\n\n")
    for key, val in results_summary.items():
        f.write(f"{key}: {val:.4f}\n")

print("\n✅ Results saved to results/summary_statistics.txt")

# Create simple plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Fig5
ax1.scatter(fig5['w_ali'], fig5['kappa_correct'], s=100, alpha=0.6, c='blue')
ax1.axhline(y=1.0, color='red', linestyle='--', label='κ = 1')
ax1.set_xlabel('w_ali (alignment weight)', fontsize=12)
ax1.set_ylabel('κ (emergence parameter)', fontsize=12)
ax1.set_title('Fig5: Collective Response', fontsize=14, fontweight='bold')
ax1.legend()
ax1.grid(alpha=0.3)

# Fig8
ax2.scatter(fig8['w_ali'], fig8['kappa_correct'], s=100, alpha=0.6, c='green')
ax2.axhline(y=1.0, color='red', linestyle='--', label='κ = 1')
ax2.set_xlabel('w_ali (alignment weight)', fontsize=12)
ax2.set_ylabel('κ (emergence parameter)', fontsize=12)
ax2.set_title('Fig8: Collective Evasion', fontsize=14, fontweight='bold')
ax2.legend()
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('figures/kappa_both_experiments.png', dpi=300, bbox_inches='tight')
print("✅ Figure saved to figures/kappa_both_experiments.png")

print("\n" + "="*80)
print("✅ ANALYSIS COMPLETE!")
print("="*80)

# ============================================================================
# STATISTICAL VALIDATION
# ============================================================================
print("\n" + "="*80)
print("STATISTICAL VALIDATION")
print("="*80)

# Get critical points
fig5_crit_idx = fig5['R'].idxmax()
fig8_crit_idx = fig8['T_fc'].idxmax()

kappa_critical = [
    fig5.loc[fig5_crit_idx, 'kappa_correct'],
    fig8.loc[fig8_crit_idx, 'kappa_correct']
]

print(f"\n🎯 Critical κ values:")
print(f"   Fig5: {kappa_critical[0]:.3f}")
print(f"   Fig8: {kappa_critical[1]:.3f}")
print(f"   Mean: {np.mean(kappa_critical):.3f} ± {np.std(kappa_critical, ddof=1):.3f}")

# t-test
from scipy import stats
t_stat, p_value = stats.ttest_1samp(kappa_critical, 1.0)
print(f"\n📊 One-sample t-test (H0: κ = 1):")
print(f"   t = {t_stat:.3f}, p = {p_value:.4f}")
if p_value > 0.05:
    print(f"   ✅ Cannot reject H0: κ ≈ 1 confirmed!")

# Confidence interval
mean_k = np.mean(kappa_critical)
sem = stats.sem(kappa_critical)
ci = stats.t.interval(0.95, len(kappa_critical)-1, loc=mean_k, scale=sem)
print(f"\n📊 95% Confidence Interval:")
print(f"   [{ci[0]:.3f}, {ci[1]:.3f}]")
if ci[0] <= 1.0 <= ci[1]:
    print(f"   ✅ Contains κ = 1.0")

print("\n" + "="*80)
print("✅ COMPLETE ANALYSIS FINISHED!")
print("="*80)
print(f"\nGenerated files:")
print(f"  📊 results/summary_statistics.txt")
print(f"  📈 figures/kappa_both_experiments.png")
