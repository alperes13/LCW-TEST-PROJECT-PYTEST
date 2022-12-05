import pytest

from pages.navbar import Navbar
from pages.mainpage import Mainpage
from pages.shop_page import ShopPage

"""
    TC06_SHOP_PAGE:
    Searched or categorized product name should be in url and inside of product names.
"""


@pytest.mark.usefixtures("setup")
class Test_TC05_SHOP_PAGE:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.sp = ShopPage(self.driver)
        self.navbar = Navbar(self.driver)
        self.mp = Mainpage(self.driver)

    def test_tc06_search_function(self):
        self.navbar.ACT_GOTO_SEARCH_PRODUCT("jean")
        self.sp.ACT_VALIDATE_HEADER_IN_URL_AND_PRODUCTS()

    def test_tc06_category_function(self):
        self.mp.ACT_GOTO_MP()
        self.navbar.ACT_MOUSEOVER_A_CATEGORY_AND_CLICK_ON_A_PRODUCT("Aksesuar", "Plaj Havlusu")
        self.sp.ACT_VALIDATE_HEADER_IN_URL_AND_PRODUCTS()
