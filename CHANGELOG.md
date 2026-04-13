# Changelog

All notable changes to the A.2 swarm_robots_kappa_analysis project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.1] - 2025-04-13
### Fixed
- README: version number, emoji symbols, documentation list

## [1.1.0] - 2025-04-13
### Fixed
- Fabricated author list in DATA_PROVENANCE.md replaced with correct authors
- Cross-system reference to A.8 (starling flocks) removed from statistical tests
- Missing kappa value for fig5 w_ali=10 filled (k=0.143)
- Fictitious kappa values (7.4, 4.1) in 04_Results.md corrected to actual data
- Column name kappa->kappa_correct in statistical_tests.py and visualization.py
- Data file paths in statistical_tests.py and visualization.py
- Nonexistent T_turn column removed from visualization.py
- Reference filenames in docs/references/README.md
- Dates 2024->2025 in CHANGELOG.md and CITATION.cff
- Attribution placeholder in CONTRIBUTING.md

### Removed
- Inconsistent FIGURE_DESCRIPTIONS.md (duplicate of FIGURE_CAPTIONS.md)
- Emoji symbols from PARAMETER_JUSTIFICATION.md and DATA_PROVENANCE.md
- Reference to nonexistent 06_Conclusions.md from docs/.structure

### Changed
- summary_statistics.txt reports critical_mean instead of misleading combined_mean
- Repository Structure in README.md updated to match actual files

## [1.0.0] - 2025-11-24

### Added
- Complete analysis framework for swarm robots κ parameter
- Statistical validation of κ ≈ 1 hypothesis  
- Publication-quality figure generation (600 DPI)
- Comprehensive documentation in academic format
- Full attribution to all source files

### Changed
- Corrected κ formula to use ψ · (⟨NND⟩/202.7)
- Removed all emoji from code and documentation
- Standardized attribution format across all files

### Fixed
- Restored missing Python code from git history
- Corrected incomplete attribution in 4 Python files
- Removed non-academic symbols from outputs

## [0.1.0] - 2025-11-15

### Added
- Initial implementation based on Lei et al. (2023) data
- Basic κ calculation framework
- Preliminary statistical tests

