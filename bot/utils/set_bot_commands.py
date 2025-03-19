from telebot.types import BotCommand
from config_data.config import DEFAULT_COMMANDS
from telebot.async_telebot import AsyncTeleBot


async def set_default_commands(bot: AsyncTeleBot) -> None:
    """
    Устанавливает команды по умолчанию для телеграм-бота.

    :param bot: Экземпляр телеграм-бота.
    """
    await bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )
