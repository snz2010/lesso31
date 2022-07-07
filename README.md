# Урок 31 - Валидаторы и тесты в Django

**Критерии выполнения:**

- [ ]  Используется валидация с помощью атрибутов модели.
- [ ]  Используется валидация с помощью поля `validators` в модели и самописной функции.
- [ ]  Используется валидация с помощью атрибутов сериализатора.
- [ ]  Используется валидация с помощью атрибута `validators` сериализатора и самописного класса.
- [ ]  Написаны тесты на указанные ручки.
- [ ]  Тесты используют фикстуру для авторизации.
- [ ]  Тесты используют фабрики моделей.

# Тесты

- создание объявления — POST `/ads`;
- создание подборки — POST `/selection`;
- выдачу списка объявлений (без фильтров) — GET `/ads`;
- выдачу одного объявления — GET `/ads/<ad_id>`.

# Валидаторы

## Категория

- Добавьте поле `slug`, длина которого не менее 5 и не более 10 символов, а значения уникальны.

## Объявление

- Поле `name` объявления не может быть пустым и должно содержать не менее 10 символов.
- Поле `description` может быть пустым.
- Значение поля `price` не может быть меньше 0.
- Значение поля `is_published` при создании объявления не может быть True.

## Пользователи

- Добавьте пользователям поле `birth_date` и запретите регистрироваться пользователям младше 9 лет.
- Добавьте поле `email`, сделайте его уникальным и запретите регистрацию с почтового адреса в домене rambler.ru.