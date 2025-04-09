import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")
        self.keys_area = (By.CSS_SELECTOR, ".keys")

    def set_delay(self, delay):
        self.driver.find_element(*self.delay_input).clear()
        self.driver.find_element(*self.delay_input).send_keys(str(delay))

    def click_button(self, button_text):
        if button_text in "0123456789":
            locator = (By.XPATH, f"//span[@class='btn btn-outline-primary' and text()='{button_text}']")
        elif button_text in "+-÷x":
            locator = (By.XPATH, f"//span[@class='operator btn btn-outline-success' and text()='{button_text}']")
        elif button_text == "=":
            locator = (By.XPATH, "//span[contains(@class, 'btn-outline-warning') and text()='=']")
        else:
            raise ValueError(f"Unknown button: {button_text}")

        button = WebDriverWait(self.driver, 15).until(

            EC.element_to_be_clickable(locator)
        )
        button.click()

    def get_result(self, timeout=45):
        # Ждем пока исчезнет "7+8" и появится числовой результат
        WebDriverWait(self.driver, timeout).until_not(
            EC.text_to_be_present_in_element(self.result_display, "7+8")
        )
        return self.driver.find_element(*self.result_display).text


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator_with_delay(driver):
    calculator = CalculatorPage(driver)
    calculator.set_delay(45)  # 45 секунд задержки

    # Вводим выражение
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")

    # Нажимаем равно с дополнительными ожиданиями
    equal_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'btn-outline-warning') and text()='=']"))
    )
    equal_button.click()

    # Ждем результат с большим таймаутом
    result = WebDriverWait(driver, 60).until(
        lambda d: d.find_element(*calculator.result_display).text
    )
    result = calculator.get_result()
    print(f"Полученный результат: {result}")  # Для диагностики
    assert result == "15", f"Ожидался '15', получено '{result}'"
    assert result == "15", f"Expected 15, got {result}"