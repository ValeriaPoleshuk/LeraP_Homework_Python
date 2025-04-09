from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[@class='keys']//span[text()='{button_text}']/..")
            )
        )
        button.click()

    def get_result(self, timeout=45):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.result_display, "")
        )
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.result_display, "15")
        )
