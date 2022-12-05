import pytest

from pages.navbar import Navbar
from pages.mainpage import Mainpage
from pages.shop_page import ShopPage

"""
    TC04_SHOP_PAGE:
    Sorting function in the shop page must be work correctly.
"""


@pytest.mark.usefixtures("setup")
class Test_TC04_SHOP_PAGE:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.sp = ShopPage(self.driver)
        self.navbar = Navbar(self.driver)
        self.mp = Mainpage(self.driver)

    def test_TC04_sorting_function_highest(self):
        self.navbar.ACT_GOTO_SEARCH_PRODUCT("bere")
        self.sp.ACT_VALIDATE_HEADER_IN_URL_AND_PRODUCTS()
        self.sp.ACT_SORT_PRODUCT_FUNCTION("highest")
        self.sp.ACT_VALIDATE_PRODUCT_PRICE_BY_SORTING("highest")
        self.mp.ACT_GOTO_MP()

    def test_TC04_sorting_function_lowest(self):
        self.navbar.ACT_GOTO_SEARCH_PRODUCT("bere")
        self.sp.ACT_VALIDATE_HEADER_IN_URL_AND_PRODUCTS()
        self.sp.ACT_SORT_PRODUCT_FUNCTION("lowest")
        self.sp.ACT_VALIDATE_PRODUCT_PRICE_BY_SORTING("lowest")
