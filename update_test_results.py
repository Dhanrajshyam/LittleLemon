import django
import os
import unittest
import markdown
from datetime import datetime
from io import StringIO
from unittest.runner import TextTestResult
from pathlib import Path
import math

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

# Django settings setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Littlelemon.settings")
django.setup()

# Test modules
TEST_CATEGORIES = {
    "Models": "Restaurant.tests.test_models",
    "Serializers": "Restaurant.tests.test_serializers",
    "Views": "Restaurant.tests.test_views",
}

# Test results file
TEST_RESULTS_FILE = "TEST_RESULTS.md"

# Function to run tests and capture results


def run_tests():
    test_summary = {category: [] for category in TEST_CATEGORIES}

    for category, test_module in TEST_CATEGORIES.items():
        try:
            suite = unittest.defaultTestLoader.loadTestsFromName(test_module)
            if suite.countTestCases() == 0:
                print(f"⚠ No test cases found in {test_module}")
                continue

            buffer = StringIO()
            runner = unittest.TextTestRunner(stream=buffer, verbosity=2)
            # result = runner.run(suite)

            for test_case in suite:
                if isinstance(test_case, unittest.TestSuite):
                    for test in test_case:
                        result = runner.run(test).wasSuccessful()
                        process_test_case(test, result, test_summary, category)
                else:
                    process_test_case(test_case, result,
                                      test_summary, category)

        except ModuleNotFoundError:
            print(f"❌ Error: Test module '{test_module}' not found.")

    return test_summary


def process_test_case(test, result, test_summary, category):
    """Extract test details and status."""
    test_name = test.id().split('.')[-1]
    doc = test.shortDescription() or "No description available"
    status = "✅PASS" if result == True else "❌FAIL"
    test_summary[category].append((test_name, doc, status))


# File where the SVG will be saved
SVG_FILE = "speedometer.svg"

def create_speedometer_svg(total, passed, failed):
    # Calculate percentage of passed tests
    percentage = (passed / total) * 100 if total > 0 else 0
    percentage = int(percentage)
    progress_size = 722
    progress = progress_size - (progress_size*percentage/100)

    # SVG template
    svg_content = f"""
    
  <svg width="250" height="250" viewBox="-31.25 -31.25 312.5 312.5" version="1.1" xmlns="http://www.w3.org/2000/svg" style="transform:rotate(-90deg)">
    <circle r="115" cx="125" cy="125" fill="transparent" stroke="#1d1f19" stroke-width="50"></circle>
    <circle r="115" cx="125" cy="125" stroke="#07bb67" stroke-width="31" stroke-linecap="butt" stroke-dashoffset="{progress}px" fill="transparent" stroke-dasharray="722px"></circle>
    <text x="52px" y="140px" fill="#07bb67" font-size="{progress_size/12}px" font-weight="bold" style="transform:rotate(90deg) translate(0px, -246px)">{percentage}%</text>
  </svg>
  
    """

    # Write the SVG content to a file
    with open(SVG_FILE, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())

    print(f"SVG speedometer created: {SVG_FILE}")

# Function to update TEST_RESULTS.md


def update_test_results(test_summary):
    """Update TEST_RESULTS.md dynamically with progress meter."""
    total_tests = sum(len(tests) for tests in test_summary.values())
    passed_tests = sum(1 for tests in test_summary.values() for _, _, status in tests if status == "✅PASS")
    failed_tests = total_tests - passed_tests

    percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    percentage = int(percentage)
    create_speedometer_svg(total_tests, passed_tests, failed_tests)
    
    markdown_content = f"""
# 🛠 Django Test Results

![Overall Status](https://github.com/Dhanrajshyam/LittleLemon/actions/workflows/test.yml/badge.svg)

This file documents all the test cases executed in the Django project and their latest execution status in GitHub Actions.

---

### 📝 Test Progress

![Test Speedometer](speedometer.svg)

---

### 📝 Test Case Summary
#### ![Test Coverage](https://img.shields.io/badge/Tests-✅_{percentage}%25_Passed-green)

- **Total Test Cases:** 🧪 `{total_tests}`
- **Passed:** ✅ `{passed_tests}`
- **Failed:** ❌ `{failed_tests}`


            """
    for category, tests in test_summary.items():
        markdown_content += f"\n#### {category}\n"
        markdown_content += "| Test Case | Description | Status |\n"
        markdown_content += "| --------- | ----------- | ------ |\n"
        for test_name, doc, status in tests:
            markdown_content += f"| `{test_name}` | {doc} | {status} |\n"

    markdown_content += f"""

**Legend**: ✅ = Pass, ❌ = Fail

This summary updates automatically based on test runs.

---

## 🔍 View Complete Test Logs:
[GitHub Actions Test Logs](https://github.com/Dhanrajshyam/LittleLemon/actions/workflows/test.yml)

---

## ✅ **How to Run Tests Locally**
Run the following command in your terminal to execute tests:
```bash
python manage.py test --keepdb
```
---

## 📢 How to Integrate This in Your Git Repo

Copy this file as `TEST_RESULTS.md` and place it in your repository root.

Commit & Push the file:
```bash
git add TEST_RESULTS.md
git commit -m "Added test results markdown file"
git push origin main
```

"""
    if os.getenv('GITHUB_ACTIONS'): 
        with open(TEST_RESULTS_FILE, "w+", encoding="utf-8") as f:
            f.write(markdown_content.strip())
    else:
        with open('TEST_RESULTS.md', "w+", encoding="utf-8") as f:
            f.write(markdown_content.strip())

# Main function to execute the script
def main():
    test_summary = run_tests()
    update_test_results(test_summary)
    print("✅ TEST_RESULTS.md updated successfully!")


if __name__ == "__main__":
    main()
