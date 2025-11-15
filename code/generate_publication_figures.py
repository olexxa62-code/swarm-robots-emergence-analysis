#!/usr/bin/env python3
"""
Generate Publication-Quality Figures for System A.2

Creates high-resolution (600 DPI) figures suitable for academic publication.

Author: Oleksii Onasenko
Developer: SubstanceNet
Date: November 2025
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Publication standards
DPI = 600
FIGSIZE_SINGLE = (8, 6)
FIGSIZE_DOUBLE = (12, 5)
FONTSIZE_TITLE = 14
FONTSIZE_LABEL = 12
FONTSIZE_LEGEND = 10
FONTSIZE_TICK = 10

# Colors
COLOR_FIG5 = '#2E86AB'  # Blue
COLOR_FIG8 = '#A23B72'  # Purple
COLOR_CRITICAL = '#F18F01'  # Orange
COLOR_GRID = '#CCCCCC'

def set_publication_style():
    """Set matplotlib style for publication."""
    plt.rcParams.update({
        'font.family': 'serif',
        'font.size': FONTSIZE_TICK,
        'axes.labelsize': FONTSIZE_LABEL,
        'axes.titlesize': FONTSIZE_TITLE,
        'xtick.labelsize': FONTSIZE_TICK,
        'ytick.labelsize': FONTSIZE_TICK,
        'legend.fontsize': FONTSIZE_LEGEND,
        'figure.dpi': DPI,
        'savefig.dpi': DPI,
        'savefig.bbox': 'tight',
        'axes.grid': True,
        'grid.alpha': 0.3,
        'grid.linestyle': ':',
        'axes.axisbelow': True
    })

def create_figure1_phase_transition(df_fig5, output_dir):
    """Figure 1: Phase transition (κ vs ψ)"""
    fig, ax = plt.subplots(figsize=FIGSIZE_SINGLE)
    
    ax.plot(df_fig5['kappa_correct'], df_fig5['psi'], 
            'o-', color=COLOR_FIG5, markersize=8, linewidth=2,
            label='Experimental data')
    
    ax.axvline(x=1.0, color=COLOR_CRITICAL, linestyle='--', 
               linewidth=2, alpha=0.8, label='κ = 1 (critical)')
    ax.axvspan(0.8, 1.2, alpha=0.15, color=COLOR_CRITICAL)
    
    ax.set_xlabel('Emergence parameter κ', fontweight='bold')
    ax.set_ylabel('Polarization ψ', fontweight='bold')
    ax.set_title('Phase Transition: Order Parameter vs κ')
    ax.legend(loc='lower right')
    ax.set_xlim(0, df_fig5['kappa_correct'].max() * 1.1)
    ax.set_ylim(-0.05, 1.05)
    
    filename = output_dir / 'fig1_phase_transition_kappa_vs_psi.png'
    plt.savefig(filename, dpi=DPI, bbox_inches='tight')
    print(f"Created: {filename}")
    plt.close()

def create_figure2_functional_peak(df_fig5, output_dir):
    """Figure 2: Functional peak (κ vs R) - UPDATED VERSION"""
    fig, ax = plt.subplots(figsize=FIGSIZE_SINGLE)
    
    # Plot data
    ax.plot(df_fig5['kappa_correct'], df_fig5['R'], 
            'o-', color=COLOR_FIG5, markersize=8, linewidth=2,
            label='Group responsiveness R')
    
    # Critical region
    ax.axvline(x=1.0, color=COLOR_CRITICAL, linestyle='--', 
               linewidth=2, alpha=0.8, label='κ = 1 (critical)')
    ax.axvspan(0.8, 1.2, alpha=0.15, color=COLOR_CRITICAL)
    
    # Mark peak
    idx_max = df_fig5['R'].idxmax()
    kappa_max = df_fig5.loc[idx_max, 'kappa_correct']
    R_max = df_fig5.loc[idx_max, 'R']
    
    ax.plot(kappa_max, R_max, '*', color='gold', markersize=20,
            markeredgecolor='black', markeredgewidth=1.5,
            label=f'Peak at κ={kappa_max:.3f}')
    
    # SHORT annotation - closer to point
    ax.annotate(f'R = {R_max:.3f}\nκ = {kappa_max:.3f}',
                xy=(kappa_max, R_max),
                xytext=(kappa_max + 0.3, R_max - 0.12),
                fontsize=10,
                bbox=dict(boxstyle='round,pad=0.5', 
                         facecolor='yellow', alpha=0.7),
                arrowprops=dict(arrowstyle='->', lw=1.5))
    
    # Labels
    ax.set_xlabel('Emergence parameter κ', fontweight='bold')
    ax.set_ylabel('Group responsiveness R', fontweight='bold')
    ax.set_title('Functional Optimum at Critical Point')
    
    # Legend - UPPER LEFT
    ax.legend(loc='upper left')
    
    ax.set_xlim(0, df_fig5['kappa_correct'].max() * 1.1)
    ax.set_ylim(-0.1, 0.9)
    
    filename = output_dir / 'fig2_functional_peak_kappa_vs_R.png'
    plt.savefig(filename, dpi=DPI, bbox_inches='tight')
    print(f"Created: {filename}")
    plt.close()

def create_figure3_combined_experiments(df_fig5, df_fig8, output_dir):
    """Figure 3: Combined experiments comparison"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIGSIZE_DOUBLE)
    
    # Left: Fig5
    ax1.plot(df_fig5['kappa_correct'], df_fig5['R'], 
             'o-', color=COLOR_FIG5, markersize=8, linewidth=2)
    ax1.axvline(x=1.0, color=COLOR_CRITICAL, linestyle='--', 
                linewidth=2, alpha=0.8)
    ax1.axvspan(0.8, 1.2, alpha=0.15, color=COLOR_CRITICAL)
    
    idx_max = df_fig5['R'].idxmax()
    ax1.plot(df_fig5.loc[idx_max, 'kappa_correct'], 
             df_fig5.loc[idx_max, 'R'],
             '*', color='gold', markersize=18,
             markeredgecolor='black', markeredgewidth=1.5)
    
    ax1.set_xlabel('Emergence parameter κ', fontweight='bold')
    ax1.set_ylabel('Group responsiveness R', fontweight='bold')
    ax1.set_title('(a) Collective Response Task')
    ax1.set_xlim(0, 2.5)
    
    # Right: Fig8
    ax2.plot(df_fig8['kappa_correct'], df_fig8['T_fc'], 
             's-', color=COLOR_FIG8, markersize=8, linewidth=2)
    ax2.axvline(x=1.0, color=COLOR_CRITICAL, linestyle='--', 
                linewidth=2, alpha=0.8)
    ax2.axvspan(0.8, 1.2, alpha=0.15, color=COLOR_CRITICAL)
    
    idx_max = df_fig8['T_fc'].idxmax()
    ax2.plot(df_fig8.loc[idx_max, 'kappa_correct'], 
             df_fig8.loc[idx_max, 'T_fc'],
             '*', color='gold', markersize=18,
             markeredgecolor='black', markeredgewidth=1.5)
    
    ax2.set_xlabel('Emergence parameter κ', fontweight='bold')
    ax2.set_ylabel('First capture time (s)', fontweight='bold')
    ax2.set_title('(b) Collective Evasion Task')
    ax2.set_xlim(0, 2.5)
    
    plt.tight_layout()
    
    filename = output_dir / 'fig3_combined_both_experiments.png'
    plt.savefig(filename, dpi=DPI, bbox_inches='tight')
    print(f"Created: {filename}")
    plt.close()

