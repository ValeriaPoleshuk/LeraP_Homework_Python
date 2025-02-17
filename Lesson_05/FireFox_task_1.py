from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера Firefox
driver = webdriver.Firefox()

# Модальное окно
try:
    # Открытие страницы
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    # Ожидание появления модального окна
    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "modal"))
    )

    # Нахождение кнопки "Close" в модальном окне
    close_button = modal.find_element(By.XPATH, "//div[@class='modal-footer']/p")

    # Прокрутка к элементу, если он не виден
    driver.execute_script("arguments[0].scrollIntoView(true);", close_button)

    # Ожидание, пока элемент станет кликабельным
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(close_button))

    # Клик по кнопке "Close"
    close_button.click()

    # Пауза для визуальной проверки
    input("Нажмите Enter для завершения...")

finally:
    # Закрытие браузера
    driver.quit()
