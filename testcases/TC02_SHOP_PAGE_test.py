import pytest

from pages.navbar import Navbar
from pages.mainpage import Mainpage
from pages.shop_page import ShopPage

"""
    TC02_SHOP_PAGE:
    Product count must be same by information count.
"""


@pytest.mark.usefixtures("setup")
class Test_TC02_SHOP_PAGE:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.sp = ShopPage(self.driver)
        self.navbar = Navbar(self.driver)
        self.mp = Mainpage(self.driver)

    def test_tc02_listed_product_quantity(self):
        self.navbar.ACT_GOTO_SEARCH_PRODUCT("blazer")
        self.sp.ACT_VALIDATE_HEADER_IN_URL_AND_PRODUCTS()
        self.sp.assert_text_in_text(self.sp.ACT_GET_PRODUCTS_COUNT(), self.sp.get_element_text(self.sp.PAGINATION_LISTED_PRODUCTS_COUNT_TEXT))
