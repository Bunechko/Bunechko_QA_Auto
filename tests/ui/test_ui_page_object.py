from modules.ui.page_object.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # Creating a page object
    sign_in_page = SignInPage()

    # We open the page https://github.com/login
    sign_in_page.go_to()

    # Trying to login to GitHub
    sign_in_page.try_login("Bunechko@not.exist", "bad_password")

    # We check that the name of the page is what we expect
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Close the browser
    sign_in_page.close()
