import uuid

def generate_project_data():
    """
    Generates unique project data for tests.
    """
    return {
        "name": f"Test Project {uuid.uuid4().hex[:6]}",
        "description": "Auto-generated project for testing",
        "team_members": ["user1", "user2"]
    }
