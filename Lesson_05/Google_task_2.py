from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация драйвера ( для Chrome)
driver = webdriver.Chrome()

# Клик по кнопке без ID
try:
    # Шаг 1: Открыть страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # Шаг 2: Кликнуть на синюю кнопку
    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    blue_button.click()
    print("Клик на синюю кнопку выполнен успешно.")

    # Пауза
    time.sleep(2)

finally:
    # Закрыть браузер
    driver.quit()
