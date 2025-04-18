import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        # Инициализация драйвера
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def tearDown(self):
        # Завершение работы драйвера
        self.driver.quit()

    def test_shopping_cart_flow(self):
        # Тест процесса покупки
        # Авторизация
        username_input = self.driver.find_element(By.ID, "user-name")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        # Ожидаем открытия страницы инвентаря
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("inventory.html")
        )

        # Добавляем товары в корзину
        backpack_add_button = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack")
        tshirt_add_button = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        onesie_add_button = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie")

        backpack_add_button.click()
        tshirt_add_button.click()
        onesie_add_button.click()

        # Проверяем количество товаров в корзине
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(cart_badge.text, "3", "В корзине должно быть 3 товара")

        # Переходим в корзину
        shopping_cart_link = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link")
        shopping_cart_link.click()

        # Нажимаем на кнопку Checkout
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()

        # Заполняем форму
        first_name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        last_name_input = self.driver.find_element(By.ID, "last-name")
        postal_code_input = self.driver.find_element(By.ID, "postal-code")

        first_name_input.send_keys("Валерия")
        last_name_input.send_keys("Полеук")
        postal_code_input.send_keys("200886")

        # Нажимаем Continue
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

        # Проверяем итоговую стоимость
        total_cost_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_cost = total_cost_element.text.replace("Total: ", "")
        print("Итоговая стоимость:", total_cost)

        self.assertEqual(
            total_cost,
            "$58.29",
            "Итоговая сумма не равна $58.29"
        )


if __name__ == "__main__":
    unittest.main()
