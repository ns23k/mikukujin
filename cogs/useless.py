from discord import *
from discord.ext import commands
import requests


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
        await ctx.send(anime_fact(self.token))
