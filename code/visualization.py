#!/usr/bin/env python3
"""
Visualization Module for System A.2: Swarm Robots
================================================

Creates publication-quality figures for emergence analysis.

All figures at 600 DPI, English labels, following established style.

System Classification: A.2 swarm_robots_kappa_analysis
Author: Oleksii Onasenko
Developer: SubstanceNet
Theoretical Framework: The Emergence Parameter κ ≈ 1: An Empirical Signature of Criticality in Physical and Biological Systems
Date: November 2025
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path
from typing import Optional, Tuple


class SwarmRobotsVisualizer:
    """
    Visualizer for swarm robots κ-analysis.
    
    Creates publication-ready figures showing:
    1. Phase transition (κ vs ψ)
    2. Functional advantage (κ vs R)
    3. Combined phase diagram
    """
    
    def __init__(self, output_dir: str = "./figures"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Style parameters
        self.dpi = 600
        self.figsize = (10, 7)
        self.color_data = '#d62728'  # Red for data points
        self.color_critical = '#2ca02c'  # Green for critical region
        self.fontsize_label = 14
        self.fontsize_title = 16
        self.fontsize_legend = 12
        self.markersize = 10
        self.linewidth = 2.5
    
    def plot_kappa_vs_psi(self, df: pd.DataFrame, save: bool = True) -> None:
        """
        Plot phase transition: κ vs polarization ψ.
        
        Shows transition from disordered (ψ ≈ 0) to ordered (ψ ≈ 1) motion.
        
        Parameters
        ----------
        df : pd.DataFrame
            Results with columns: kappa, psi
        save : bool
            Whether to save figure
        """
        fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)
        
        # Plot data points and line
        ax.plot(df['kappa_correct'], df['psi'], 'o-', 
                color=self.color_data, 
                markersize=self.markersize,
                linewidth=self.linewidth,
                label='Experimental data')
        
        # Mark critical region (κ ≈ 1)
        ax.axvline(x=1.0, color=self.color_critical, 
                  linestyle='--', linewidth=2, alpha=0.7,
                  label='κ = 1 (critical point)')
        
        ax.axvspan(0.8, 1.2, alpha=0.1, color=self.color_critical,
                  label='Critical region')
        
        # Labels
        ax.set_xlabel('Emergence parameter κ', fontsize=self.fontsize_label, fontweight='bold')
        ax.set_ylabel('Polarization ψ (order parameter)', 
                     fontsize=self.fontsize_label, fontweight='bold')
        ax.set_title('Phase Transition in Swarm Robots\nκ vs Order Parameter', 
                    fontsize=self.fontsize_title, fontweight='bold')
        
        # Grid and legend
        ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.8)
        ax.legend(fontsize=self.fontsize_legend, loc='lower right')
        
        # Axis limits
        ax.set_xlim(0, df['kappa_correct'].max() * 1.1)
        ax.set_ylim(-0.05, 1.05)
        
        plt.tight_layout()
        
        if save:
            output_path = self.output_dir / "fig1_kappa_vs_psi_phase_transition.png"
            plt.savefig(output_path, dpi=self.dpi, bbox_inches='tight')
            print(f"Saved: {output_path}")
        
        plt.show()
        plt.close()
    
    def plot_kappa_vs_R(self, df: pd.DataFrame, save: bool = True) -> None:
        """
        Plot functional advantage: κ vs group responsiveness R.
        
        KEY RESULT: Shows peak R at κ ≈ 1 (criticality hypothesis).
        
        Parameters
        ----------
        df : pd.DataFrame
            Results with columns: kappa, R
        save : bool
            Whether to save figure
        """
        fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)
        
        # Plot data points and line
        ax.plot(df['kappa_correct'], df['R'], 'o-', 
                color=self.color_data, 
                markersize=self.markersize,
                linewidth=self.linewidth,
                label='Group responsiveness R')
        
        # Mark critical region and peak
        ax.axvline(x=1.0, color=self.color_critical, 
                  linestyle='--', linewidth=2, alpha=0.7,
                  label='κ = 1 (critical point)')
        
        ax.axvspan(0.8, 1.2, alpha=0.1, color=self.color_critical,
                  label='Critical region')
        
        # Mark peak R
        peak_idx = df['R'].idxmax()
        peak_kappa = df.loc[peak_idx, 'kappa']
        peak_R = df.loc[peak_idx, 'R']
        
        ax.plot(peak_kappa, peak_R, '*', 
                color='gold', markersize=20, 
                markeredgecolor='black', markeredgewidth=1.5,
                label=f'Peak R at κ={peak_kappa:.2f}')
        
        # Add annotation for peak
        ax.annotate(f'Max R = {peak_R:.3f}\nκ = {peak_kappa:.2f}',
                   xy=(peak_kappa, peak_R),
                   xytext=(peak_kappa + 0.5, peak_R - 0.1),
                   fontsize=11,
                   bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                   arrowprops=dict(arrowstyle='->', lw=1.5))
        
        # Labels
        ax.set_xlabel('Emergence parameter κ', fontsize=self.fontsize_label, fontweight='bold')
        ax.set_ylabel('Group responsiveness R', 
                     fontsize=self.fontsize_label, fontweight='bold')
        ax.set_title('Criticality Hypothesis: Functional Peak at κ ≈ 1\nκ vs Collective Response', 
                    fontsize=self.fontsize_title, fontweight='bold')
        
        # Grid and legend
        ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.8)
        ax.legend(fontsize=self.fontsize_legend, loc='upper right')
        
        # Axis limits
        ax.set_xlim(0, df['kappa_correct'].max() * 1.1)
        ax.set_ylim(df['R'].min() - 0.1, df['R'].max() * 1.1)
        
        plt.tight_layout()
        
        if save:
            output_path = self.output_dir / "fig2_kappa_vs_R_functional_peak.png"
            plt.savefig(output_path, dpi=self.dpi, bbox_inches='tight')
            print(f"Saved: {output_path}")
        
        plt.show()
        plt.close()
    
    def plot_phase_diagram(self, df: pd.DataFrame, save: bool = True) -> None:
        """
        Plot combined phase diagram: κ vs multiple metrics.
        
        Shows ψ and R on same plot (normalized).
        
        Parameters
        ----------
        df : pd.DataFrame
            Results with all metrics
        save : bool
            Whether to save figure
        """
        fig, ax1 = plt.subplots(figsize=(12, 7), dpi=self.dpi)
        
        # Primary axis: ψ and R
        ax1.plot(df['kappa_correct'], df['psi'], 'o-', 
                color='blue', markersize=8, linewidth=2,
                label='Polarization ψ (order)')
        
        ax1.plot(df['kappa_correct'], df['R'], 's-', 
                color='red', markersize=8, linewidth=2,
                label='Responsiveness R (function)')
        
        ax1.set_xlabel('Emergence parameter κ', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Normalized metrics', fontsize=14, fontweight='bold')
        ax1.set_ylim(-0.1, 1.1)
        
        # Mark critical region
        ax1.axvline(x=1.0, color='green', linestyle='--', 
                   linewidth=2.5, alpha=0.7, label='κ = 1')
        ax1.axvspan(0.8, 1.2, alpha=0.15, color='green')
        
        
        # Title and legends
        ax1.set_title('System A.2 Phase Diagram: Swarm Robots\nEmergence at κ ≈ 1',
                     fontsize=16, fontweight='bold')
        
        ax1.legend(loc='upper left', fontsize=12)
        
        ax1.grid(True, alpha=0.3, linestyle=':', linewidth=0.8)
        
        plt.tight_layout()
        
        if save:
            output_path = self.output_dir / "fig3_phase_diagram_combined.png"
            plt.savefig(output_path, dpi=self.dpi, bbox_inches='tight')
            print(f"Saved: {output_path}")
        
        plt.show()
        plt.close()
    
    def plot_w_ali_comparison(self, df: pd.DataFrame, save: bool = True) -> None:
        """
        Plot original control parameter w_ali vs metrics.
        
        Shows how raw experimental parameter relates to κ.
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), dpi=self.dpi)
        
        # Left: w_ali vs ψ
        ax1.plot(df['w_ali'], df['psi'], 'o-', 
                color='blue', markersize=10, linewidth=2.5)
        ax1.axvline(x=25, color='green', linestyle='--', 
                   linewidth=2, label='w_ali = 25 (critical)')
        ax1.set_xlabel('Alignment weight w_ali', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Polarization ψ', fontsize=14, fontweight='bold')
        ax1.set_title('Phase Transition vs Control Parameter', fontsize=15)
        ax1.grid(True, alpha=0.3)
        ax1.legend(fontsize=12)
        
        # Right: w_ali vs R
        ax2.plot(df['w_ali'], df['R'], 'o-', 
                color='red', markersize=10, linewidth=2.5)
        ax2.axvline(x=25, color='green', linestyle='--', 
                   linewidth=2, label='w_ali = 25 (critical)')
        
        # Mark peak
        peak_idx = df['R'].idxmax()
        ax2.plot(df.loc[peak_idx, 'w_ali'], 
                df.loc[peak_idx, 'R'], 
                '*', color='gold', markersize=20,
                markeredgecolor='black', markeredgewidth=1.5,
                label=f"Peak at w_ali={df.loc[peak_idx, 'w_ali']:.0f}")
        
        ax2.set_xlabel('Alignment weight w_ali', fontsize=14, fontweight='bold')
        ax2.set_ylabel('Group responsiveness R', fontsize=14, fontweight='bold')
        ax2.set_title('Functional Peak Near Critical Point', fontsize=15)
        ax2.grid(True, alpha=0.3)
        ax2.legend(fontsize=12)
        
        plt.tight_layout()
        
        if save:
            output_path = self.output_dir / "fig4_w_ali_comparison.png"
            plt.savefig(output_path, dpi=self.dpi, bbox_inches='tight')
            print(f"Saved: {output_path}")
        
        plt.show()
        plt.close()
    
    def create_all_figures(self, df: pd.DataFrame) -> None:
        """
        Generate all publication figures.
        
        Parameters
        ----------
        df : pd.DataFrame
            Results dataframe
        """
        print("\n=== Generating Publication Figures ===\n")
        
        self.plot_kappa_vs_psi(df)
        self.plot_kappa_vs_R(df)
        self.plot_phase_diagram(df)
        self.plot_w_ali_comparison(df)
        
        print(f"\n✓ All figures saved to {self.output_dir}")
        print(f"  Resolution: {self.dpi} DPI")
        print(f"  Format: PNG (publication-ready)")


def main():
    """Example usage."""
    # Load results
    data_path = Path("./data/swarm_robots_complete_data.csv")
    df = pd.read_csv(data_path)
    
    # Create visualizer
    viz = SwarmRobotsVisualizer()
    
    # Generate all figures
    viz.create_all_figures(df)


if __name__ == "__main__":
    main()
