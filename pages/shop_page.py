from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class ShopPage(BaseDriver):
    # Locators
    # ---- BUTTONS ----
    FILTER_XL_RADIO_BUTTON = [By.XPATH, "//span[text()='XL']/preceding-sibling::div"]
    CONTENT_DROPDOWN_BUTTON = [By.CLASS_NAME, "dropdown-button__button"]
    CONTENT_DROPDOWN_HIGH_PRICE_BUTTON = [By.XPATH, "//*[text()='En yüksek fiyat']"]
    CONTENT_DROPDOWN_LOW_PRICE_BUTTON = [By.XPATH, "//*[text()='En düşük fiyat']"]

    # ---- TEXTS ----
    HEADER_PRODUCT_NAME_TEXT = [By.XPATH, "//*[@class='container-fluid product-list-heading']//child::*[contains(@class,'product-list-heading__product-count__count') or contains(@class,'product-list-heading__heading')]"]
    ALL_PRODUCT_TITLES = [By.CLASS_NAME, "product-card__title"]
    ALL_PRODUCT_PRICES = [By.XPATH, "//*[@class='product-price__price product-price__price--only' or @class='product-price__cart-price' or @class='product-price__price']"]
    DROPDOWN_BUTTON_TEXT = [By.CLASS_NAME, "dropdown-button__text"]
    FILTER_PRODUCT_QUANTITIES_IN_PRODUCT_TYPE = [By.XPATH, "//div[text()='Ürün Tip']/following-sibling::div//div[@class='filter-option']//span[@class='filter-option__product-count']"]
    FILTER_APPLIED_FILTER_VALUE = [By.CLASS_NAME, "applied-filters__value"]
    PAGINATION_LISTED_PRODUCTS_COUNT_TEXT = [By.CLASS_NAME, "paginator__info-text-viewed-products"]
    PAGINATION_TOTAL_PRODUCTS_COUNT_TEXT = [By.CLASS_NAME, "paginator__info-text-product-count"]

    # ---- COMPONENTS ----
    PRODUCT_COMPONENT = [By.CLASS_NAME, "product-grid"]

    def __init__(self, driver):
        super().__init__(driver)
        self.log = self.custom_logger()

    # Actions
    def ACT_SORT_PRODUCT_FUNCTION(self, feature):
        self.find_and_click(self.CONTENT_DROPDOWN_BUTTON)
        self.log.info("Clicked to dropdown menu.")
        if feature.lower() == "highest":
            self.find_and_click(self.CONTENT_DROPDOWN_HIGH_PRICE_BUTTON)
            self.log.info("Clicked to highly price sorting method")
            self.assert_text_in_element(self.DROPDOWN_BUTTON_TEXT, "En yüksek fiyat")
            self.log.info("Products sorted for highly price")
        elif feature.lower() == "lowest":
            self.find_and_click(self.CONTENT_DROPDOWN_LOW_PRICE_BUTTON)
            self.log.info("Clicked to lowest price sorting method")
            self.assert_text_in_element(self.DROPDOWN_BUTTON_TEXT, "En düşük fiyat")
            self.log.info("Products sorted for lowest price")

    def ACT_FILTER_FOR_A_VARIATION(self, varitaion):
        element = ""
        if varitaion.lower() == "xl":
            element = self.FILTER_XL_RADIO_BUTTON
        self.find_and_click(element)
        self.log.info("Clicked to " + varitaion + " filter.")
        self.assert_text_in_element(self.FILTER_APPLIED_FILTER_VALUE, varitaion)
        self.log.info("Products filtered for " + varitaion + " variation.")

    def ACT_CLICK_ON_ANY_PRODUCT(self):
        self.log.info("Navigated to any shop page.")
        self.find_and_click_random_element(self.ALL_PRODUCT_TITLES)
        self.log.info("Clicked to any item in the shop page, navigating to chosen product page")

    def ACT_GET_PRODUCTS_COUNT(self):
        self.wait_until_visibility_of_all_elements(self.ALL_PRODUCT_TITLES)
        try:
            self.log.info("Products counted and returned.")
            return str(len(self.driver.find_elements(*self.ALL_PRODUCT_TITLES)))
        except Exception as e:
            self.log.error("Products can not to be count.")
            raise e

    def ACT_GET_PRODUCT_COUNT_IN_FILTER(self):
        self.wait_until_visibility_of_all_elements(self.FILTER_PRODUCT_QUANTITIES_IN_PRODUCT_TYPE)
        quantities = self.driver.find_elements(*self.FILTER_PRODUCT_QUANTITIES_IN_PRODUCT_TYPE)
        total = 0
        for i in range(len(quantities)):
            total += int(quantities[i].text.strip("(").strip(")"))
        self.log.info(str(total) + " products gathered.")
        return str(total)

    def ACT_GET_A_FILTER_QUANTITY(self, variation):
        element = [By.XPATH, "//span[text()='" + variation + "']/following-sibling::span"]
        filter_quantity = self.get_element_text(element).strip(")").strip("(")
        self.log.info(filter_quantity + " products found in " + variation + " variation.")
        return filter_quantity

    def ACT_VALIDATE_PRODUCT_PRICE_BY_SORTING(self, feature):
        self.wait_until_element_attribute_text_to_be(self.PRODUCT_COMPONENT, "class", "product-grid")
        self.wait_until_visibility_of_all_elements(self.ALL_PRODUCT_PRICES)
        products = self.driver.find_elements(*self.ALL_PRODUCT_PRICES)
        if feature.lower() == "highest":
            # self.driver.execute_script("arguments[0].scrollIntoView();", products[i])
            for i in range(len(products) - 2):
                assert int(products[i].text[0:products[i].text.index(",")]) >= int(products[i + 1].text[0:products[i + 1].text.index(",")])
        elif feature.lower() == "lowest":
            for i in range(len(products) - 2):
                # self.driver.execute_script("arguments[0].scrollIntoView();", products[i])
                assert int(products[i].text[0:products[i].text.index(",")]) <= int(products[i + 1].text[0:products[i + 1].text.index(",")])
        self.log.info("Product prices sorted correctly.")

    def ACT_VALIDATE_HEADER_IN_URL(self):
        self.assert_current_url(self.get_element_text(self.HEADER_PRODUCT_NAME_TEXT).replace(" ", "-").replace("\"", ""))
        self.log.info("Categorized product name in the url and around the products.")

    def ACT_VALIDATE_HEADER_IN_PRODUCTS(self):
        self.assert_text_in_element(self.ALL_PRODUCT_TITLES, self.get_element_text(self.HEADER_PRODUCT_NAME_TEXT).replace("\"", ""))

    def ACT_VALIDATE_HEADER_IN_URL_AND_PRODUCTS(self):
        self.ACT_VALIDATE_HEADER_IN_URL()
        self.ACT_VALIDATE_HEADER_IN_URL()
