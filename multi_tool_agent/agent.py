from datetime import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from typing import List

from .domain.repository.RepositoriesImpl import RepositoriesImpl
from .controller.GitHubController import GitHubController
from .constants import global_constants
from .domain.model.GitHubRepo import GitHubRepo
from .agent_descriptions.agent_repositories_description import github_repositories_description

names = ["anne", "phil","morgan","matthew","john", "mathilda"]

def check_name(name: str) -> dict:

    """
    Checks if a name is available.

    Args:
        name (str): The name to check.

    Returns:
        dict: status and result or error msg.
    """


    if name.lower() in names:
        return {
            "status": "success", 
            "report": f"{name} is available."
        }
    else:
        return {
            "status": "error", 
            "error_message": f"{name} is not available."
        }

def check_gender(name: str) -> dict:
    """
    Checks the gender of a name.

    Args:
        name (str): The name to check.

    Returns:
        dict: status and result or error msg.
    """

    if name.lower() == "anne" or name.lower() == "mathilda"or name.lower() == "morgan":
        return {
            "status": "success", 
            "report": f"{name} is female."
        }
    elif name.lower() == "phil" or  name.lower() == "matthew" or name.lower() == "john":
        return {
            "status": "success", 
            "report": f"{name} is male."
        }
    else:
        return {
            "status": "error", 
            "error_message": f"{name} is not available."
        }

def get_repositories(user: str) -> dict:
    repository = RepositoriesImpl([])  # Initialize with empty list
    controller = GitHubController(repository)
    result_repos = []
    
    # Get repositories for the user
    repos = controller.get_user_repositories(user)
    if repos:
        result_repos.extend(repos)

    language_type = analyze_repositories(result_repos)

    return {
        "status": "success",
        "report": language_type
    }
        
def analyze_repositories(result_repos: List[GitHubRepo]) -> dict:
    language_type = {
        "python": 0,
        "kotlin": 0,
        "java": 0,
    }
    if result_repos:  # Changed from 'is not empty' to proper Python syntax
        for repo in result_repos:
            if repo.language and repo.language.lower() in language_type:  # Added .lower() for case insensitive comparison
                language_type[repo.language.lower()] += 1
    return language_type




root_agent = Agent(
    name="family_member_agent",
    model="gemini-2.0-flash-exp",
    description = github_repositories_description,
    instruction = (
        "Search in the repositories the type of language used in them"
    ),
    tools=[get_repositories],
)
