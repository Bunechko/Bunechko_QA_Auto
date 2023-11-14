from modules.ui.page_object.buy_product_iherb import BuyGoods
import pytest


@pytest.mark.iherb
def test_iherb():
    # Creating a page object
    add_cart = BuyGoods()

    # We open the page https://ua.iherb.com
    add_cart.go_to()

    # We find the product, add it to the basket, proceed to the order
    add_cart.buy_goods("now foods vitamin d3 5000 iu - 240 softgels")

    # We check that we are on the data entry page in the personal account
    assert add_cart.check_title("Login Pages")

    # Close the browser
    add_cart.close()
