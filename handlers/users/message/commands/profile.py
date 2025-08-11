from aiogram import types
from aiogram.types import ParseMode
import logging

from data.config import config
from loader import dp
from models.user import User, UserStats

logger = logging.getLogger(__name__)


class ProfileCommand:
    """Обработчик команды /profile"""
    
    @staticmethod
    async def handle(message: types.Message):
        """Обработчик команды /profile - показывает профиль пользователя"""
        user = message.from_user
        
        try:
            # Получаем данные из БД
            db_user = User.get_or_none(User.user_id == user.id)
            
            if db_user:
                # Получаем статистику
                stats = UserStats.get_or_none(UserStats.user == db_user)
                
                # Определяем статус пользователя
                user_status = ('👑 Администратор' if user.id in config.admin.owner_ids 
                              else '👤 Пользователь')
                
                # Определяем статус аккаунта
                account_status = ('🚫 Забанен' if db_user.is_banned else '✅ Активен')
                
                profile_text = f"""
<b>📋 Профиль пользователя</b>

<b>Основная информация:</b>
• ID: <code>{user.id}</code>
• Имя: {user.first_name}
• Фамилия: {user.last_name or 'Не указана'}
• Username: @{user.username or 'Не указан'}
• Premium: {'✅ Да' if getattr(user, 'is_premium', False) else '❌ Нет'}

<b>Статус:</b> {user_status}

<b>Дата регистрации:</b> {db_user.created_at.strftime('%d.%m.%Y %H:%M')}
<b>Последняя активность:</b> {db_user.updated_at.strftime('%d.%m.%Y %H:%M')}

<b>Статистика:</b>
• Сообщений отправлено: {stats.messages_sent if stats else 0}
• Команд использовано: {stats.commands_used if stats else 0}
• Файлов отправлено: {stats.files_sent if stats else 0}
• Предупреждений: {db_user.warnings}

<b>Статус аккаунта:</b> {account_status}
"""
            else:
                profile_text = """
<b>📋 Профиль пользователя</b>

❌ <b>Ошибка:</b> Пользователь не найден в базе данных.

Попробуйте использовать команду /start для регистрации.
"""
            
            await message.answer(
                profile_text,
                parse_mode=ParseMode.HTML
            )
            
        except Exception as e:
            logger.error(f"Error getting profile for user {user.id}: {e}")
            await message.answer("❌ Ошибка при получении профиля")


# Регистрация обработчика
@dp.message_handler(commands=['profile'], chat_type='private')
async def profile_cmd(message: types.Message):
    await ProfileCommand.handle(message)
