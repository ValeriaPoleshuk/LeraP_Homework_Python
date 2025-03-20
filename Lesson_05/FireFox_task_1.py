from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Firefox
driver = webdriver.Firefox()

# Модальное окно

try:
    # Открыть страницу
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    # Ожидание появления модального окна
    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "modal"))
    )

    # Найти кнопку "Close" и нажать на неё
    close_button = modal.find_element(By.XPATH, ".//p[text()='Close']")
    close_button.click()

    # Пауза для визуальной проверки результата
    input("Нажмите Enter для завершения...")

finally:
    # Закрыть браузер
    driver.quit()
