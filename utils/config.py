import os

class Config:
    """
    Central configuration management for the test framework.
    Values can be overridden using environment variables.
    """

    ENVIRONMENT = os.getenv("ENV", "test")

    BASE_WEB_URL = os.getenv("BASE_WEB_URL", "https://app.workflowpro.com")
    BASE_API_URL = os.getenv("BASE_API_URL", "https://api.workflowpro.com")

    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

    DEFAULT_TENANT = os.getenv("TENANT", "company1")
