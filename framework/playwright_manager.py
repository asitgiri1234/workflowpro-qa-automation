from playwright.sync_api import sync_playwright
from utils.config import Config

class PlaywrightManager:
    """
    Manages Playwright browser instances based on configuration.
    """

    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = None

    def start_browser(self):
        if Config.BROWSER == "chromium":
            self.browser = self.playwright.chromium.launch(headless=Config.HEADLESS)
        elif Config.BROWSER == "firefox":
            self.browser = self.playwright.firefox.launch(headless=Config.HEADLESS)
        elif Config.BROWSER == "webkit":
            self.browser = self.playwright.webkit.launch(headless=Config.HEADLESS)
        return self.browser

    def stop_browser(self):
        if self.browser:
            self.browser.close()
        self.playwright.stop()
