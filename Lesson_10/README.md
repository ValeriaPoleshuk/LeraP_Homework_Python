# Проекты по автоматизации тестирования с использованием Allure

## Описание проекта

Проект направлен на автоматизацию тестирования двух ключевых процессов на сайте SauceDemo с применением инструмента Allure для создания отчетов.

### Структура проекта:

- `calculator_test.py`: Тестирует калькулятор с длительной задержкой вычислений.
- `shopping_cart_test.py`: Тестирует процесс покупки товаров на сайте SauceDemo.
- `reports/`: Папка для сохранения отчетов Allure.

## Тест 1: Калькулятор с задержкой (calculator_test.py)

Тест проверяет корректность работы калькулятора с большой задержкой (45 секунд). Основная задача — убедиться, что результат вычисления «7 + 8» равен «15» спустя указанное время.

### Результаты:

- Рассматриваемый калькулятор намеренно замедляется, чтобы имитировать реальную нагрузку на сервер.
- Время ожидания составляет строго 45 секунд, после которого результат сравнения проверяется.

## Тест 2: Процесс покупки товаров (shopping_cart_test.py)

Цель теста — проверить полноценную покупку на сайте SauceDemo, включающую следующие шаги:

1. Авторизация на сайте.
2. Выбор и добавление товаров в корзину.
3. Оформление заказа и заполнение контактных данных.
4. Проверка итоговой стоимости ($58.29).

### Результаты:

- Полноценный цикл покупки товаров проверяется от начала до конца.
- Итоговая стоимость проверяется с точностью до цента.

## Запуск тестов и формирование отчетов

Для запуска тестов и генерации отчетов выполните следующие шаги:

1. **Установите зависимости**:
 ```bash pip install -r requirements.txt

