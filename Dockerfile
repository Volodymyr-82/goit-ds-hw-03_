FROM ubuntu:latest
LABEL authors="Vova"

ENTRYPOINT ["top", "-b"]

# 🐍 Базовий Python-образ
FROM python:3.11-slim

# 🗂️ Робоча директорія всередині контейнера
WORKDIR /app

# 📋 Копіюємо файли в контейнер
COPY . .

# 📦 Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# 🏁 Команда запуску
CMD ["python", "main.py"]
