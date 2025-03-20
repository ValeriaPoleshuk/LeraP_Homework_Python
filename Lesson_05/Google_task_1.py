from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome
driver = webdriver.Chrome()

# Клик по кнопке
try:
    # Шаг 1: Открыть страницу
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    # Шаг 2: Пять раз кликнуть на кнопку "Add Element"
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    for click_count in range(5):  # Используем понятное имя переменной
        add_button.click()
        # Ожидание, пока кнопка "Add Element" станет кликабельной
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Element']")))

    # Шаг 3: Собрать список кнопок "Delete"
    delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

    # Шаг 4: Вывести размер списка
    print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

finally:
    # Закрыть браузер
    driver.quit()