def create_figure4_order_vs_function(df_fig5, output_dir):
    """Figure 4: Order parameter vs functional response"""
    fig, ax = plt.subplots(figsize=FIGSIZE_SINGLE)
    
    colors = []
    for k in df_fig5['kappa_correct']:
        if k < 0.8:
            colors.append('#E63946')
        elif k <= 1.2:
            colors.append('#06D6A0')
        else:
            colors.append('#118AB2')
    
    scatter = ax.scatter(df_fig5['psi'], df_fig5['R'], 
                        c=colors, s=150, alpha=0.7, edgecolors='black')
    
    idx_max = df_fig5['R'].idxmax()
    ax.scatter(df_fig5.loc[idx_max, 'psi'], 
              df_fig5.loc[idx_max, 'R'],
              marker='*', s=400, c='gold', 
              edgecolors='black', linewidths=2,
              zorder=10, label='Critical point (κ ≈ 1)')
    
    ax.set_xlabel('Polarization ψ (order parameter)', fontweight='bold')
    ax.set_ylabel('Group responsiveness R (function)', fontweight='bold')
    ax.set_title('High Order Does Not Guarantee High Function')
    ax.legend()
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.1, 0.9)
    
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#E63946', label='Subcritical (κ < 0.8)'),
        Patch(facecolor='#06D6A0', label='Critical (0.8 ≤ κ ≤ 1.2)'),
        Patch(facecolor='#118AB2', label='Supercritical (κ > 1.2)')
    ]
    ax.legend(handles=legend_elements, loc='lower right')
    
    filename = output_dir / 'fig4_order_vs_function.png'
    plt.savefig(filename, dpi=DPI, bbox_inches='tight')
    print(f"Created: {filename}")
    plt.close()

def main():
    """Generate all publication figures."""
    print("\n" + "="*80)
    print("GENERATING PUBLICATION-QUALITY FIGURES")
    print("="*80 + "\n")
    
    set_publication_style()
    
    data_path = Path("data/swarm_robots_complete_data.csv")
    df = pd.read_csv(data_path)
    
    df_fig5 = df[df['experiment'] == 'fig5'].copy()
    df_fig8 = df[df['experiment'] == 'fig8'].copy()
    
    output_dir = Path("figures/publication")
    output_dir.mkdir(exist_ok=True)
    
    print("Creating Figure 1: Phase transition...")
    create_figure1_phase_transition(df_fig5, output_dir)
    
    print("Creating Figure 2: Functional peak...")
    create_figure2_functional_peak(df_fig5, output_dir)
    
    print("Creating Figure 3: Combined experiments...")
    create_figure3_combined_experiments(df_fig5, df_fig8, output_dir)
    
    print("Creating Figure 4: Order vs function...")
    create_figure4_order_vs_function(df_fig5, output_dir)
    
    print("\n" + "="*80)
    print("ALL FIGURES GENERATED SUCCESSFULLY")
    print("="*80)
    print(f"\nLocation: {output_dir.absolute()}")
    print(f"Resolution: {DPI} DPI (publication quality)")
    print(f"Total figures: 4")

if __name__ == "__main__":
    main()
