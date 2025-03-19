from telebot.types import Message

from config_data.config import DEFAULT_COMMANDS
from loader import bot


@bot.message_handler(commands=["help"])
async def bot_help(message: Message) -> None:
    """
    Обрабатывает команду /help и отправляет список доступных команд.

    :param message: Сообщение от пользователя.
    """
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    await bot.reply_to(message, "\n".join(text))
