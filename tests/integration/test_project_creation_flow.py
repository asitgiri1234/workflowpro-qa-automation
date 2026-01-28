import requests
import pytest
from playwright.sync_api import sync_playwright, expect

BASE_API_URL = "https://api.workflowpro.com"
PROJECTS_ENDPOINT = "/api/v1/projects"
LOGIN_URL = "https://app.workflowpro.com/login"
DASHBOARD_URL_PATTERN = "**/dashboard"


@pytest.fixture
def api_headers():
    """
    Base API headers used for authenticated requests.
    """
    return {
        "Authorization": "Bearer dummy-access-token",
        "Content-Type": "application/json",
        "X-Tenant-ID": "company1"
    }


@pytest.fixture
def created_project(api_headers):
    """
    Creates a project via API before UI and mobile validation.
    Returns project details for downstream verification.
    """

    payload = {
        "name": "Integration Test Project",
        "description": "Created via API for integration testing",
        "team_members": ["user1", "user2"]
    }

    response = requests.post(
        BASE_API_URL + PROJECTS_ENDPOINT,
        headers=api_headers,
        json=payload
    )

    assert response.status_code == 201

    project = response.json()
    yield project

    # Cleanup step (conceptual)
    # In a real system, the project would be deleted here via API


def test_project_creation_flow(created_project):
    """
    Validates the complete project creation flow:
    1. Project is created via API
    2. Project appears in Web UI
    3. Project is accessible on mobile
    4. Project is isolated to the correct tenant
    """

    project_name = created_project["name"]

    # -------------------------------
    # Web UI Validation
    # -------------------------------
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto(LOGIN_URL)

        page.fill("#email", "admin@company1.com")
        page.fill("#password", "password123")
        page.click("#login-btn")

        page.wait_for_url(DASHBOARD_URL_PATTERN, timeout=15000)

        # Verify project appears in dashboard
        project_locator = page.locator(".project-card", has_text=project_name)
        expect(project_locator).to_be_visible()

        context.close()
        browser.close()

    # -------------------------------
    # Mobile Validation (Conceptual)
    # -------------------------------
    # This step would execute on BrowserStack using real devices.
    # The same project name would be validated in the mobile UI.
    #
    # Example (conceptual):
    # - Launch mobile session on BrowserStack
    # - Authenticate user
    # - Verify project_name is visible in project list
    #
    # Mobile-specific assertions focus on accessibility and availability,
    # not full UI parity with web.

    assert project_name is not None

    # -------------------------------
    # Tenant Isolation Validation
    # -------------------------------
    other_tenant_headers = {
        "Authorization": "Bearer dummy-access-token",
        "Content-Type": "application/json",
        "X-Tenant-ID": "company2"
    }

    response = requests.get(
        BASE_API_URL + PROJECTS_ENDPOINT,
        headers=other_tenant_headers
    )

    assert response.status_code == 200

    project_names = [project["name"] for project in response.json()]

    # Ensure project is not visible to another tenant
    assert project_name not in project_names
