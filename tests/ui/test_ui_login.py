from selenium.webdriver.common.by import By

# Base URL and test data
BASE_URL = "https://www.saucedemo.com/"

VALID_USERNAME = "standard_user"
LOCKED_USERNAME = "locked_out_user"
VALID_PASSWORD = "secret_sauce"


def login(browser, username, password):
    """Helper function to perform login on SauceDemo."""
    # Go to login page (safe to call even if conftest already does this)
    browser.get(BASE_URL)

    # Locate fields
    user_input = browser.find_element(By.ID, "user-name")
    pass_input = browser.find_element(By.ID, "password")
    login_btn = browser.find_element(By.ID, "login-button")

    # Clear and type
    user_input.clear()
    pass_input.clear()
    user_input.send_keys(username)
    pass_input.send_keys(password)

    # Click login
    login_btn.click()


def test_login_valid_credentials(browser):
    """
    TC_UI_001 – Login with valid credentials
    Expectation: User is redirected to the inventory (products) page.
    """
    login(browser, VALID_USERNAME, VALID_PASSWORD)

    # Check URL contains "inventory"
    assert "inventory" in browser.current_url

    # Check page title text
    title_text = browser.find_element(By.CLASS_NAME, "title").text
    assert title_text == "Products"


def test_login_invalid_password(browser):
    """
    TC_UI_002 – Login with invalid password
    Expectation: Error message is displayed and user stays on login page.
    """
    login(browser, VALID_USERNAME, "wrong_password")

    error = browser.find_element(By.CSS_SELECTOR, "[data-test='error']").text

    assert "Epic sadface" in error
    assert "do not match" in error  # generic part of the message
    assert BASE_URL in browser.current_url  # still on login page


def test_login_locked_out_user(browser):
    """
    TC_UI_003 – Login with locked out user
    Expectation: Locked-out error message is shown and user stays on login page.
    """
    login(browser, LOCKED_USERNAME, VALID_PASSWORD)

    error = browser.find_element(By.CSS_SELECTOR, "[data-test='error']").text

    assert "Epic sadface" in error
    assert "locked out" in error.lower()
    assert BASE_URL in browser.current_url  # still on login page
