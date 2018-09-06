from dinnerplate import BaseCog
import discord
from discord.ext import commands


class Info(BaseCog):

    def __init__(self, bot):
        super().__init__(bot)

    @commands.command()
    async def website(self, ctx):
        """
        Returns the university website
        """
        await ctx.send("http://www.aber.ac.uk/en/")


setup = Info.setup
