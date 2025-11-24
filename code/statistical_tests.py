#!/usr/bin/env python3
"""
Statistical Tests Module for System A.2: Swarm Robots
====================================================

Performs rigorous statistical validation of κ ≈ 1 hypothesis.

Tests include:
- Peak detection and significance
- Correlation analysis
- Regime comparison

System Classification: A.2 swarm_robots_kappa_analysis
Author: Oleksii Onasenko
Developer: SubstanceNet
Theoretical Framework: The Emergence Parameter κ ≈ 1: An Empirical Signature of Criticality in Physical and Biological Systems
Date: November 2025
"""

import numpy as np
import pandas as pd
from scipy import stats
from scipy.signal import find_peaks
from typing import Dict, Tuple


class SwarmRobotsStatistics:
    """
    Statistical analysis for swarm robots emergence.
    
    Validates:
    1. Peak R occurs at κ ≈ 1
    2. Significant difference between regimes
    3. Correlation between κ and emergent properties
    """
    
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.results = {}
    
    def analyze_peak_location(self) -> Dict:
        """
        Analyze location of peak R relative to κ = 1.
        
        Returns
        -------
        dict
            Peak statistics and proximity to critical point
        """
        # Find peak
        peak_idx = self.df['R'].idxmax()
        peak_kappa = self.df.loc[peak_idx, 'kappa']
        peak_R = self.df.loc[peak_idx, 'R']
        peak_w_ali = self.df.loc[peak_idx, 'w_ali']
        
        # Distance from κ = 1
        delta_kappa = abs(peak_kappa - 1.0)
        
        # Is peak within critical region (κ ∈ [0.8, 1.2])?
        in_critical_region = (0.8 <= peak_kappa <= 1.2)
        
        result = {
            'peak_kappa': peak_kappa,
            'peak_R': peak_R,
            'peak_w_ali': peak_w_ali,
            'delta_from_critical': delta_kappa,
            'in_critical_region': in_critical_region,
            'relative_error_%': (delta_kappa / 1.0) * 100
        }
        
        self.results['peak_analysis'] = result
        return result
    
    def test_regime_differences(self) -> Dict:
        """
        Test whether sub/critical/super-critical regimes are statistically different.
        
        Uses Kruskal-Wallis H-test (non-parametric ANOVA).
        
        Returns
        -------
        dict
            Statistical test results
        """
        # Classify regimes
        df = self.df.copy()
        conditions = [
            df['kappa'] < 0.8,
            (df['kappa'] >= 0.8) & (df['kappa'] <= 1.2),
            df['kappa'] > 1.2
        ]
        df['regime'] = np.select(conditions, 
                                 ['sub-critical', 'critical', 'super-critical'],
                                 default='unknown')
        
        # Separate groups
        sub = df[df['regime'] == 'sub-critical']
        crit = df[df['regime'] == 'critical']
        sup = df[df['regime'] == 'super-critical']
        
        # Kruskal-Wallis test for R
        if len(sub) > 0 and len(crit) > 0 and len(sup) > 0:
            h_stat, p_value = stats.kruskal(sub['R'], crit['R'], sup['R'])
            
            result = {
                'test': 'Kruskal-Wallis H-test',
                'metric': 'Group responsiveness R',
                'H_statistic': h_stat,
                'p_value': p_value,
                'significant': p_value < 0.05,
                'n_sub': len(sub),
                'n_critical': len(crit),
                'n_super': len(sup),
                'R_sub_mean': sub['R'].mean(),
                'R_critical_mean': crit['R'].mean(),
                'R_super_mean': sup['R'].mean()
            }
        else:
            result = {
                'test': 'Kruskal-Wallis H-test',
                'error': 'Insufficient data in some regimes'
            }
        
        self.results['regime_test'] = result
        return result
    
    def test_pairwise_regimes(self) -> Dict:
        """
        Pairwise Mann-Whitney U tests between regimes.
        
        Returns
        -------
        dict
            Pairwise comparison results
        """
        df = self.df.copy()
        conditions = [
            df['kappa'] < 0.8,
            (df['kappa'] >= 0.8) & (df['kappa'] <= 1.2),
            df['kappa'] > 1.2
        ]
        df['regime'] = np.select(conditions, 
                                 ['sub-critical', 'critical', 'super-critical'],
                                 default='unknown')
        
        sub = df[df['regime'] == 'sub-critical']['R']
        crit = df[df['regime'] == 'critical']['R']
        sup = df[df['regime'] == 'super-critical']['R']
        
        pairwise = {}
        
        # Sub vs Critical
        if len(sub) > 0 and len(crit) > 0:
            u_stat, p_val = stats.mannwhitneyu(sub, crit, alternative='two-sided')
            pairwise['sub_vs_critical'] = {
                'U_statistic': u_stat,
                'p_value': p_val,
                'significant': p_val < 0.05
            }
        
        # Critical vs Super
        if len(crit) > 0 and len(sup) > 0:
            u_stat, p_val = stats.mannwhitneyu(crit, sup, alternative='two-sided')
            pairwise['critical_vs_super'] = {
                'U_statistic': u_stat,
                'p_value': p_val,
                'significant': p_val < 0.05
            }
        
        # Sub vs Super
        if len(sub) > 0 and len(sup) > 0:
            u_stat, p_val = stats.mannwhitneyu(sub, sup, alternative='two-sided')
            pairwise['sub_vs_super'] = {
                'U_statistic': u_stat,
                'p_value': p_val,
                'significant': p_val < 0.05
            }
        
        self.results['pairwise_tests'] = pairwise
        return pairwise
    
    def calculate_correlations(self) -> Dict:
        """
        Calculate correlations between κ and emergent properties.
        
        Returns
        -------
        dict
            Correlation coefficients and p-values
        """
        correlations = {}
        
        # κ vs ψ (should be strong positive)
        r_psi, p_psi = stats.pearsonr(self.df['kappa'], self.df['psi'])
        correlations['kappa_vs_psi'] = {
            'pearson_r': r_psi,
            'p_value': p_psi,
            'interpretation': 'Phase transition correlation'
        }
        
        # κ vs R (should be non-monotonic, peak at κ≈1)
        r_R, p_R = stats.pearsonr(self.df['kappa'], self.df['R'])
        spearman_R, sp_p_R = stats.spearmanr(self.df['kappa'], self.df['R'])
        
        correlations['kappa_vs_R'] = {
            'pearson_r': r_R,
            'pearson_p': p_R,
            'spearman_rho': spearman_R,
            'spearman_p': sp_p_R,
            'interpretation': 'Non-monotonic (peak at critical point)'
        }
        
        # ψ vs R (order vs function)
        r_psi_R, p_psi_R = stats.pearsonr(self.df['psi'], self.df['R'])
        correlations['psi_vs_R'] = {
            'pearson_r': r_psi_R,
            'p_value': p_psi_R,
            'interpretation': 'Order parameter vs function'
        }
        
        self.results['correlations'] = correlations
        return correlations
    
    def generate_report(self) -> str:
        """
        Generate comprehensive statistical report.
        
        Returns
        -------
        str
            Formatted report text
        """
        report = []
        report.append("=" * 70)
        report.append("STATISTICAL ANALYSIS REPORT")
        report.append("System A.2: Swarm Robots Emergence")
        report.append("=" * 70)
        
        # Peak analysis
        if 'peak_analysis' in self.results:
            peak = self.results['peak_analysis']
            report.append("\n1. PEAK LOCATION ANALYSIS")
            report.append("-" * 70)
            report.append(f"Peak κ value: {peak['peak_kappa']:.3f}")
            report.append(f"Peak R value: {peak['peak_R']:.3f}")
            report.append(f"Peak w_ali: {peak['peak_w_ali']:.1f}")
            report.append(f"Distance from κ=1: {peak['delta_from_critical']:.3f}")
            report.append(f"Relative error: {peak['relative_error_%']:.1f}%")
            report.append(f"In critical region [0.8, 1.2]: {peak['in_critical_region']}")
            
            if peak['in_critical_region']:
                report.append("✓ CONCLUSION: Peak R occurs within critical region!")
            else:
                report.append("⚠ CONCLUSION: Peak R is outside critical region")
        
        # Regime differences
        if 'regime_test' in self.results:
            regime = self.results['regime_test']
            report.append("\n2. REGIME COMPARISON (Kruskal-Wallis)")
            report.append("-" * 70)
            if 'error' not in regime:
                report.append(f"H-statistic: {regime['H_statistic']:.4f}")
                report.append(f"p-value: {regime['p_value']:.4e}")
                report.append(f"Significant (p < 0.05): {regime['significant']}")
                report.append(f"\nMean R by regime:")
                report.append(f"  Sub-critical (n={regime['n_sub']}): {regime['R_sub_mean']:.3f}")
                report.append(f"  Critical (n={regime['n_critical']}): {regime['R_critical_mean']:.3f}")
                report.append(f"  Super-critical (n={regime['n_super']}): {regime['R_super_mean']:.3f}")
            else:
                report.append(f"Error: {regime['error']}")
        
        # Pairwise tests
        if 'pairwise_tests' in self.results:
            report.append("\n3. PAIRWISE COMPARISONS (Mann-Whitney U)")
            report.append("-" * 70)
            for comparison, result in self.results['pairwise_tests'].items():
                report.append(f"\n{comparison.replace('_', ' ').title()}:")
                report.append(f"  U-statistic: {result['U_statistic']:.2f}")
                report.append(f"  p-value: {result['p_value']:.4f}")
                report.append(f"  Significant: {result['significant']}")
        
        # Correlations
        if 'correlations' in self.results:
            report.append("\n4. CORRELATIONS")
            report.append("-" * 70)
            for name, corr in self.results['correlations'].items():
                report.append(f"\n{name.replace('_', ' vs ').upper()}:")
                if 'pearson_r' in corr:
                    report.append(f"  Pearson r: {corr['pearson_r']:.4f}")
                    if 'p_value' in corr:
                        report.append(f"  p-value: {corr['p_value']:.4e}")
                if 'spearman_rho' in corr:
                    report.append(f"  Spearman ρ: {corr['spearman_rho']:.4f}")
                report.append(f"  Note: {corr['interpretation']}")
        
        report.append("\n" + "=" * 70)
        
        return "\n".join(report)
    
    def run_all_tests(self) -> Dict:
        """
        Run complete statistical analysis.
        
        Returns
        -------
        dict
            All test results
        """
        self.analyze_peak_location()
        self.test_regime_differences()
        self.test_pairwise_regimes()
        self.calculate_correlations()
        
        return self.results


def main():
    """Example usage."""
    # Load results
    data_path = "./data/analysis_results.csv"
    df = pd.read_csv(data_path)
    
    # Run statistical tests
    stats_analyzer = SwarmRobotsStatistics(df)
    results = stats_analyzer.run_all_tests()
    
    # Print report
    report = stats_analyzer.generate_report()
    print(report)
    
    # Save report
    output_path = "./docs/statistical_report.txt"
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(report)
    
    print(f"\nReport saved to {output_path}")


if __name__ == "__main__":
    from pathlib import Path
    main()
