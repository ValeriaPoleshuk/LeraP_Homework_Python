from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Chrome
driver = webdriver.Chrome()

try:
    # Шаг 1: Открыть страницу
    driver.get("http://uitestingplayground.com/classattr")

    # Шаг 2: Кликнуть на синюю кнопку
    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")

    actions = ActionChains(driver)
    actions.click(blue_button).perform()

    print("Клик на синюю кнопку выполнен успешно.")

    # Пауза для наглядности (необязательно)
    time.sleep(2)

finally:
    # Закрыть браузер
    driver.quit()
