from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_form_validation():
    # Инициализация драйвера
    driver = webdriver.Chrome()

    try:
        # Открытие страницы
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        driver.maximize_window()  # Максимизируем окно, чтобы избежать перекрытия элементов

        # Заполнение формы
        form_fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            # "zip-code" оставляем пустым
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        for field, value in form_fields.items():
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, f'input[name="{field}"]'))
            )
            element.clear()
            element.send_keys(value)

        # Прокручиваем к кнопке перед нажатием
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        ActionChains(driver).move_to_element(submit_button).perform()

        # Нажатие кнопки Submit с явным ожиданием
        submit_button.click()

        # Ожидание применения стилей
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code.alert-danger"))
        )

        # Проверка, что поле Zip code подсвечено красным
        zip_code = driver.find_element(By.CSS_SELECTOR, '#zip-code')
        assert "alert-danger" in zip_code.get_attribute("class"), "Поле Zip code должно быть подсвечено красным"

        # Список полей, которые должны быть подсвечены зеленым
        green_fields = [
            'first-name', 'last-name', 'address', 'e-mail', 'phone',
            'city', 'country', 'job-position', 'company'
        ]

        # Проверка, что остальные поля подсвечены зеленым
        for field in green_fields:
            element = driver.find_element(By.CSS_SELECTOR, f'#{field}')
            assert "alert-success" in element.get_attribute("class"), f"Поле {field} не подсвечено зеленым"

    finally:
        # Закрытие браузера
        driver.quit()

if __name__ == "__main__":
    test_form_validation()
