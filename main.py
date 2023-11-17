import os
import argparse
from git import Repo
from datetime import datetime, timedelta
from openai import OpenAI
from github import Github, GithubException

# Initialize GitHub API client
github_token = os.getenv('GITHUB_TOKEN')
GH_EMAIL = os.environ["GH_EMAIL"]
REPO_NAME = os.environ["MAIN_REPO"]
REPO_LOC = os.environ["MAIN_REPO_LOC"]
g = Github(github_token)


def get_git_changes(branch_name, author_email=GH_EMAIL, base_branch="main", days_back=2):
    """
    Function to get changes from the specified Git branch within the last N days.
    """
    repo = Repo(REPO_LOC)  # Adjust the path to your repository
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


def create_github_pr(branch_name, summary='-'):
    """
    Function to create a pull request on GitHub.
    """
    repo = g.get_repo(REPO_NAME)
    try:
        pr = repo.create_pull(base="main",
                              head=branch_name,
                              title=f"PR: {branch_name}",
                              body=summary)
        return pr
    except GithubException as e:
        print(f"Error creating PR: {e}")
        return None


def create_github_issue(branch_name, summary, pr_link):
    """
    Function to create an issue on GitHub with a link to the PR.
    """
    repo = g.get_repo(REPO_NAME)
    try:
        issue = repo.create_issue(title=f"Issue for {branch_name} changes", body=f"{summary}\n\nRelated PR: {pr_link}")
        return issue
    except GithubException as e:
        print(f"Error creating issue: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(description='DailyGitGPT: AI-Powered Git Summaries.')
    parser.add_argument('--branch', type=str, help='Name of the branch to process.')
    args = parser.parse_args()

    if args.branch:
        changes = get_git_changes(args.branch)
        summary = generate_summary(changes)

        # Create PR
        pr = create_github_pr(branch_name=args.branch, summary=summary)

        if pr:
            # Create Issue with link to PR
            issue = create_github_issue(branch_name=args.branch, summary=summary, pr_link=pr.html_url)

            if issue:
                # Add a comment to PR with a link to the issue
                pr.create_issue_comment(f"Related issue: {issue.html_url}")

    else:
        print("Please specify a branch name using --branch <branch-name>.")


if __name__ == "__main__":
    main()
