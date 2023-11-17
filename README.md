## DailyGitGPT: AI-Powered Summaries for Git Workflows

## Overview

DailyGitGPT is designed to enhance your Git workflow. It automates the creation of GitHub issues and related pull requests (PRs) for changes made on a specified branch, utilizing LLMs to generate concise, intelligent summaries of code diffs.

## Features

- **Branch-Specific Automation**: Targets a user-specified Git branch for processing.
- **Automated Issue and PR Creation**: Streamlines the process of generating GitHub issues and PRs.
- **GPT-3.5 Integration**: Employs GPT-3.5 for generating clear, informative summaries of changes.
- **Customizable Issue and PR Templates**: Allows for tailored templates to suit project needs.

## Tooling Stack

- **Git**: For managing local repository changes.
- **GitHub API**: For interaction with GitHub to create issues and PRs.
- **Python**: Scripting language of choice for its simplicity and versatility.
- **PyGitHub**: Python library to facilitate GitHub API interactions.
- **GitPython**: Python library to interact with git.
- **OpenAI API**: Accessing the GPT-3.5 model for summary generation.

## Prerequisites

- Git installed on your machine.
- Python (version 3.6 or later).
- A GitHub account with configured local Git credentials.
- An OpenAI API key for GPT-3.5 access.

## Setup and Configuration

1. **Clone the Repository**:

    ```other
    git clone [URL of the DailyGitGPT repository]
    ```

2. **Install Dependencies**:

    ```other
    pip install -r requirements.txt
    ```

3. **Set Up OpenAI API Key**:
	- Define your OpenAI API key in an environment variable named `OPENAI_API_KEY`.

## Usage

1. **Execute the Tool**:

    ```other
    python main.py --branch <branch-name>
    ```

2. **Template Customization**:
	- Modify the templates in the `templates` folder to suit your project's style and requirements.

## GitHub Credential Utilization

- DailyGitGPT leverages the existing Git configuration on your machine for GitHub actions.
- Ensure your Git is set up with your GitHub credentials for smooth operation.

## Contributing


We encourage contributions to DailyGitGPT. For guidelines on contributing, please see `CONTRIBUTING.md`.

## License


DailyGitGPT is licensed under [LICENSE NAME]. For more details, refer to the `LICENSE` file.
----

**Additional Information**:


- The tool assumes your Git environment is already configured for GitHub access, simplifying setup and usage.
- Instructions are provided for setting up the necessary OpenAI API key, focusing on security and user-friendliness.
