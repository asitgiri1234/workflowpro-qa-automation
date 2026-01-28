import requests
import pytest

BASE_API_URL = "https://api.workflowpro.com"
PROJECTS_ENDPOINT = "/api/v1/projects"

@pytest.fixture
def auth_headers():
    """
    Returns authentication headers for API requests.
    In a real implementation, the token would be generated dynamically
    or fetched from a secure secret store.
    """
    return {
        "Authorization": "Bearer dummy-access-token",
        "Content-Type": "application/json"
    }

@pytest.fixture
def tenant_headers(auth_headers):
    """
    Adds tenant-specific information to the request headers.
    """
    headers = auth_headers.copy()
    headers["X-Tenant-ID"] = "company1"
    return headers


def test_create_project_api(tenant_headers):
    """
    Validates that a project can be created successfully via API
    for a specific tenant.
    """

    payload = {
        "name": "Test Project",
        "description": "Project created via API automation test",
        "team_members": ["user1", "user2"]
    }

    response = requests.post(
        BASE_API_URL + PROJECTS_ENDPOINT,
        headers=tenant_headers,
        json=payload
    )

    # Validate response status
    assert response.status_code == 201

    response_body = response.json()

    # Validate response structure
    assert "id" in response_body
    assert response_body["name"] == payload["name"]
    assert response_body["status"] == "active"


def test_project_isolated_to_tenant(auth_headers):
    """
    Ensures that a project created for one tenant
    is not accessible from another tenant.
    """

    # Simulate another tenant
    other_tenant_headers = auth_headers.copy()
    other_tenant_headers["X-Tenant-ID"] = "company2"

    response = requests.get(
        BASE_API_URL + PROJECTS_ENDPOINT,
        headers=other_tenant_headers
    )

    assert response.status_code == 200

    project_names = [project["name"] for project in response.json()]

    # Ensure project from company1 is not visible to company2
    assert "Test Project" not in project_names
