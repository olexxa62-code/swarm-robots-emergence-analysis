# Installation Guide

## System Requirements

- Python 3.8 or higher
- 2 GB RAM minimum
- 500 MB disk space

## Installation Steps

### 1. Clone Repository
```bash
git clone [repository-url]
cd A.2_swarm_robots_kappa_analysis
```

### 2. Create Virtual Environment
```bash
python -m venv my_env
source my_env/bin/activate  # On Windows: my_env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

Required packages:
- pandas>=1.3.0
- numpy>=1.21.0
- matplotlib>=3.4.0
- scipy>=1.7.0

### 4. Verify Installation
```bash
python code/run_full_analysis.py
```

Expected output:
- κ mean: 0.976 ± 0.022
- Statistical validation: p = 0.359
- Generated files in results/ and figures/

## Project Structure
```
A.2_swarm_robots_kappa_analysis/
├── code/              # Python analysis scripts
├── data/              # Experimental data (CSV)
├── docs/              # Documentation
├── figures/           # Generated plots
├── results/           # Analysis outputs
└── requirements.txt   # Python dependencies
```

## Data Files

The project includes:
- `data/swarm_robots_complete_data.csv`: Preprocessed experimental data from Lei et al. (2023)

## Running Analysis

### Complete Analysis
```bash
python code/run_full_analysis.py
```

### Statistical Tests Only
```bash
python code/run_statistical_tests.py
```

### Generate Publication Figures
```bash
python code/generate_publication_figures.py
```

## Troubleshooting

### Import Errors
Ensure virtual environment is activated and all packages installed.

### Data Not Found
Verify `data/swarm_robots_complete_data.csv` exists.

### Permission Errors
Ensure write permissions for results/ and figures/ directories.

## Contact

For installation issues, refer to CONTRIBUTING.md for contact information.
