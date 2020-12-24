"""
Утилита для загрузки чего либо.
"""

from discord.ext import commands


def load_cogs(bot: commands.Bot, cogs_list: list, cogs_path: str) -> str:
    """
    Функция для загрузки когов бота.

    :param bot: Бот, для которого загружаются коги.
    :param cogs_list: Список когов, которые загружаются.
    :param cogs_path: Путь к когам, которые загружаются.
    """
    
    for cog in cogs_list:
        try:
            bot.load_extension(name = f"{cogs_path}.{cog}")
            print(f"[Ког {cog}] Успешно загружен!")
        except (ImportError, AttributeError) as error:
            print(f"При загрузке кога {cog} произошла ошибка:\n{error}")