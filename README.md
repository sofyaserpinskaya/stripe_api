# stripe_api
Тестовое задание - создание платежных форм для товаров.

## Методы API

- GET /buy/{id} - получение Stripe Session Id для оплаты выбранного Item. 

- GET /buy_order/{id} - получение Stripe Session Id для оплаты выбранного Order (несколько Item). 

- GET /item/{id} - HTML страница с информацией о выбранном Item и кнопка Buy (запрос на /buy/{id})

- GET /order/{id} - HTML страница с информацией о выбранном Order и кнопка Buy (запрос на /buy_order/{id}).

### Автор

[Софья Серпинская](https://github.com/sofyaserpinskaya)

### Технологии

Python, Django, Stripe API, PostgreSQL, Docker

### Шаблон наполнения env-файла

```bash
SECRET_KEY=secretkey
STRIPE_PUBLIC_KEY=pk_test...
STRIPE_SECRET_KEY=sk_test...
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
DB_HOST=db
DB_PORT=5432
```

### Запуск приложения в контейнерах

Запуск docker-compose:

```bash
docker-compose up -d
```

Выполнить миграции:

```bash
docker-compose exec web python manage.py migrate
```

Создать суперюзера:

```bash
docker-compose exec web python manage.py createsuperuser
```

### Тестирование

Проект доступен по адресу http://84.252.143.211/

Админка: http://84.252.143.211/admin/

```bash
username: admin
password: admin
```
