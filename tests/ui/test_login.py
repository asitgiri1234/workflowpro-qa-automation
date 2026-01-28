import pytest
from playwright.sync_api import sync_playwright, expect

LOGIN_URL = "https://app.workflowpro.com/login"
DASHBOARD_URL_PATTERN = "**/dashboard"


@pytest.fixture(scope="function")
def browser_context():
    """
    Creates a new isolated browser context for each test.
    This prevents state leakage between tests.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


def test_user_login_success(browser_context):
    """
    Verifies that a valid user can successfully log in
    and reach the dashboard.
    """

    page = browser_context

    page.goto(LOGIN_URL)

    page.fill("#email", "admin@company1.com")
    page.fill("#password", "password123")
    page.click("#login-btn")

    # Wait for navigation to complete
    page.wait_for_url(DASHBOARD_URL_PATTERN, timeout=15000)

    # Verify dashboard is loaded
    expect(page.locator(".welcome-message")).to_be_visible()


def test_login_invalid_credentials(browser_context):
    """
    Ensures that login fails gracefully with invalid credentials.
    """

    page = browser_context

    page.goto(LOGIN_URL)

    page.fill("#email", "invalid@company1.com")
    page.fill("#password", "wrongpassword")
    page.click("#login-btn")

    # Verify error message is displayed
    expect(page.locator(".error-message")).to_be_visible()
