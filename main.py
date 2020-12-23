"""
Главный файл бота, в котором запускается бот.
"""

import discord
from discord.ext import commands

from resources.config import config


bot = commands.Bot(**config["bot"]["settings"])


@bot.event
async def on_ready() -> None:
    print(f"[Бот: {bot.user} с ID: {bot.user.id}] Запуск произошёл успешно!")


bot.run(config["bot"]["token"])