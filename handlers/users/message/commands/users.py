from aiogram import types
from aiogram.types import ParseMode
import logging
from datetime import datetime

from data.config import config
from loader import dp
from models.user import User
from filters.admin_filter import AdminFilter

logger = logging.getLogger(__name__)


class UsersCommand:
    """Обработчик команды /users"""
    
    @staticmethod
    async def handle(message: types.Message):
        """Обработчик команды /users - список пользователей"""
        if message.from_user.id not in config.admin.owner_ids:
            await message.answer("❌ У вас нет прав администратора!")
            return
        
        try:
            # Получаем последних 10 пользователей
            recent_users = User.select().order_by(User.created_at.desc()).limit(10)
            
            users_text = "<b>👥 Последние пользователи</b>\n\n"
            
            for user in recent_users:
                status = "🚫" if user.is_banned else "✅"
                username = f"@{user.username}" if user.username else "Не указан"
                users_text += (
                    f"{status} <b>{user.first_name}</b> "
                    f"(ID: <code>{user.user_id}</code>)\n"
                    f"Username: {username}\n"
                    f"Зарегистрирован: {user.created_at.strftime('%d.%m.%Y')}\n"
                    f"Предупреждений: {user.warnings}\n\n"
                )
            
            # Добавляем общую статистику
            total_users = User.select().count()
            active_users = User.select().where(
                User.last_activity >= datetime.now().replace(
                    hour=0, minute=0, second=0, microsecond=0
                )
            ).count()
            
            users_text += f"""
<b>📊 Общая статистика:</b>
• Всего пользователей: {total_users}
• Активных сегодня: {active_users}

<i>Показаны последние 10 зарегистрированных пользователей.</i>
"""
            
            await message.answer(
                users_text,
                parse_mode=ParseMode.HTML
            )
            
        except Exception as e:
            logger.error(f"Error getting users list: {e}")
            await message.answer("❌ Ошибка при получении списка пользователей")


# Регистрация обработчика
@dp.message_handler(AdminFilter(), commands=['users'])
async def users_cmd(message: types.Message):
    await UsersCommand.handle(message)
