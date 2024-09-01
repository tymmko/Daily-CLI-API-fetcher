'''
Module for fetching tasks from API via clockify
'''
import requests
import json
import yaml

with open('configuration/config.yml', 'r') as file:
    config = yaml.safe_load(file)

def get_workspaces(api_key: str) -> list[dict]:
    '''
    Workspace id getter from API.
    '''
    url = "https://api.clockify.me/api/v1/workspaces"
    return requests.get(url, headers=config['HEADER']).json()

def get_projects(api_key: str, workspace_id: str) -> list[dict]:
    '''
    Projects id getter from API.
    '''
    url = f"https://api.clockify.me/api/v1/workspaces/{workspace_id}/projects"
    return requests.get(url, headers=config['HEADER']).json()

def main() -> str:
    '''
    Main function
    '''
    workspaces = get_workspaces(config['API_KEY'])
    if not workspaces:
        raise Exception("No workspaces found for this API key.")
    workspace_id = workspaces[0]["id"]

    projects = get_projects(config['API_KEY'], workspace_id)
    if not projects:
        raise Exception("No projects found in the workspace.")
    project_id = projects[0]["id"]

    url = f"https://api.clockify.me/api/v1/workspaces/{workspace_id}/projects/{project_id}/tasks"
    
    response = requests.get(url, headers=config['HEADER'])
    response.raise_for_status() 
    time_entries = response.json()

    return json.dumps(time_entries, indent = 3, ensure_ascii=False)

if __name__ == "__main__":
    main()
