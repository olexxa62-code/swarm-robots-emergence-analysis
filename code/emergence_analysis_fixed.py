"""Fixed emergence_analysis.py to work with CSV"""
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
        print(f"✅ Loaded {len(self.fig5)} Fig5 + {len(self.fig8)} Fig8 conditions")
    
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

if __name__ == "__main__":
    analyzer = SwarmRobotsAnalyzer()
    analyzer.load_data()
    critical = analyzer.get_critical_points()
    
    print("\n🎯 Critical Points:")
    print(f"  Fig5: w_ali={critical['fig5']['w_ali']}, κ={critical['fig5']['kappa']:.3f}")
    print(f"  Fig8: w_ali={critical['fig8']['w_ali']}, κ={critical['fig8']['kappa']:.3f}")
