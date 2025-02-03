import os
import re
import requests

# GitHub repository details
repo = "Dhanrajshyam/LittleLemon"
workflow_run_url = "https://api.github.com/repos/{}/actions/runs".format(repo)
latest_run = requests.get(workflow_run_url).json()['workflow_runs'][0]

# Get the latest workflow run ID
run_id = latest_run['id']

# Fetch test results from the latest run
job_url = f"https://api.github.com/repos/{repo}/actions/runs/{run_id}/jobs"
jobs = requests.get(job_url).json()

# Extract the test logs (you'll need to find the correct job name for your test job)
for job in jobs['jobs']:
    if job['name'] == 'test':  # Replace 'test' with your actual test job name
        test_log_url = job['steps'][0]['logs_url']
        test_log = requests.get(test_log_url).json()['logs']
        
        # Parse the test results from the logs
        passed_tests = []
        failed_tests = []
        
        for line in test_log:
            if 'PASSED' in line:
                passed_tests.append(line.strip())
            elif 'FAILED' in line:
                failed_tests.append(line.strip())
        
        # Update the markdown file with the test results
        with open('TEST_RESULTS.md', 'r') as file:
            md_content = file.read()
        
        # Update the markdown content with dynamic results
        md_content = re.sub(r'(?<=Models\n)(.|\n)*?(?=Serializers)', '', md_content)
        md_content = md_content.replace("Models", "Models\n" + "\n".join(passed_tests))
        md_content = md_content.replace("Serializers", "Serializers\n" + "\n".join(failed_tests))

        # Write back the updated markdown content
        with open('TEST_RESULTS.md', 'w') as file:
            file.write(md_content)

