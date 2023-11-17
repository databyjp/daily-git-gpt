# DailyGitGPT: AI-Powered Summaries for Git Workflows

## Overview

DailyGitGPT enhances your Git workflow by automating the creation of GitHub issues and related pull requests (PRs) for changes made on a specified branch. Leveraging Large Language Models (LLMs), specifically GPT-3.5, it generates concise, intelligent summaries of code diffs, streamlining the process of documenting and tracking changes.

## Features

- **Branch-Specific Automation**: Targets a user-specified Git branch for processing.
- **Automated Issue and PR Creation**: Generates GitHub issues and PRs, complete with AI-generated summaries.
- **GPT-3.5 Integration**: Utilizes GPT-3.5 to create informative summaries of Git changes.
- **Customizable Issue and PR Templates**: Tailor templates to fit project-specific needs.
- **Environment Variable Configuration**: Leverages environment variables for easy setup and configuration.

## Tooling Stack

- **Git**: Manages local repository changes.
- **GitHub API**: Interacts with GitHub for issue and PR creation.
- **Python**: For scripting and API interactions.
- **PyGitHub**: Facilitates GitHub API interactions.
- **GitPython**: Interacts with Git.
- **OpenAI API**: Accesses the GPT-3.5 model for summary generation.

## Prerequisites

- Git installed on your machine.
- Python (version 3.6 or later).
- GitHub account with local Git credentials configured.
- OpenAI API key for GPT-3.5 access.
- Set environment variables: `GITHUB_TOKEN`, `GH_EMAIL`, `MAIN_REPO`, and `MAIN_REPO_LOC`.

## Setup and Configuration

1. **Clone the Repository**:
    ```
    git clone [URL of the DailyGitGPT repository]
    ```

2. **Install Dependencies**:
    ```
    pip install -r requirements.txt
    ```

3. **Configure Environment Variables**:
   - `GITHUB_TOKEN`: Your GitHub personal access token.
   - `GH_EMAIL`: Your GitHub email address.
   - `MAIN_REPO`: Your main repository in the format `username/repo`.
   - `MAIN_REPO_LOC`: Local path to your main repository.

## Usage

1. **Execute the Tool**:
    ```
    python main.py --branch <branch-name>
    ```
   Replace `<branch-name>` with the name of the branch you want to process.

## GitHub Credential Utilization

- Utilizes the existing Git configuration on your machine for GitHub actions.
- Ensure Git is set up with GitHub credentials for seamless operation.

## Contributing

TBC

## License

TBC

**Additional Information**:

- The tool assumes your Git environment is configured for GitHub access, simplifying setup and usage.
- Detailed instructions are provided for setting up necessary OpenAI API keys, focusing on security and user-friendliness.