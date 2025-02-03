import django
import os
import unittest
import markdown
from datetime import datetime
from io import StringIO
from unittest.runner import TextTestResult

# Django settings setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LittleLemon.settings")
django.setup()

# Test directories
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
        suite = unittest.defaultTestLoader.loadTestsFromName(test_module)
        buffer = StringIO()
        runner = unittest.TextTestRunner(stream=buffer, verbosity=2)
        result = runner.run(suite)

        for test_case in suite:
            test_name = test_case._testMethodName
            doc = test_case.shortDescription() or "No description available"
            status = "✅" if test_name in [
                t._testMethodName for t in result.successes] else "❌"
            test_summary[category].append((test_name, doc, status))

    return test_summary

# Function to update TEST_RESULTS.md


def update_test_results(test_summary):
    markdown_content = f"""
            # 🛠 Django Test Results

            ![Django Tests](https://github.com/Dhanrajshyam/LittleLemon/actions/workflows/test.yml/badge.svg)

            This file documents all the test cases executed in the Django project and their latest execution status in GitHub Actions.

            ---

            ## ✅ **How to Run Tests Locally**
            Run the following command in your terminal to execute tests:
            ```bash
            python manage.py test --keepdb
            ```
            ---

            ### 📝 Test Case Summary

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

            ## 📌 GitHub Actions Status

            ## 📊 Latest Test Execution Status:

            ## 🔍 View Complete Test Logs:
            [GitHub Actions Test Logs](https://github.com/Dhanrajshyam/LittleLemon/actions/workflows/test.yml)

            ## 📢 How to Integrate This in Your Git Repo

            Copy this file as `TEST_RESULTS.md` and place it in your repository root.

            Commit & Push the file:
            ```bash
            git add TEST_RESULTS.md
            git commit -m "Added test results markdown file"
            git push origin main
            ```

            """
    with open(TEST_RESULTS_FILE, "w", encoding="utf-8") as f:
        f.write(markdown_content.strip())


# Main function to execute the script
def main():
    test_summary = run_tests() 
    update_test_results(test_summary) 
    print("✅ TEST_RESULTS.md updated successfully!")

if __name__ == "__main__":
    main()
