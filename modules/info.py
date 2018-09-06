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

    @commands.command()
    async def source(self, ctx):
        """
        Source code for the bot
        """
        await ctx.send("http://www.github.com/DiNitride/AberBot\n"
                       f"If you want to contribute do {ctx.prefix}contributing")

    @commands.command()
    async def contributing(self, ctx):
        """
        Information about contributing
        """
        await ctx.send("If you wish to help contribute to the bot, then fork the repo on Github.\n"
                       "The bot is written in Python, using an awfully named framework called Dinnerplate, "
                       "which uses the discord.py (Rewrite) library to communicate with library.\n"
                       "If don't know any Python then I would reccomend practicing with some small projects of your "
                       "own first, but once you have the basics feel free to make yourself a module or "
                       "contribute to an existing one.")


setup = Info.setup
