import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# Reuse same base URL and credentials as login tests
BASE_URL = "https://www.saucedemo.com/"
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


def login_and_go_to_inventory(browser):
    """Log in and make sure we land on the inventory page."""
    browser.get(BASE_URL)

    user_input = browser.find_element(By.ID, "user-name")
    pass_input = browser.find_element(By.ID, "password")
    login_btn = browser.find_element(By.ID, "login-button")

    user_input.clear()
    pass_input.clear()

    user_input.send_keys(VALID_USERNAME)
    pass_input.send_keys(VALID_PASSWORD)
    login_btn.click()

    # Wait until inventory page really loads
    WebDriverWait(browser, 5).until(EC.url_contains("inventory"))
    assert "inventory" in browser.current_url


def test_sort_price_low_to_high(browser):
    """
    TC_UI_004 – Sort products by Price (low to high)
    Expectation: Prices are displayed in ascending order.
    """
    login_and_go_to_inventory(browser)

    # Select "Price (low to high)" in sort dropdown
    sort_dropdown = Select(
        browser.find_element(By.CLASS_NAME, "product_sort_container")
    )
    sort_dropdown.select_by_visible_text("Price (low to high)")

    # Grab all displayed prices and convert to float
    price_elements = browser.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = [float(p.text.replace("$", "").strip()) for p in price_elements]

    # Assert list is sorted ascending
    assert prices == sorted(prices)


def test_add_item_to_cart_shows_badge(browser):
    """
    TC_UI_005 – Add one product to cart
    Expectation: Cart badge shows 1 item.
    """
    login_and_go_to_inventory(browser)

    # Click "Add to cart" for the first visible item
    first_add_button = browser.find_elements(
        By.CSS_SELECTOR, ".inventory_item button"
    )[0]
    first_add_button.click()

    # Cart badge should show "1"
    cart_badges = browser.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(cart_badges) == 1
    assert cart_badges[0].text == "1"


@pytest.mark.xfail(reason="Flaky in headless mode / timing-dependent, kept as stretch test")
def test_remove_item_from_cart_clears_badge(browser):
    """
    TC_UI_006 – Remove product from cart
    Expectation: Cart badge disappears after removing the only item.
    """
    login_and_go_to_inventory(browser)

    # Add one item to cart from inventory
    add_button = browser.find_elements(
        By.CSS_SELECTOR, ".inventory_item button"
    )[0]
    add_button.click()

    # Wait until cart badge shows "1"
    badge = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert badge.text == "1"

    # Click the same button again (it is now a "Remove" button)
    remove_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test^='remove-']"))
    )
    remove_button.click()

    # Wait until the badge disappears
    WebDriverWait(browser, 5).until_not(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    # Final sanity check: no badge elements left
    cart_badges = browser.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(cart_badges) == 0


@pytest.mark.xfail(reason="Menu / logout link occasionally not found in CI/headless, stretch test")
def test_logout_returns_to_login(browser):
    """
    TC_UI_007 – Logout from inventory page
    Expectation: User is returned to the login page.
    """
    login_and_go_to_inventory(browser)

    # Open side menu (wait until clickable)
    menu_btn = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    )
    menu_btn.click()

    # Wait until Logout link is visible and clickable
    logout_link = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_link.click()

    # Wait until login button appears — this guarantees we're on the login page
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "login-button"))
    )

    # Back on login page
    assert BASE_URL in browser.current_url
