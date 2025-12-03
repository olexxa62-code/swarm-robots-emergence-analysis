"""
Fixed emergence_analysis.py to work with CSV
System Classification: A.2 swarm_robots_kappa_analysis
Author: Oleksii Onasenko
Developer: SubstanceNet
Theoretical Framework: The Emergence Parameter κ ≈ 1: An Empirical Signature of Criticality in Physical and Biological Systems
"""
import pandas as pd
import numpy as np
from pathlib import Path

class SwarmRobotsAnalyzer:
    def __init__(self, data_path='data/swarm_robots_complete_data.csv'):
        self.data_path = data_path
        self.data = None
        self.fig5 = None
        self.fig8 = None
    
    def load_data(self):
        """Load data from CSV"""
        print(f"Loading from {self.data_path}...")
        self.data = pd.read_csv(self.data_path)
        self.fig5 = self.data[self.data['experiment'] == 'fig5'].copy()
        self.fig8 = self.data[self.data['experiment'] == 'fig8'].copy()
        print(f"  Loaded {len(self.fig5)} Fig5 + {len(self.fig8)} Fig8 conditions")
    
    def get_critical_points(self):
        """Find critical points for both experiments"""
        fig5_critical_idx = self.fig5['R'].idxmax()
        fig8_critical_idx = self.fig8['T_fc'].idxmax()
        
        return {
            'fig5': {
                'w_ali': self.fig5.loc[fig5_critical_idx, 'w_ali'],
                'kappa': self.fig5.loc[fig5_critical_idx, 'kappa_correct'],
                'R': self.fig5.loc[fig5_critical_idx, 'R']
            },
            'fig8': {
                'w_ali': self.fig8.loc[fig8_critical_idx, 'w_ali'],
                'kappa': self.fig8.loc[fig8_critical_idx, 'kappa_correct'],
                'T_fc': self.fig8.loc[fig8_critical_idx, 'T_fc']
            }
        }

    def calculate_kappa_from_raw(self, Lambda_c=202.7):
        """
        Calculate kappa directly from raw data columns (psi, NND_mean).
        
        Formula: kappa = psi * (NND / Lambda_c)
        
        Since N = Nc = 30 (fixed), the A/Ac term equals 1.
        
        Args:
            Lambda_c: Critical spatial correlation length (mm), default 202.7
            
        Returns:
            DataFrame with calculated kappa and comparison to stored values
        """
        results = []
        
        for _, row in self.data.iterrows():
            psi = row['psi']
            nnd = row['NND_mean']
            
            # Calculate kappa from raw data
            if pd.notna(psi) and pd.notna(nnd) and psi > 0:
                kappa_calculated = psi * (nnd / Lambda_c)
            else:
                kappa_calculated = np.nan
            
            results.append({
                'experiment': row['experiment'],
                'w_ali': row['w_ali'],
                'psi': psi,
                'NND_mean': nnd,
                'kappa_calculated': kappa_calculated,
                'kappa_stored': row['kappa_correct'],
                'difference': abs(kappa_calculated - row['kappa_correct']) if pd.notna(row['kappa_correct']) else np.nan
            })
        
        return pd.DataFrame(results)
    
    def verify_kappa_calculation(self, Lambda_c=202.7):
        """
        Verify that stored kappa values match calculation from raw data.
        Prints detailed comparison for transparency.
        """
        print("\n" + "="*70)
        print("KAPPA CALCULATION VERIFICATION FROM RAW DATA")
        print("="*70)
        print(f"\nFormula: kappa = psi * (NND / Lambda_c)")
        print(f"Parameters: Lambda_c = {Lambda_c} mm, N = Nc = 30")
        print("-"*70)
        
        df = self.calculate_kappa_from_raw(Lambda_c)
        
        # Filter valid rows
        valid = df.dropna(subset=['kappa_calculated', 'kappa_stored'])
        
        print(f"\n{'Exp':<6} {'w_ali':<8} {'psi':<8} {'NND':<10} {'k_calc':<10} {'k_stored':<10} {'Diff':<8}")
        print("-"*70)
        
        for _, row in valid.iterrows():
            print(f"{row['experiment']:<6} {row['w_ali']:<8} {row['psi']:<8.3f} "
                  f"{row['NND_mean']:<10.1f} {row['kappa_calculated']:<10.4f} "
                  f"{row['kappa_stored']:<10.4f} {row['difference']:<8.6f}")
        
        max_diff = valid['difference'].max()
        mean_diff = valid['difference'].mean()
        
        print("-"*70)
        print(f"Max difference: {max_diff:.6f}")
        print(f"Mean difference: {mean_diff:.6f}")
        
        if max_diff < 0.001:
            print("VERIFIED: All kappa values match calculation from raw data")
        else:
            print("WARNING: Some discrepancies found")
        
        return df


if __name__ == "__main__":
    analyzer = SwarmRobotsAnalyzer()
    analyzer.load_data()
    
    # Verify kappa calculation transparency
    analyzer.verify_kappa_calculation()
    
    # Show critical points
    critical = analyzer.get_critical_points()
    print("\nCritical Points:")
    print(f"  Fig5: w_ali={critical['fig5']['w_ali']}, kappa={critical['fig5']['kappa']:.3f}")
    print(f"  Fig8: w_ali={critical['fig8']['w_ali']}, kappa={critical['fig8']['kappa']:.3f}")
