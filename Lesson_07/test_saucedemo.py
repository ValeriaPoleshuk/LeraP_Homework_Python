import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self

    def enter_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        return self

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)
        return self

    def login(self):
        self.driver.find_element(By.ID, "login-button").click()
        return InventoryPage(self.driver)


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        item_container = self.driver.find_element(By.XPATH,
                                                  f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']")
        item_container.find_element(By.CLASS_NAME, "btn_inventory").click()
        return self

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        return CartPage(self.driver)


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
        return CheckoutPage(self.driver)

    def get_cart_items(self):
        return self.driver.find_elements(By.CLASS_NAME, "cart_item")


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_info(self, first_name, last_name, zip_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        return self

    def continue_to_overview(self):
        self.driver.find_element(By.ID, "continue").click()
        return self

    def get_total(self):
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text

    def finish_checkout(self):
        self.driver.find_element(By.ID, "finish").click()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_checkout_total(driver):
    # Test data
    username = "standard_user"
    password = "secret_sauce"
    first_name = "John"
    last_name = "Doe"
    zip_code = "12345"
    expected_total = "Total: $58.29"

    # Test steps
    inventory_page = (
        LoginPage(driver)
        .open()
        .enter_username(username)
        .enter_password(password)
        .login()
    )

    inventory_page \
        .add_to_cart("Sauce Labs Backpack") \
        .add_to_cart("Sauce Labs Bolt T-Shirt") \
        .add_to_cart("Sauce Labs Onesie")

    cart_page = inventory_page.go_to_cart()
    checkout_page = cart_page.checkout()

    total = (
        checkout_page
        .fill_info(first_name, last_name, zip_code)
        .continue_to_overview()
        .get_total()
    )

    # Assertion
    assert total == expected_total, f"Expected total {expected_total}, but got {total}"


