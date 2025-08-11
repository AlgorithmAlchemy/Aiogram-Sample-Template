# 🚀 Быстрый старт

## Установка и настройка

### 1. Клонирование репозитория
```bash
git clone <your-repo-url>
cd Sample-Template-Aiogram-2.x
```

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Настройка переменных окружения
```bash
# Скопируйте пример файла
cp env.example .env

# Отредактируйте .env файл
nano .env
```

**Обязательные настройки:**
```env
BOT_TOKEN=your_bot_token_here
OWNER_IDS=your_admin_id_here
CHAT_ID=your_chat_id_here
```

### 4. Запуск бота
```bash
# Windows
python main.py

# Linux/Mac
python3 main.py
```

## 🎯 Основные возможности

### ✅ Что уже готово:
- **18 базовых команд** в отдельных модулях
- **FSM состояния** для многошаговых диалогов
- **API wrappers** для интеграции внешних сервисов
- **Middleware система** для расширения функциональности
- **Event hooks** для кастомизации жизненного цикла
- **База данных** с моделями пользователей и статистики
- **Inline клавиатуры** для интерактивности
- **Планировщик задач** для автоматизации
- **Система логирования** для отладки

### 📁 Структура команд:
```
handlers/users/message/commands/
├── start.py          # /start - запуск бота
├── menu.py           # /menu - главное меню
├── help.py           # /help - справка
├── profile.py        # /profile - профиль пользователя
├── settings.py       # /settings - настройки
├── about.py          # /about - о боте
├── version.py        # /version - версия
├── status.py         # /status - статус бота
├── ping.py           # /ping - проверка соединения
├── uptime.py         # /uptime - время работы
├── commands.py       # /commands - список команд
├── feedback.py       # /feedback - отзыв
├── support.py        # /support - поддержка
├── echo.py           # echo - обработка текста
├── register.py       # /register - регистрация (FSM)
├── weather.py        # /weather - погода (API)
├── ban_user.py       # /ban_user - бан (админ)
├── unban_user.py     # /unban_user - разбан (админ)
├── warn_user.py      # /warn_user - предупреждение (админ)
├── stats.py          # /stats - статистика (админ)
└── users.py          # /users - список пользователей (админ)
```

## 🔧 Быстрая настройка

### Добавление новой команды:
1. Создайте файл в `handlers/users/message/commands/`
2. Добавьте импорт в `__init__.py`
3. Используйте декоратор `@dp.message_handler(commands=['your_command'])`

### Использование FSM:
```python
from states.user.registration import RegistrationStates

@dp.message_handler(commands=['survey'])
async def start_survey(message: types.Message, state: FSMContext):
    await state.set_state(RegistrationStates.waiting_for_name)
    await message.answer("Как вас зовут?")
```

### Интеграция API:
```python
from utils.api_wrappers.weather_api import WeatherAPIWrapper

weather_api = WeatherAPIWrapper(api_key="your_api_key")
weather_data = await weather_api.get_weather("Москва")
```

### Создание клавиатуры:
```python
from keyboards.inline.keyboards import MainKeyboards

keyboard = MainKeyboards.create_keyboard([
    [("Кнопка 1", "btn1"), ("Кнопка 2", "btn2")],
    [("Кнопка 3", "btn3")]
])
```

## 🎨 Кастомизация

### Изменение текстов:
- Отредактируйте `data/config.py`
- Измените `help_text` и `admin_help_text`

### Добавление middleware:
```python
from utils.middleware.custom_middleware import LoggingMiddleware
dp.middleware.setup(LoggingMiddleware())
```

### Настройка event hooks:
```python
from utils.hooks.event_hooks import EventHooks

@event_hooks.startup_hook
async def custom_startup():
    print("Bot started!")
```

## 📊 Мониторинг

### Логи:
- Файл: `bot.log`
- Уровень: настраивается в `.env`

### Статистика:
- Команда: `/stats` (для админов)
- Автоматическая отправка: ежедневно в 9:00

### База данных:
- Файл: `data/botBD.db`
- Модели: `models/user.py`

## 🚨 Безопасность

### Обязательно:
- ✅ Никогда не коммитьте `.env` файл
- ✅ Используйте сильные API ключи
- ✅ Ограничьте доступ администраторов
- ✅ Регулярно обновляйте зависимости

### Рекомендуется:
- 🔒 Используйте HTTPS для webhook
- 🔒 Настройте firewall
- 🔒 Мониторьте логи на подозрительную активность

## 🆘 Поддержка

### Полезные команды:
- `/help` - справка по командам
- `/status` - статус бота
- `/version` - версия бота

### Отладка:
- Проверьте логи в `bot.log`
- Убедитесь, что все переменные окружения установлены
- Проверьте подключение к базе данных

### Частые проблемы:
1. **Бот не отвечает**: проверьте `BOT_TOKEN`
2. **Ошибки БД**: проверьте права доступа к папке `data/`
3. **Middleware не работает**: проверьте импорты в `loader.py`

## 🎉 Готово!

Ваш бот готов к использованию! 

**Следующие шаги:**
1. Протестируйте все команды
2. Настройте дополнительные API ключи
3. Кастомизируйте под ваши нужды
4. Разверните на сервере

**Дополнительная документация:**
- `README.md` - полная документация
- `examples/usage_examples.py` - примеры использования
- `handlers/` - примеры обработчиков
