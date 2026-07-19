# Домашнее задание №10 — Allure

Проект содержит доработанные автотесты из домашнего задания №7 с использованием:

- Python;
- pytest;
- Selenium WebDriver;
- Page Object;
- Allure Report;
- Google Chrome для теста калькулятора;
- Mozilla Firefox для теста интернет-магазина.

## Структура проекта

```text
lesson_10/
├── pages/
│   ├── calculator_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── tests/
│   ├── test_calculator.py
│   └── test_shop.py
├── conftest.py
├── pytest.ini
└── README.md
```

## Создание ветки

Из корня Git-репозитория выполнить:

```bash
git checkout -b lesson10
```

После добавления папки и файлов:

```bash
git add lesson_10
git commit -m "Add lesson 10 tests with Allure"
git push -u origin lesson10
```

## Подготовка окружения

Установить Python 3.10 или новее, Google Chrome и Mozilla Firefox.
Selenium использует Selenium Manager, поэтому при обычной конфигурации отдельная ручная установка ChromeDriver и GeckoDriver не требуется.

Создать виртуальное окружение из корня папки `lesson_10`:

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Windows cmd

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

## Установка Allure Report

Для формирования HTML-отчета необходимо установить Allure Report CLI. Для Allure Report 2 также требуется установленная Java.

Проверить установку:

```bash
allure --version
```

## Запуск тестов и формирование результатов Allure

Из папки `lesson_10` выполнить:

```bash
pytest
```

Параметры Allure уже заданы в `pytest.ini`. Результаты будут записаны в папку:

```text
allure-results
```

Эквивалентный запуск с явными параметрами:

```bash
pytest -v --alluredir=allure-results --clean-alluredir
```

Запуск только теста калькулятора:

```bash
pytest tests/test_calculator.py
```

Запуск только теста магазина:

```bash
pytest tests/test_shop.py
```

## Просмотр сформированного отчета

Самый простой способ сформировать отчет и сразу открыть его в браузере:

```bash
allure serve allure-results
```

Для отдельного создания статического отчета выполнить:

```bash
allure generate allure-results -o allure-report --clean
```

Затем открыть созданный отчет:

```bash
allure open allure-report
```

## Allure-разметка

Каждый тест содержит:

- `@allure.title` — понятное название;
- `@allure.description` — описание сценария;
- `@allure.feature` — тестируемую функциональность;
- `@allure.severity` — уровень важности.

Действия Page Object размечены декоратором `@allure.step`. Проверки оформлены через контекстный менеджер `with allure.step(...)`.

## Ожидаемые результаты

1. Калькулятор после задержки отображает результат `15` для выражения `7 + 8`.
2. Итоговая стоимость трех товаров в SauceDemo равна `$58.29`.
