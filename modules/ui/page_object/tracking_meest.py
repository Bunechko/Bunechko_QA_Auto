# Project task 6. Module 28. UI testing

from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class Search(BasePage):
    URL = "https://ua.meest.com"

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(Search.URL)

    def tracking(self, tracking_number):

        # Find the search or tracking field
        search_query = self.driver.find_element(By.NAME, "query")

        # Enter the tracking number
        search_query.send_keys(tracking_number)

        # We find the search button
        search_btn = self.driver.find_element(By.CLASS_NAME, "input-btn")

        # Emulate pressing the search button
        search_btn.click()

    # We check whether the page corresponds to the expected
    def check_title(self, expected_title):
        return self.driver.title == expected_title
