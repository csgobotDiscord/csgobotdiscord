"""
Ког с командами для создателей бота.
"""

from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.is_owner
    @commands.group(name = "cogs",
                    aliases = ("cog", "module", "modules", "ког", "коги"))
    async def cogs(self, ctx: commands.Cog) -> None:
        pass


def setup(bot: commands.Bot) -> None:
    bot.add_cog(Owner(bot))