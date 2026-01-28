import pytest
from playwright.sync_api import expect

DASHBOARD_URL = "https://app.workflowpro.com/dashboard"


def test_projects_visible_for_correct_tenant(browser_context):
    """
    Verifies that projects belonging to the logged-in tenant
    are visible on the dashboard.
    """

    page = browser_context

    # Assumption: user is already authenticated
    page.goto(DASHBOARD_URL)

    # Wait for project cards to load
    page.wait_for_selector(".project-card", timeout=15000)

    project_cards = page.locator(".project-card")

    # Ensure at least one project is visible
    expect(project_cards.first).to_be_visible()

    # Validate tenant-specific data
    for i in range(project_cards.count()):
        project_text = project_cards.nth(i).text_content()
        assert "Company1" in project_text


def test_projects_not_visible_for_other_tenant(browser_context):
    """
    Ensures that projects from another tenant are not visible
    to the currently logged-in user.
    """

    page = browser_context
    page.goto(DASHBOARD_URL)

    page.wait_for_selector(".project-card", timeout=15000)

    project_cards = page.locator(".project-card")

    for i in range(project_cards.count()):
        project_text = project_cards.nth(i).text_content()
        assert "Company2" not in project_text
