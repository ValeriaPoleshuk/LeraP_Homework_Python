from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Chrome
driver = webdriver.Chrome()

try:
    # Шаг 1: Открыть страницу
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    # Шаг 2: Пять раз кликнуть на кнопку "Add Element"
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    for _ in range(5):
        add_button.click()
        time.sleep(0.5)

    # Шаг 3: Собрать список кнопок "Delete"
    delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

    # Шаг 4: Вывести размер списка
    print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

finally:
    # Закрыть браузер
    driver.quit()
