import os
import argparse
from github import Github
from git import Repo
from datetime import datetime, timedelta
from openai import OpenAI

def get_git_changes(branch_name, author_email="me@jphwang.com", base_branch="main", days_back=2):
    """
    Function to get changes from the specified Git branch within the last N days.
    """
    repo = Repo('/Users/jphwang/code/weaviate-io')  # Adjust the path to your repository
    branch = repo.branches[branch_name]

    # Calculate the date N days ago
    date_N_days_ago = datetime.now() - timedelta(days=days_back)

    # Get the base commit from the main branch
    base_commit = repo.commit(base_branch)

    # Filter commits in the branch from the last N days
    commits = list(repo.iter_commits(branch, since=date_N_days_ago.isoformat(), author=author_email))

    # Get diffs from these commits
    diffs = []
    for commit in commits:
        diff = base_commit.diff(commit, create_patch=True)
        for patch in diff:
            diffs.append(patch.diff.decode('utf-8'))

    return '\n'.join(diffs)


def generate_summary(changes):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"""
                Write a very short summary for the following git diff 
                that would be suitable as a body of the commit message :\n{changes}
            """}
        ]
    )

    return completion.choices[0].message.content


# MAYBE TODO: Function to create a PR, and an accompanying GH issue.


def main():
    parser = argparse.ArgumentParser(description='DailyGitGPT: AI-Powered Git Summaries.')
    parser.add_argument('--branch', type=str, help='Name of the branch to process.')
    args = parser.parse_args()

    if args.branch:
        changes = get_git_changes(args.branch)
        summary = generate_summary(changes)
        print(summary)
    else:
        print("Please specify a branch name using --branch <branch-name>.")


if __name__ == "__main__":
    main()
