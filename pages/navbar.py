from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class Navbar(BaseDriver):
    # Locators
    # ---- BUTTONS ----
    LOGIN_BUTTON = [By.XPATH, "//span[text()='Giriş Yap']"]
    MY_CART_BUTTON = [By.XPATH, "//*[text()='Sepetim']"]

    # ---- INPUTS ----
    SEARCH_INPUT = [By.ID, "search-form__input-field__search-input"]

    # ---- TEXTS ----
    MY_CART_BADGE = [By.XPATH, "//*[text()='Sepetim']/following-sibling::span"]

    def __init__(self, driver):
        super().__init__(driver)
        self.log = self.custom_logger()

    # Actions
    def ACT_GOTO_CART(self):
        self.find_and_click(self.MY_CART_BUTTON)
        self.assert_current_url("sepetim")
        self.log.info("Navigating to my cart section.")

    def ACT_GOTO_SEARCH_PRODUCT(self, product_name):
        self.find_and_send(self.SEARCH_INPUT, product_name)
        self.find_and_send(self.SEARCH_INPUT, Keys.ENTER)
        self.log.info("Searched for \"" + product_name + "\"")

    def ACT_MOUSEOVER_A_CATEGORY_AND_CLICK_ON_A_PRODUCT(self, category, product):
        self.find_and_mouseover(self.create_an_element_by_link(category))
        self.log.info("Mouse overed on to " + category + ".")
        self.wait_until_dropdown_visible()
        self.find_and_click(self.create_an_element_by_link(product))
        self.log.info("Clicked to " + product + " link.")

    def wait_until_dropdown_visible(self):
        self.wait_until_visibility_of_element([By.CSS_SELECTOR, "[class='menu-header-item menu-header-item--active ']"])
