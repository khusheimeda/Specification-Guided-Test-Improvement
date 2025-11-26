# Exercise 3: Specification-Guided Test Improvement

## Project Structure

```
exercise3_part2/
├── problems/
│   ├── __init__.py
│   ├── is_prime.py              # HumanEval/31 implementation (DeepSeek-6.7B + CoT)
│   └── truncate_number.py       # HumanEval/2 implementation (CodeLlama-7B + CoT)
├── tests/
│   ├── test_is_prime_baseline.py           # Original Exercise 2 tests
│   ├── test_is_prime_spec_guided.py        # NEW: Spec-guided tests (Part 2)
│   ├── test_truncate_number_baseline.py    # Original Exercise 2 tests
│   └── test_truncate_number_spec_guided.py # NEW: Spec-guided tests (Part 2)
├── specifications/
│   ├── is_prime_specs.py        # Documented formal specifications
│   └── truncate_number_specs.py # Documented formal specifications
├── coverage_reports/
│   ├── spec_guided_html/        # HTML coverage report (spec-guided)
│   └── spec_guided_coverage.xml # XML coverage data (spec-guided)
├── run_coverage.sh              # Automated coverage measurement script
└── README.md                    # This file
```

## Quick Start

### Prerequisites
```bash
pip install pytest pytest-cov
```

### Run All Tests
```bash
pytest tests/ -v
```

### Generate Coverage Reports
```bash
./run_coverage.sh
```

## Viewing Coverage Reports

### HTML Reports (Recommended)

Open in a browser:
```bash
firefox coverage_reports/spec_guided_html/index.html
```

Or use any browser to open the `index.html` files.

### XML Reports

For programmatic access or CI/CD integration:
```
coverage_reports/spec_guided_coverage.xml
```