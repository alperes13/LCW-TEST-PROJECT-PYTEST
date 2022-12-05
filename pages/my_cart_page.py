from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class MyCartPage(BaseDriver):
    # Locators
    # ---- TEXTS ----
    PRODUCT_QUANTITY_IN_MY_CART = [By.CSS_SELECTOR, "[class='col-md-12 cart-header mb-20'] span"]

    def __init__(self, driver):
        super().__init__(driver)
        self.log = self.custom_logger()

    # Actions
    def ACT_GET_PRODUCT_QUANTITY(self):
        self.assert_current_url("sepetim")
        self.log.info("Navigated to my cart page.")
        products_quantity_text = self.get_element_text(self.PRODUCT_QUANTITY_IN_MY_CART)
        products_quantity = products_quantity_text[
                            products_quantity_text.index("(") + 1: products_quantity_text.rindex(" ")]

        self.log.info(products_quantity + " product in the cart.")
        return products_quantity
