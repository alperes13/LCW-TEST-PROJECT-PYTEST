from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class ProductPage(BaseDriver):
    # Locators
    # ---- BUTTONS ----
    ADD_TO_CART_BUTTON = [By.ID, "pd_add_to_cart"]
    PRODUCT_VARIATIONS = [By.XPATH, "//*[contains(@class, 'option') and (contains(@class, 'active') or contains(@class, 'disabled'))]"]

    # ---- TEXTS -----
    PRODUCT_CODE_LABEL = [By.CSS_SELECTOR, "[class='product-code'] span"]

    def __init__(self, driver):
        super().__init__(driver)
        self.log = self.custom_logger()

    # Actions
    def ACT_ADD_TO_CART(self):
        self.ACT_VALIDATE_PRODUCT_PAGE()
        self.ACT_CHOOSE_PRODUCT_VARIATON()
        self.log.info("Navigated to a product page.")
        self.find_and_click(self.ADD_TO_CART_BUTTON)
        self.log.info("Current product added to cart.")

    def ACT_CHOOSE_PRODUCT_VARIATON(self):
        self.find_and_click_random_element(self.PRODUCT_VARIATIONS)
        self.log.info("Chose random variation if it is exist.")

    def ACT_VALIDATE_PRODUCT_PAGE(self):
        self.assert_text_in_element(self.PRODUCT_CODE_LABEL, "ürün kodu")
