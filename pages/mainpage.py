from base.base_driver import BaseDriver


class Mainpage(BaseDriver):
    # Locators
    # ---- LINK ----
    MAINPAGE_LINK = "https://www.lcwaikiki.com/tr-TR/TR"

    def __init__(self, driver):
        super().__init__(driver)
        self.log = self.custom_logger()

    # Actions
    def ACT_GOTO_MP(self):
        self.driver.get(self.MAINPAGE_LINK)
        self.assert_current_url(self.MAINPAGE_LINK)
        self.log.info("Navigated to mainpage.")
