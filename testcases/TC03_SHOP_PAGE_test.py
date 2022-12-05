import pytest

from pages.navbar import Navbar
from pages.mainpage import Mainpage
from pages.shop_page import ShopPage

""""
    TC03_SHOP_PAGE:
    Product count in filter must be same with filtered products count by that filter.
"""


@pytest.mark.usefixtures("setup")
class Test_TC03_SHOP_PAGE:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.sp = ShopPage(self.driver)
        self.navbar = Navbar(self.driver)
        self.mp = Mainpage(self.driver)

    def test_tc03_product_counts_in_filter(self):
        filter_variation = "XL"
        self.navbar.ACT_GOTO_SEARCH_PRODUCT("jogger")
        self.sp.ACT_FILTER_FOR_A_VARIATION(filter_variation)
        self.sp.assert_text_in_text(self.sp.ACT_GET_A_FILTER_QUANTITY(filter_variation), self.sp.get_element_text(self.sp.PAGINATION_TOTAL_PRODUCTS_COUNT_TEXT))
