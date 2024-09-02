from discord.ext import commands
from cogs.tictactoe import TicTacToe
import discord
from cogs.image import ImageMaker
from cogs.f import Image
from cogs.help import Help
import imageio_ffmpeg as f
from cogs.tts import tts
from cogs.anime import Anime
import asyncio
import aiohttp
import socket
from cogs.test import test
from cogs.akinator import Aki
from discord import *
from cogs.music import music
from cogs.mod import Moderation
import requests
from cogs.rockp import rockpaperscissors
from cogs.Minecraft.info import Info
from cogs.Minecraft.profile import Profile


class hm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


class base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_quote(self):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = response.json()
        quote = json_data[0]["q"] + " -" + json_data[0]["a"]
        return quote

    @app_commands.command()
    async def quote(self, msg: discord.Interaction):
        quote = self.get_quote()
        embed = discord.Embed(title="Wonder thoughts", color=discord.Color.red())
        # embed.set_image(url=imgdat)
        embed.add_field(name="Tada! ", value=quote, inline=False)
        await msg.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command()
    async def ping(self, ctx: discord.Interaction):
        print("me is running" + str(round(self.bot.latency * 1000)))
        await ctx.response.send_message(
            f"""Pong! {round(self.bot.latency * 1000)} ms""", ephemeral=True
        )

    @commands.Cog.listener()
    async def on_message(self, msg):
        pass


class bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=["m.", "l!"],
            intents=discord.Intents.all(),
            activity=discord.Game("m.help"),
        )

    def get_quote(self):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = response.json()
        quote = json_data[0]["q"] + " -" + json_data[0]["a"]
        return quote

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.reply(
                "aisa koyi command nhi hai bewakoof <:cheems:998927712758534195>"
            )
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(
                title=f"Slow it down bro!",
                description=f"Try again in {error.retry_after:.2f}s.",
                color=discord.Colour.black())
            await ctx.send(embed=em)
            print("cooldown")
        else:
            print(error)

    async def on_raw_reaction_add(payload):
        pass

    async def setup_hook(self):
        await bot.add_cog(TicTacToe(bot))
        await bot.add_cog(ImageMaker(bot))
        await bot.add_cog(Image(bot))
        await bot.add_cog(Help(bot))
        await bot.add_cog(tts(bot))
        await bot.add_cog(Anime(bot))
        await bot.add_cog(Aki(bot))
        await bot.add_cog(base(bot))
        await bot.add_cog(music(bot))
        await bot.add_cog(Moderation(bot))
        await bot.add_cog(rockpaperscissors(bot))
        await bot.add_cog(test(bot))
        await bot.add_cog(hm(bot))
        await bot.add_cog(Info(bot))
        await bot.add_cog(Profile(bot))
        await self.tree.sync()
        print(f"Synced slash commands for {self.user}.")

    async def on_ready(self):
        print(f.get_ffmpeg_exe())


bot = bot()

# tree = app_commands.CommandTree(bot)
# @tree.command( name = 'tester', description='testing') #guild specific slash command

TOKEN = "OTY2MzQyODkxMjA1MTY1MTg3.GeDBwP.YTVL25ZLzQ9HMWAzI1NnJqo7lfVQXqgtgyyJd4"


async def main() -> None:
    async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(
                resolver=aiohttp.AsyncResolver(), family=socket.AF_INET
            )
    ) as http_session:
        async with bot:
            bot.http_session = http_session

            await bot.start(TOKEN)


asyncio.run(main())
