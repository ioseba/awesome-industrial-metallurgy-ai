import os
import subprocess

repo_dir = r"C:\Users\ioseb\awesome_repo_build"
os.chdir(repo_dir)

# Create a clean orphan branch to squash into a clean initial commit with author ioseba
subprocess.run(["git", "checkout", "--orphan", "clean_main"], check=True)
subprocess.run(["git", "add", "-A"], check=True)

env = os.environ.copy()
env["GIT_AUTHOR_NAME"] = "ioseba"
env["GIT_AUTHOR_EMAIL"] = "iosebaalonso@gmail.com"
env["GIT_COMMITTER_NAME"] = "ioseba"
env["GIT_COMMITTER_EMAIL"] = "iosebaalonso@gmail.com"

subprocess.run([
    "git", "commit", "-m", "feat: initial release of awesome-industrial-metallurgy-ai curated ecosystem"
], env=env, check=True)

subprocess.run(["git", "branch", "-D", "main"], check=True)
subprocess.run(["git", "branch", "-m", "main"], check=True)

token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
url = f"https://ioseba:{token}@github.com/ioseba/awesome-industrial-metallurgy-ai.git"
subprocess.run(["git", "push", url, "main", "--force"], check=True)
print("Successfully reset history and pushed with author ioseba!")
