from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)
    
    def try_login(self, username, password):
        # We find the field in which we will enter the wrong username or e-mail
        login_elem = self.driver.find_element(By.ID, "login_field")
    
        # Enter the wrong username or email
        login_elem.send_keys(username)

        # We find the field in which we will enter the wrong password
        pass_elem = self.driver.find_element(By.ID, "password")

        # Enter the wrong password
        pass_elem.send_keys(password)

        # Find the Sign in button
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Emulate a click with the left mouse button
        btn_elem.click()

    # We check whether the page corresponds to the expected
    def check_title(self, expected_title):
        return self.driver.title == expected_title
