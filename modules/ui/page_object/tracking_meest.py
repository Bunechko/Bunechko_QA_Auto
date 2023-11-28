# Project task 6. Module 28. UI testing

from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class TrackingMeest(BasePage):
    URL = "https://ua.meest.com"

    def __init__(self):
        super().__init__()

    def go_to(self):
        # Navigate to the Meest tracking page
        self.driver.get(TrackingMeest.URL)

    def tracking(self, tracking_number):
        # Find and input the tracking number
        search_query = self.driver.find_element(By.NAME, "query")
        search_query.send_keys(tracking_number)

        # Find and click the search button
        search_btn = self.driver.find_element(By.CLASS_NAME, "input-btn")
        search_btn.click()

    # Checking whether the page corresponds to the expected result
    def check_title(self, expected_title):
        return self.driver.title == expected_title
