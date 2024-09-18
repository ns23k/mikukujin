from discord.ext import commands
import discord
import asyncio
import aiohttp
import selectors
from dotenv import load_dotenv
import socket
from cogs.image import Image


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=["m."],
            intents=discord.Intents.all(),
            activity=discord.Game("with your Mom"),
        )

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
            print("cooldown")
        else:
            print(error)

    async def setup_hook(self):
        await self.add_cog(Image(bot))
        await self.tree.sync()
        print(f"Synced slash commands for {self.user}.")


bot = Bot()

TOKEN = load_dotenv("TOKEN")


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
