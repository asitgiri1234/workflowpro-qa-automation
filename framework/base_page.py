class BasePage:
    """
    Base page object providing common UI actions.
    """

    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)
