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
        await ctx.send(embed = discord.Embed(title = "Информация о пользователе:", description = "Имя+Дискриминатор:\nАйди:\nБаланс:\nДата регистрации:\nЗвание:\n Опыт:\nДоллары:\nТекущее оружее:")                                             


def setup(bot: commands.Bot) -> None:
    bot.add_cog(Economy(bot))
