# Django DRF Book Management API

Простой REST API для управления книгами с JWT аутентификацией, построенный на Django и Django REST Framework.

## 🚀 Особенности

- ✅ JWT аутентификация (access/refresh токены)
- ✅ CRUD операции для книг
- ✅ Управление пользователями (регистрация, профиль, обновление)
- ✅ Безопасный logout с blacklist токенов
- ✅ Пагинация и фильтрация
- ✅ Django Admin панель

## 📦 Технологии

- Python 3.8+
- Django 4.x
- Django REST Framework
- Simple JWT
- SQLite (для разработки)

Установка зависимостей
pip install -r requirements.txt


Получение токенов
POST /api/token/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}

Обновление токена
POST /api/token/refresh/
{
    "refresh": "your_refresh_token"
}

Проверка токена
POST /api/token/verify/
{
    "token": "your_access_token"
}


📚 API Endpoints
Аутентификация пользователя
POST /api/user/register/ - Регистрация нового пользователя
POST /api/user/login/ - Вход в систему (получение токенов)
POST /api/user/logout/ - Выход из системы
GET /api/user/profile/ - Получение профиля пользователя
PUT/PATCH /api/user/update/ - Обновление профиля

Книги (CRUD)
GET /api/book/book_list/ - Список всех книг
GET /api/book/book_detail/<id>/ - Детали книги
POST /api/book/book_create/ - Создание новой книги
PUT/PATCH /api/book/book_update/<id>/ - Обновление книги
DELETE /api/book/book_remove/<id>/ - Удаление книги

🛡️ Права доступа
Endpoint	Метод	Доступ
/api/book/book_list/	GET	Все пользователи
/api/book/book_create/	POST	Только авторизованные
/api/book/book_update/<id>/	PUT/PATCH	Владелец книги или админ
/api/book/book_remove/<id>/	DELETE	Владелец книги или админ
/api/user/profile/	GET	Только авторизованные
/api/user/update/	PUT/PATCH	Только свой профиль
