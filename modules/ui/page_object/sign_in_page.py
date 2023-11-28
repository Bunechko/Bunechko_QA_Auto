from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # Find and input wrong username or email
        login_elem = self.driver.find_element(By.ID, "login_field")
        login_elem.send_keys(username)

        # Find and input wrong password
        pass_elem = self.driver.find_element(By.ID, "password")
        pass_elem.send_keys(password)

        # Click on the Sign in button
        btn_elem = self.driver.find_element(By.NAME, "commit")
        btn_elem.click()

    # Checking whether the page corresponds to the expected result
    def check_title(self, expected_title):
        return self.driver.title == expected_title
