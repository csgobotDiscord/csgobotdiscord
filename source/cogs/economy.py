"""
Ког экономики для бота.
"""

from discord.ext import commands


class Economy(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.group(name = "statistics")
    async def statistics(self, ctx: commands.Context) -> None:
        pass

    @statistics.command(name = "profile",
                        aliases = ("user", "профиль", "пользователь"),
                        brief = "Команда для просмотра информации о пользователе.",
                        usage = "statistics profile <пользователь: ID, @упоминание, имя#дискриминатор>")
    async def profile(self, ctx: commands.Context) -> None:
        pass


def setup(bot: commands.Bot) -> None:
    bot.add_cog(Economy(bot))