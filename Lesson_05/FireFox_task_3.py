from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#  Firefox
driver = webdriver.Firefox()

# Форма авторизации

try:
    # Шаг 1: Открытие страницы
    driver.get("http://the-internet.herokuapp.com/login")

    # Шаг 2: Ввод значения в поле username
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_field.send_keys("tomsmith")

    # Шаг 3: Ввод значения в поле password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    # Шаг 4: Нажатие кнопки Login
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Пауза
    input("Нажмите Enter для завершения...")

finally:
    # Закрытие браузера
    driver.quit()
