import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # Фикстура для инициализации и закрытия браузера.
    options = Options()
    options.add_argument("--headless")  # Режим без GUI (для CI/серверов)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)  # Можно заменить на Firefox/Edge

    yield driver  # Возвращает драйвер тесту

    driver.quit()  # Закрытие браузера после теста


