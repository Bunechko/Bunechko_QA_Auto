import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # Creating an object to control the browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # We open the page https://github.com/login
    driver.get("https://github.com/login")

    # We find the field in which we will enter the wrong username or e-mail
    login_elem = driver.find_element(By.ID, "login_field")
    
    # Enter the wrong username or email
    login_elem.send_keys("Bunechko@not@exist")

    # We find the field in which we will enter the wrong password
    pass_elem = driver.find_element(By.ID, "password")

    # Enter the wrong password
    pass_elem.send_keys("password")

    # Find the Sign in button
    btn_elem = driver.find_element(By.NAME, "commit")

    # Emulate a click with the left mouse button
    btn_elem.click()

    # We check that the name of the page is what we expect
    assert driver.title == "Sign in to GitHub · GitHub"

    # We close the page
    driver.close()
