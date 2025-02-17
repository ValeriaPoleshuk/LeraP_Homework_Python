from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера Firefox
driver = webdriver.Firefox()

try:
    # Открытие страницы
    driver.get("http://the-internet.herokuapp.com/login")

    # Ввод логина и пароля
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # Нажатие кнопки Login
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Пауза для визуальной проверки
    input("Нажмите Enter для завершения...")

finally:
    # Закрытие браузера
    driver.quit()
