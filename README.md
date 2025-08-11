# 🤖 Aiogram 2.x Template

**Современный шаблон для создания Telegram ботов на aiogram 2.x**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Aiogram](https://img.shields.io/badge/Aiogram-2.x-green.svg)](https://aiogram.dev)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 Особенности

- **Готовая структура** проекта с логичной организацией файлов
- **Примеры всех компонентов**:
  - Команды (`/start`, `/help`, `/profile`)
  - Inline клавиатуры с callback обработчиками
  - FSM (машины состояний) для сложных диалогов
  - Middleware для логирования и обработки ошибок
  - Система администраторов с правами доступа
- **Преднастроенные компоненты**:
  - Логирование с настраиваемыми уровнями
  - Конфигурация через переменные окружения (.env)
  - Планировщик задач (APScheduler)
  - База данных SQLite с Peewee ORM
  - Обработка ошибок и исключений
- **Безопасность**:
  - Защита конфиденциальных данных
  - Система прав доступа
  - Валидация входных данных

## 🛠 Технологии

- **Python 3.8+**
- **Aiogram 2.25.2** - современный асинхронный фреймворк для Telegram Bot API
- **SQLite + Peewee** - легкая база данных с ORM
- **APScheduler** - планировщик задач
- **python-dotenv** - управление переменными окружения

## 📦 Быстрый старт

### 1. Клонирование репозитория
```bash
git clone https://github.com/your-username/aiogram-2x-template.git
cd aiogram-2x-template
```

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Настройка конфигурации
```bash
cp env.example .env
# Отредактируйте .env файл, добавив свои данные
```

### 4. Запуск бота
```bash
python main.py
```

## 🔒 Безопасность

**ВАЖНО**: Никогда не коммитьте файл `.env` в репозиторий!

### Настройка переменных окружения:

1. **Скопируйте** `env.example` в `.env`
2. **Заполните** в `.env` ваши реальные данные:
   - `BOT_TOKEN` - токен от @BotFather
   - `OWNER_IDS` - ID администраторов (через запятую)
   - `CHAT_ID` - ID чата/группы
   - `SUPPORT_USERNAME` - username поддержки

### Получение необходимых данных:

- **Токен бота**: @BotFather → `/newbot`
- **ID пользователя**: @userinfobot
- **ID группы**: @getidsbot

## 📂 Структура проекта

```
├── data/
│   ├── config.py          # Конфигурация и настройки
│   └── image/             # Изображения и медиафайлы
├── handlers/
│   ├── users/             # Обработчики для пользователей
│   │   ├── message/       # Обработчики сообщений
│   │   └── callback/      # Обработчики callback кнопок
│   ├── groups/            # Обработчики для групп
│   ├── supergroups/       # Обработчики для супергрупп
│   └── errors/            # Обработчики ошибок
├── keyboards/
│   ├── inline/            # Inline клавиатуры
│   └── reply/             # Reply клавиатуры
├── models/                # Модели базы данных
├── states/                # FSM состояния
├── utils/                 # Утилиты и вспомогательные функции
├── filters/               # Фильтры для обработчиков
├── loader.py              # Инициализация бота и диспетчера
├── main.py                # Точка входа
├── requirements.txt       # Зависимости
├── .env.example           # Пример конфигурации
├── .gitignore             # Исключения Git
└── README.md              # Документация
```

## 🎯 Основные команды

### Пользовательские команды:
- `/start` - Запустить бота и показать главное меню
- `/menu` - Показать главное меню
- `/help` - Показать справку
- `/about` - Информация о боте
- `/profile` - Показать ваш профиль
- `/settings` - Открыть настройки

### Админские команды:
- `/stats` - Статистика бота
- `/users` - Список пользователей
- `/ban` - Забанить пользователя
- `/unban` - Разбанить пользователя

## 🔧 Настройка и кастомизация

### Добавление новых команд:
1. Создайте обработчик в `handlers/users/message/`
2. Зарегистрируйте его в `handlers/__init__.py`
3. Добавьте команду в меню бота

### Создание новых клавиатур:
1. Добавьте функцию в `keyboards/inline/keyboards.py`
2. Создайте обработчик в `handlers/users/callback/`
3. Используйте в нужных обработчиках

### Работа с базой данных:
1. Создайте модель в `models/`
2. Используйте Peewee ORM для запросов
3. Не забудьте создать миграции

## 🚀 Развертывание

### Локальная разработка:
```bash
python main.py
```

### Продакшн (с Redis):
1. Установите Redis
2. Настройте переменные Redis в `.env`
3. Запустите с помощью systemd или supervisor

### Docker (опционально):
```bash
docker build -t aiogram-bot .
docker run -d --name bot aiogram-bot
```

## 📝 Примеры использования

### Создание простого обработчика:
```python
from aiogram import types
from loader import dp

@dp.message_handler(commands=['hello'])
async def hello_handler(message: types.Message):
    await message.answer("Привет! 👋")
```

### Создание inline клавиатуры:
```python
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_example_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Кнопка", callback_data="button"))
    return keyboard
```

### Работа с FSM:
```python
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class ExampleStates(StatesGroup):
    waiting_for_input = State()

@dp.message_handler(state=ExampleStates.waiting_for_input)
async def process_input(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Спасибо за ввод!")
```

## 🤝 Вклад в проект

1. Fork репозитория
2. Создайте ветку для новой функции (`git checkout -b feature/amazing-feature`)
3. Commit изменения (`git commit -m 'Add amazing feature'`)
4. Push в ветку (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. См. файл `LICENSE` для получения дополнительной информации.

## 🆘 Поддержка

Если у вас есть вопросы или проблемы:

- 📧 Создайте Issue в GitHub
- 💬 Обратитесь к документации aiogram
- 🔗 Присоединитесь к сообществу aiogram

---

**Создано с ❤️ для сообщества aiogram**
