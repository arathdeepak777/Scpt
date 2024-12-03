def create_merge_request(project_id, source_branch, destination_branch):
    """Creates a merge request from source_branch to destination_branch"""
    url = f"{GITLAB_URL}/api/v4/projects/{project_id}/merge_requests"
    data = {
        'source_branch': source_branch,
        'target_branch': destination_branch,
        'title': f"Merge {source_branch} into {destination_branch}",
        'squash': False,  # Disable squash merge
    }

    # Make the API request to create the merge request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        print(f"Merge request created successfully for {project_id}.")
    else:
        print(f"Failed to create merge request for {project_id}: {response.status_code}, {response.text}")
