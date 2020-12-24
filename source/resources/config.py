"""
Файл конфигурации с настройками бота, эмодзи, токеном.
"""

import discord


config = {
    "bot": {
        "settings": {
            "command_prefix": ">",
            "case_insensitive": False,
            "intents": discord.Intents.all() 
        },
        "cogs": {
            "list": ["economy"],
            "path": "source.cogs"
        },
        "token": "https://discord.com/developers"
    },
    "discord": {
        "interface": {
            "timezone": "ru",
            "timelocal": "%d.%m.%Y %H:%M:%S"
        }
    }
}
