import discord
from discord.ext.commands import hybrid_command
import datetime
from discord.ext import commands
import aiohttp
import requests
import random


def create_embed(ctx, title, name, url):
    embed = discord.Embed(
        title=f"{title}",
        description=f"[*{name}*]({url})",
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.red(),
    )
    embed.set_image(url=url)
    embed.set_author(name=ctx.me.name, icon_url=ctx.me.avatar.url)
    embed.set_footer(
        text="{}".format(ctx.author.name), icon_url=ctx.author.avatar.url
    )
    return embed


def get_husbando(token: str) -> str:
    url = "https://waifu.it/api/v4/husbando"
    response = requests.get(url, headers={
        "Authorization": token,
    })
    data = response.json()
    return data


class Image(commands.Cog):
    """Image Stuff"""

    def __init__(self, bot: commands.Bot, TOKEN):
        self.TOKEN = TOKEN
        self.bot = bot

    @hybrid_command()
    async def cat(self, ctx: discord.ext.commands.Context):
        """Sends an image of cat"""
        msg = await ctx.send("....")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.thecatapi.com/v1/images/search") as r:
                data = await r.json()
                embed_meow = create_embed(ctx, "Cat!", "Meow~~", url=data[0].get("url"))
            await msg.edit(content=" ", embed=embed_meow)

    @commands.hybrid_command()
    async def dog(self, ctx: discord.ext.commands.Context):
        """Sends an image of dog"""
        msg = await ctx.send("....")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://random.dog/woof.json") as r:
                data = await r.json()
                embed_woof = create_embed(ctx, "Dog!", name="*Woof~*", url=data.get("url"))
            await msg.edit(content="", embed=embed_woof)

    @commands.hybrid_command()
    async def fox(self, ctx):
        """Sends an image of fox"""
        msg = await ctx.send("....")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://randomfox.ca/floof/") as r:
                data = await r.json()
                embed_floof = create_embed(ctx, title="Fox!", name="*Floof~*", url=data.get("image"))
            await msg.edit(content="", embed=embed_floof)

    @commands.hybrid_command()
    async def duck(self, ctx):
        """Sends an image of ducky duck"""
        msg = await ctx.send("....")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://random-d.uk/api/v2/random") as r:
                data = await r.json()
                ducky_embed = create_embed(ctx, title="Duck!", name="*Quack~*", url=data.get("url"))
            await msg.edit(content="", embed=ducky_embed)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.hybrid_command()
    async def waifu(self, ctx):
        """Pretty self-explanatory I guess"""
        msg = await ctx.send("....")
        rand = random.randint(0, 1)
        if rand == 0:
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://api.waifu.im/search") as r:
                    data = await r.json()
                waif_embed = create_embed(ctx, title="Kawaiii!", name="url", url=data.get("images")[0].get("url"))
        else:
            endpoint = "https://waifu.it/api/v4/waifu"
            response = requests.get(endpoint, headers={
                "Authorization": self.TOKEN,
            })
            url = response.json().get("image").get("large")
            waif_embed = create_embed(ctx, title="Kawaiii!", name="url", url=url)

        await msg.edit(content="", embed=waif_embed)
        await msg.add_reaction("⬆️")
        await msg.add_reaction("⬇️")

    @commands.hybrid_command()
    async def husbando(self, ctx):
        """Pretty self-explanatory too I guess"""
        msg = await ctx.send("....")
        data = get_husbando(self.TOKEN)
        waif_embed = create_embed(ctx, title="Kawaiii!", name="url", url=data.get("image").get("large"))
        await msg.edit(content="", embed=waif_embed)
        await msg.add_reaction("⬆️")
        await msg.add_reaction("⬇️")
