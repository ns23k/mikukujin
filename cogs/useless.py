from discord.ext import commands
import requests
import random


def anime_fact(token: str) -> str:
    url = "https://waifu.it/api/v4/fact"
    response = requests.get(url, headers={
        "Authorization": token,
    })
    return response.json()["fact"]


class Useless(commands.Cog):
    def __init__(self, bot, token):
        self.token = token
        self.bot = bot

    @commands.hybrid_command()
    async def fact(self, ctx: commands.Context):
        """fact about anime"""
        await ctx.send(anime_fact(self.token))

    @commands.command()
    async def mahi(self, ctx: commands.Context):
        """Bole jo koyal"""
        await ctx.message.delete()
        await ctx.send(random.choice(["https://media.tenor.com/xKeJyC9B4IkAAAAM/bole-jo-koyal.gif", "https://media"
                                                                                                    ".tenor.com"
                                                                                                    "/TAqoJiVSpb4AAAAM/vintage-mahi-gif.gif", "https://media.tenor.com/GAPX3IWIbDYAAAAM/rohit-sharma-virat-kohli.gif", "https://media.tenor.com/vh2htOrwf-0AAAAM/uppal-balu-uppal-bal.gif", ]))