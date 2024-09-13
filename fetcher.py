'''
Module for fetching time entries from API via Clockify.
'''
import json
import requests
import yaml

with open('configuration/config.yml', 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)

HEADER = {'X-Api-Key': config['API_KEY']}

def get_workspaces() -> list[dict]:
    '''
    Workspace id getter from API.
    '''
    url = "https://api.clockify.me/api/v1/workspaces"
    return requests.get(url, headers = HEADER, timeout = 10).json()

def get_time_entries(workspace_id: str, user_id: str) -> list[dict]:
    '''
    Time entries getter from the Clockify API for a specific workspace.
    '''
    url = f"https://api.clockify.me/api/v1/workspaces/{workspace_id}/user/{user_id}/time-entries"
    return requests.get(url, headers = HEADER, timeout = 10).json()

def get_projects(workspace_id: str) -> list[dict]:
    '''
    Projects id getter from API.
    '''
    url = f"https://api.clockify.me/api/v1/workspaces/{workspace_id}/projects"
    return requests.get(url, headers = HEADER, timeout = 10).json()

def convert_id_to_name(json_tasks: list, workspace_id: str, project_id: str) -> str:
    '''
    A function to parse name of tasks via corresponding id.
    '''
    url = f'https://api.clockify.me/api/v1/workspaces/{workspace_id}/projects/{project_id}/tasks/'
    response = requests.get(url, headers=HEADER, timeout=10)
    for task in json_tasks:
        tasks_info = response.json()
        task_lookup = {task["id"]: task["name"] for task in tasks_info}
        for record in json_tasks:
            task_id = record.get("taskId")
            if task_id in task_lookup:
                record["name"] = task_lookup[task_id]

def main() -> str:
    '''
    Main function to fetch time entries.
    '''
    workspaces = get_workspaces()
    if not workspaces:
        raise Exception("No workspaces found for this API key.")
    workspace_id = workspaces[0]["id"]
    user_id = workspaces[0]['memberships'][0]['userId']

    projects = get_projects(workspace_id)
    if not projects:
        raise Exception("No projects found in the workspace.")
    project_id = projects[0]["id"]

    time_entries = get_time_entries(workspace_id, user_id)
    if not time_entries:
        raise Exception("No time entries found in the workspace.")

    convert_id_to_name(time_entries, workspace_id, project_id)
    return json.dumps(time_entries, indent=3, ensure_ascii=False)

if __name__ == "__main__":
    main()
