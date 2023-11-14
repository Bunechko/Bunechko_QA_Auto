# Project task 6. Module 28. UI testing

from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class BuyGoods(BasePage):

    URL = 'https://ua.iherb.com'
    
    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(BuyGoods.URL)

    def buy_goods(self, goods_name):

        # -----------------------------------------------------------------------
        # The highlighted piece of code was written using GPT chat.
        # A dynamic search element was searched.
        # To do this, it was necessary to find the appropriate class and change it.

        # We find the elements of the class to open the search field
        branded_header = self.driver.find_element(By.CLASS_NAME, "branded-header-container.header-container")
        iherb_header_search = self.driver.find_element(By.CLASS_NAME, "iherb-header-search")

        # We get the current classes of search field elements
        branded_header_classes = branded_header.get_attribute("class")
        iherb_header_search_classes = iherb_header_search.get_attribute("class")

        # We change the classes of the search field
        branded_header_classes += " search-open"
        iherb_header_search_classes += " active"

        # We update the classes of search field elements using JavaScript code
        self.driver.execute_script(
            "arguments[0].setAttribute('class', arguments[1]);",
            branded_header, branded_header_classes
            )
        self.driver.execute_script(
            "arguments[0].setAttribute('class', arguments[1]);",
            iherb_header_search, iherb_header_search_classes
            )
        
        # -----------------------------------------------------------------------
       
        # We find the product search field
        search_elem = self.driver.find_element(By.ID, "txtSearch")

        # Enter the name of the product
        search_elem.send_keys(goods_name)

        # We find the search button
        search_btn = self.driver.find_element(By.ID, "searchBtn")
    
        # Emulate a click with the left mouse button
        search_btn.click()

        # We find the product
        goods_elem = self.driver.find_element(By.ID, "pid_22335")

        # We choose a product
        goods_elem.click()
        
        # Find the "Add to Cart" button
        add_cart_goods = self.driver.find_element(By.NAME, "AddToCart")

        # We emulate a click with the left mouse button, and add a delay for the animation
        add_cart_goods.click()
        time.sleep(2)

        # We find the basket
        carts = self.driver.find_element(By.CLASS_NAME, "checkout-button")

        # Emulate a click with the left mouse button
        carts.click()

        # We find the field for changing the quantity of the product
        count_elem = self.driver.find_element(By.ID, "react-select-2-input")

        # Enter the number 5
        count_elem.send_keys(5)

        # We find the delivery change element
        delivery_elem = self.driver.find_element(By.CLASS_NAME, "css-g94so0")

        # Emulate a click with the left mouse button
        delivery_elem.click()
        
        # We find the country change field
        country_elem = self.driver.find_element(By.CLASS_NAME, "css-y8v00p")

        # We check the value, and enter "UA - Ukraine" if necessary
        if country_elem != "UA - Україна":
            country_elem.send_keys("UA - Україна")
            country_elem.send_keys(Keys.ENTER)
        else:
            pass

        # We find the index change field
        zip_elem = self.driver.find_element(By.NAME, "postal-code")

        # Enter the value "79496"
        zip_elem.send_keys("79496")
        zip_elem.send_keys(Keys.ENTER)

        # Find the "Save" button
        save_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[data-qa-element="btn-save-destination"]')

        # We keep
        save_btn.click()
        time.sleep(1)

        # We find Meest delivery
        delivery_meest_elem = self.driver.find_element(By.CLASS_NAME, 'css-3ge7j2')

        # We choose Meest delivery
        delivery_meest_elem.click()

        # We find the element "Make an order"
        order_elem = self.driver.find_element(By.CLASS_NAME, "css-1ijv08")

        # We create an order
        order_elem.click()

    # We check whether the page corresponds to the expected
    def check_title(self, expected_title):
        return self.driver.title == expected_title
