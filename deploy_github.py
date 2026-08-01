"""
GitHub Deployment Automation Script for srinivasgangumalla12/crop-disease-detection.
"""

import subprocess
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
USERNAME = "srinivasgangumalla12"
REPO_NAME = "crop-disease-detection"
REMOTE_URL = f"https://github.com/{USERNAME}/{REPO_NAME}.git"

def run_cmd(cmd, cwd=REPO_DIR):
    print(f"Executing: {cmd}")
    res = subprocess.run(cmd, shell=True, cwd=cwd, text=True, capture_output=True)
    if res.stdout:
        print(res.stdout)
    if res.stderr and res.returncode != 0:
        print("Error:", res.stderr)
    return res.returncode

def deploy():
    print("Starting GitHub Deployment...")
    run_cmd("git init")
    run_cmd(f'git config user.name "{USERNAME}"')
    run_cmd(f'git config user.email "srinivasgangumalla12@gmail.com"')
    run_cmd("git branch -M main")
    run_cmd("git add .")
    run_cmd('git commit -m "Deploy FARMERS SOLUTION - Crop Disease Detection & Agricultural Weather Advisory System"')
    
    # Configure clean remote
    run_cmd("git remote remove origin")
    run_cmd(f"git remote add origin {REMOTE_URL}")
    
    print("\nPushing to GitHub repo...")
    ret = run_cmd("git push -u origin main --force")
    if ret == 0:
        print(f"\nSUCCESS! Project successfully deployed to https://github.com/{USERNAME}/{REPO_NAME}")
    else:
        print("\nNote: Make sure repository 'crop-disease-detection' is created on GitHub at https://github.com/new")

if __name__ == "__main__":
    deploy()
