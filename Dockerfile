FROM python:3.11-slim

WORKDIR /app

# Обновляем pip
RUN pip install --upgrade pip setuptools wheel

# Копируем и ставим зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Создаём пользователя
RUN useradd -m -u 1000 django && chown -R django:django /app
USER django

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
