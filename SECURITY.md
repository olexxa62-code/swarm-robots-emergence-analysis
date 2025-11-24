# Security Policy

## Supported Versions

Currently supported versions of the A.2 Swarm Robots Kappa Analysis:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

This is a scientific research project. Security concerns primarily relate to:

1. **Data Integrity**: Ensuring experimental data remains unmodified
2. **Calculation Accuracy**: Verifying κ parameter calculations
3. **Code Reliability**: Maintaining reproducible results

### To Report an Issue:

1. **Data Concerns**: If you discover discrepancies in the swarm robots data or calculations
2. **Code Issues**: If you find bugs affecting the κ parameter computation
3. **Documentation**: If you identify errors in mathematical formulations

Please report to the project maintainer with:
- Detailed description of the issue
- Steps to reproduce
- Expected vs actual results
- Relevant code or data references

### Response Timeline:

- Acknowledgment: Within 48 hours
- Initial Assessment: Within 1 week
- Resolution: Depends on severity and complexity

## Data Protection

- All experimental data is versioned in git
- Calculations are independently verifiable
- Results are reproducible from raw data

## Verification

To verify integrity of calculations:
```python
python code/run_full_analysis.py
# Expected: κ = 0.976 ± 0.022
```
