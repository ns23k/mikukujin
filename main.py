from discord.ext import commands
import discord
import asyncio
import aiohttp
import selectors
from dotenv import load_dotenv
import socket
import os

from cogs.image import Image
from cogs.help import Help
from cogs.akinator import Aki
from cogs.useless import Useless
from cogs.aninteractions import AnInteraction
from cogs.quespaper import QuesPaper


class Bot(commands.Bot):
    def __init__(self, husbando_token):
        super().__init__(
            command_prefix=["m."],
            intents=discord.Intents.all(),
            activity=discord.Game("with your mom"),
        )
        self.husbando_token = husbando_token

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.reply(
                "aisa koyi command nhi hai bewakoof <:cheems:998927712758534195>"
            )
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(
                title=f"Slow it down bro!",
                description=f"Try again in {error.retry_after:.2f}s.",
                color=discord.Colour.black(),
            )
            await ctx.send(embed=em)
        else:
            print(error)

    async def setup_hook(self):
        await self.add_cog(Image(bot, self.husbando_token))
        await self.add_cog(Help(bot))
        await self.add_cog(Aki(bot))
        await self.add_cog(Useless(bot, self.husbando_token))
        await self.add_cog(AnInteraction(bot, self.husbando_token))
        await self.add_cog(QuesPaper(bot))
        await self.tree.sync()
        print(f"Synced slash commands for {self.user}.")


load_dotenv()
HUSBANDO_TOKEN = os.environ.get("HUSBANDO")

bot = Bot(HUSBANDO_TOKEN)

TOKEN = os.environ.get("TOKEN")


class MyPolicy(asyncio.DefaultEventLoopPolicy):
    def new_event_loop(self):
        selector = selectors.SelectSelector()
        return asyncio.SelectorEventLoop(selector)


async def main() -> None:
    async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(
                resolver=aiohttp.AsyncResolver(), family=socket.AF_INET
            )
    ) as http_session:
        async with bot:
            bot.http_session = http_session

            await bot.start(TOKEN)


asyncio.set_event_loop_policy(MyPolicy())
asyncio.run(main())
