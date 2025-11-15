#!/usr/bin/env python3
"""Fix Figure 2 - Legend left, shorter annotation line"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DPI = 600
FIGSIZE = (8, 6)

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.dpi': DPI,
    'savefig.dpi': DPI
})

df = pd.read_csv('data/swarm_robots_complete_data.csv')
df_fig5 = df[df['experiment'] == 'fig5'].copy()

fig, ax = plt.subplots(figsize=FIGSIZE)

# Data
ax.plot(df_fig5['kappa_correct'], df_fig5['R'], 
        'o-', color='#2E86AB', markersize=8, linewidth=2,
        label='Group responsiveness R')

# Critical line
ax.axvline(x=1.0, color='#F18F01', linestyle='--', 
           linewidth=2, alpha=0.8, label='κ = 1 (critical)')
ax.axvspan(0.8, 1.2, alpha=0.15, color='#F18F01')

# Peak
idx_max = df_fig5['R'].idxmax()
kappa_max = df_fig5.loc[idx_max, 'kappa_correct']
R_max = df_fig5.loc[idx_max, 'R']

ax.plot(kappa_max, R_max, '*', color='gold', markersize=20,
        markeredgecolor='black', markeredgewidth=1.5,
        label=f'Peak at κ={kappa_max:.3f}')

# SHORT annotation - moved closer
ax.annotate(f'R = {R_max:.3f}\nκ = {kappa_max:.3f}',
            xy=(kappa_max, R_max),
            xytext=(kappa_max + 0.3, R_max - 0.12),  # Closer!
            fontsize=10,
            bbox=dict(boxstyle='round,pad=0.5', 
                     facecolor='yellow', alpha=0.7),
            arrowprops=dict(arrowstyle='->', lw=1.5))  # Thinner arrow

# Labels
ax.set_xlabel('Emergence parameter κ', fontweight='bold')
ax.set_ylabel('Group responsiveness R', fontweight='bold')
ax.set_title('Functional Optimum at Critical Point')

# Legend - LEFT position
ax.legend(loc='upper left')

ax.set_xlim(0, df_fig5['kappa_correct'].max() * 1.1)
ax.set_ylim(-0.1, 0.9)

plt.tight_layout()
plt.savefig('figures/publication/fig2_functional_peak_kappa_vs_R.png', 
            dpi=DPI, bbox_inches='tight')
print("✓ Figure 2 fixed")
