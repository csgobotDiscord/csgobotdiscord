"""
Главный файл бота, в котором запускается бот.
"""

import os
import site
site.addsitedir(os.getcwd())  # Добавляем рабочую директорию в sys.path чтобы не было бед с импортами

import discord
from discord.ext import commands

from source.resources.config import config
from source.utils import loaders
from source.utils import errors

bot = commands.Bot(**config["bot"]["settings"])


@bot.event
async def on_ready() -> None:
    print(f"[Бот: {bot.user} с ID: {bot.user.id}] Запуск произошёл успешно!")
    loaders.load_cogs(bot = bot, cogs_list = config["bot"]["cogs"]["list"], cogs_path = config["bot"]["cogs"]["path"])


@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError) -> None:
    await errors.handler.command_error_detection(ctx, error)


bot.run(config["bot"]["token"])
