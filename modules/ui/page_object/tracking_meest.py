from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class Search(BasePage):
    URL = "https://ua.meest.com"

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(Search.URL)

    def tracking(self, tracking_number):

        # Знаходимо поле для пошуку або трекінгу
        search_query = self.driver.find_element(By.NAME, "query")

        # Вводимо номер відстеження
        search_query.send_keys(tracking_number)

        # Знаходимо кнопку пошуку
        search_btn = self.driver.find_element(By.CLASS_NAME, "input-btn")

        # Емулюємо натискання на кнопку пошуку
        search_btn.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
