from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Firefox
driver = webdriver.Firefox()

# Поле ввода

try:
    # Открытие страницы
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Ожидание появления поля ввода
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )

    # Ввод текста "1000"
    input_field.send_keys("1000")

    # Очистка поля
    input_field.clear()

    # Ввод текста "999"
    input_field.send_keys("999")

    # Пауза для визуальной проверки
    input("Нажмите Enter для завершения...")

finally:
    # Закрытие браузера
    driver.quit()
