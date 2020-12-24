"""
Классы собственных исключений.
"""

from discord.ext import commands


class SubcommandIsNone(commands.CommandError):
    """
    Исключение, когда пользователь не указал подкоманду из группы команд
    """

    def __init__(self, commands_group):
        self.commands_group = commands_group