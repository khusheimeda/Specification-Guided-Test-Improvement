#!/bin/bash
# Script to measure coverage for Exercise 3 Part 2
# This script measures BASELINE coverage and SPEC-GUIDED coverage separately

set -e  # Exit on error

echo "================================================"
echo "Exercise 3 Part 2: Coverage Measurement"
echo "================================================"
echo ""

# Navigate to project directory
cd "$(dirname "$0")"

# Install dependencies if needed
echo "Installing dependencies..."
pip install pytest pytest-cov --break-system-packages -q

echo "================================================"
echo "SPEC-GUIDED COVERAGE (Baseline + Spec-guided tests)"
echo "================================================"
echo ""

# Run all tests (spec-guided)
pytest tests/ \
    --cov=problems \
    --cov-report=html:coverage_reports/spec_guided_html \
    --cov-report=xml:coverage_reports/spec_guided_coverage.xml \
    --cov-report=term \
    --cov-branch

echo ""
echo "Spec-guided coverage reports saved to:"
echo "  - coverage_reports/spec_guided_html/index.html"
echo "  - coverage_reports/spec_guided_coverage.xml"
echo ""

echo "================================================"
echo "COVERAGE MEASUREMENT COMPLETE"
echo "================================================"
echo ""
echo "To view HTML reports:"
echo "  firefox coverage_reports/spec_guided_html/index.html"
