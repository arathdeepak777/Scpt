def create_merge_request(project_id, source_branch, destination_branch):
    """Creates a merge request from source_branch to destination_branch"""
    url = f"{GITLAB_URL}/api/v4/projects/{project_id}/merge_requests"
    data = {
        'source_branch': source_branch,
        'target_branch': destination_branch,
        'title': f"Merge {source_branch} into {destination_branch}",
        'squash': False,  # Disable squash merge
    }
