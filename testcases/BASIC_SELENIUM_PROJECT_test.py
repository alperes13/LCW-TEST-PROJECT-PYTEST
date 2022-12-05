import pytest

from pages.mainpage import Mainpage
from pages.my_cart_page import MyCartPage
from pages.navbar import Navbar
from pages.product_page import ProductPage
from pages.shop_page import ShopPage

"""
    BASIC SELENIUM PROJECT:
    A user should be able to add a product to cart.
"""


@pytest.mark.usefixtures("setup")
class Test_BasicSeleniumProject:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.sp = ShopPage(self.driver)
        self.navbar = Navbar(self.driver)
        self.pp = ProductPage(self.driver)
        self.mp = Mainpage(self.driver)
        self.mcp = MyCartPage(self.driver)

    def test_basic_selenium_project(self):
        self.navbar.ACT_MOUSEOVER_A_CATEGORY_AND_CLICK_ON_A_PRODUCT("Aksesuar", "Plaj Havlusu")
        self.sp.ACT_VALIDATE_HEADER_IN_URL_AND_PRODUCTS()
        self.sp.ACT_CLICK_ON_ANY_PRODUCT()
        self.pp.ACT_ADD_TO_CART()
        badge_product_quantity = self.navbar.get_element_text(self.navbar.MY_CART_BADGE)
        self.navbar.ACT_GOTO_CART()
        product_quantity_in_cart = self.mcp.ACT_GET_PRODUCT_QUANTITY()
        self.mcp.assert_text_in_text(badge_product_quantity, product_quantity_in_cart)
        self.mp.ACT_GOTO_MP()
