#!/bin/bash

# Скрипт для быстрого запуска проекта VILLA
# Использование: ./start_project.sh

echo "🚀 Запуск проекта VILLA..."
echo "================================"

# Проверяем, находимся ли мы в правильной директории
if [ ! -f "manage.py" ]; then
    echo "❌ Ошибка: manage.py не найден!"
    echo "Перейдите в директорию core проекта VILLA"
    exit 1
fi

# Активируем виртуальное окружение
if [ -d "venv" ]; then
    echo "✅ Активируем виртуальное окружение..."
    source venv/bin/activate
else
    echo "❌ Виртуальное окружение не найдено!"
    echo "Создайте его командой: python3 -m venv venv"
    exit 1
fi

# Проверяем зависимости
echo "📦 Проверяем зависимости..."
pip install -r requirements.txt

# Применяем миграции
echo "🗄️ Применяем миграции..."
python manage.py migrate

# Собираем статические файлы
echo "🎨 Собираем статические файлы..."
python manage.py collectstatic --noinput

# Запускаем сервер
echo "🌐 Запускаем сервер разработки..."
echo "Сайт будет доступен по адресу: http://localhost:8000"
echo "Для остановки сервера нажмите Ctrl+C"
echo "================================"

python manage.py runserver 0.0.0.0:8000

