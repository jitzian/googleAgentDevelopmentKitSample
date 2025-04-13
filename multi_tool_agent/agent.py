import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent



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


root_agent = Agent(
    name="family_member_agent",
    model="gemini-2.0-flash-exp",
    description=(
        "Agent to answer questions about the family members."
    ),
    instruction=(
        "I can answer your questions about the family members."
    ),
    tools=[check_name, check_gender],
)
