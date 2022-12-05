import pytest

from pages.navbar import Navbar
from pages.mainpage import Mainpage
from pages.shop_page import ShopPage

"""
    TC05_SHOP_PAGE:
    Total of products count in filters in shop page header must be same with total product count.
"""


@pytest.mark.usefixtures("setup")
class Test_TC05_SHOP_PAGE:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.sp = ShopPage(self.driver)
        self.navbar = Navbar(self.driver)
        self.mp = Mainpage(self.driver)

    def test_tc05_product_counts_of_filters_in_the_header(self):
        self.navbar.ACT_GOTO_SEARCH_PRODUCT("spor")
        self.sp.ACT_VALIDATE_HEADER_IN_URL_AND_PRODUCTS()
        self.sp.assert_text_in_text(self.sp.ACT_GET_PRODUCT_COUNT_IN_FILTER(), self.sp.get_element_text(self.sp.PAGINATION_TOTAL_PRODUCTS_COUNT_TEXT))
