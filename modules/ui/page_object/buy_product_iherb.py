# Project task 6. Module 28. UI testing

from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BuyProductIherb(BasePage):
    URL = "https://ua.iherb.com"

    def __init__(self):
        super().__init__()

    def go_to(self):
        # Navigate to the iHerb store page
        self.driver.get(BuyProductIherb.URL)

    def buy_goods(self, goods_name):
        # The piece of code was written using GPT chat.
        # A dynamic search element was searched.
        # To do this, it was necessary to find the appropriate class and change it.
        # Open the search field
        branded_header = self.driver.find_element(
            By.CLASS_NAME, "branded-header-container.header-container"
        )
        iherb_header_search = self.driver.find_element(
            By.CLASS_NAME, "iherb-header-search"
        )
        branded_header_classes = branded_header.get_attribute("class")
        iherb_header_search_classes = iherb_header_search.get_attribute("class")
        branded_header_classes += " search-open"
        iherb_header_search_classes += " active"
        self.driver.execute_script(
            "arguments[0].setAttribute('class', arguments[1]);",
            branded_header,
            branded_header_classes,
        )
        self.driver.execute_script(
            "arguments[0].setAttribute('class', arguments[1]);",
            iherb_header_search,
            iherb_header_search_classes,
        )

        # Search for the product
        search_elem = self.driver.find_element(By.ID, "txtSearch")
        search_elem.send_keys(goods_name)
        search_btn = self.driver.find_element(By.ID, "searchBtn")
        search_btn.click()

        # Choose and add the product to the cart
        goods_elem = self.driver.find_element(By.ID, "pid_22335")
        goods_elem.click()
        add_cart_goods = self.driver.find_element(By.NAME, "AddToCart")
        add_cart_goods.click()

        # Navigate to the cart
        wait = WebDriverWait(self.driver, 5)
        carts = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "checkout-button"))
        )
        carts.click()

        # Update quantity, select delivery options, and proceed to checkout
        count_elem = self.driver.find_element(By.ID, "react-select-2-input")
        count_elem.send_keys(5)
        delivery_elem = self.driver.find_element(By.CLASS_NAME, "css-g94so0")
        delivery_elem.click()
        country_elem = self.driver.find_element(By.CLASS_NAME, "css-y8v00p")
        if country_elem != "UA - Україна":
            country_elem.send_keys("UA - Україна")
            country_elem.send_keys(Keys.ENTER)
        zip_elem = self.driver.find_element(By.NAME, "postal-code")
        zip_elem.send_keys("79496")
        zip_elem.send_keys(Keys.ENTER)
        save_btn = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-qa-element="btn-save-destination"]'
        )
        save_btn.click()

        # Choose delivery method and make the order
        delivery_meest_elem = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-3ge7j2"))
        )
        delivery_meest_elem.click()
        order_elem = self.driver.find_element(By.CLASS_NAME, "css-1ijv08")
        order_elem.click()

    # Checking whether the page corresponds to the expected result
    def check_title(self, expected_title):
        return self.driver.title == expected_title
