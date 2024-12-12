import requests

# GitLab personal access token with admin permissions
GITLAB_API_TOKEN = 'your_gitlab_api_token_here'

# Base URL for your GitLab instance
GITLAB_URL = 'https://gitlab.com'  # Change to your GitLab server if not using gitlab.com

# Dictionary containing repository names and PAT tokens
repos_and_tokens = {
    "repository_name1": "pat_token1",
    "repository_name2": "pat_token2"
    # Add more repositories and PAT tokens as needed
}

# Header for API requests
headers = {
    'PRIVATE-TOKEN': GITLAB_API_TOKEN
}

def create_ci_cd_variable(repo_name, pat_token):
    """
    Create a masked CI/CD variable for a given repository.

    Args:
        repo_name (str): Name of the repository.
        pat_token (str): Personal Access Token (PAT) to be set as a CI/CD variable.

    Returns:
        None
    """
    # Fetch the project ID based on repository name
    project_url = f'{GITLAB_URL}/api/v4/projects/{repo_name}'
    response = requests.get(project_url, headers=headers)

    if response.status_code == 404:
        print(f"Error: Repository '{repo_name}' not found.")
        return

    project_data = response.json()
    project_id = project_data['id']

    # Define the variable name and value
    variable_name = 'CI_PAT_TOKEN'  # You can change the name as needed
    variable_value = pat_token

    # API endpoint to create a CI/CD variable
    variables_url = f'{GITLAB_URL}/api/v4/projects/{project_id}/variables'

    # Create the data payload for the variable
    variable_data = {
        'key': variable_name,
        'value': variable_value,
        'masked': True  # Mask the token in CI/CD logs
    }

    # Send the request to create the variable
    response = requests.post(variables_url, headers=headers, data=variable_data)

    if response.status_code == 201:
        print(f"CI/CD variable '{variable_name}' created successfully for repository '{repo_name}'.")
    else:
        print(f"Error creating variable for repository '{repo_name}': {response.text}")

def main():
    """
    Main function to create variables for all repositories in the dictionary.
    """
    for repo_name, pat_token in repos_and_tokens.items():
        create_ci_cd_variable(repo_name, pat_token)

if __name__ == '__main__':
    main()
