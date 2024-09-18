import discord
from discord.ext.commands import hybrid_command
import datetime
from discord.ext import commands
import aiohttp
import random
import praw

reddit = praw.Reddit(
    client_id="pLYhQqgfPuq4piJarBO6PQ",
    client_secret="yUqfp3kHf_0EwrVI-WNPB05XMskR0Q",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    check_for_async=False,
)


class Image(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @hybrid_command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.thecatapi.com/v1/images/search") as r:
                data = await r.json()
                print(data)
                embed_meow = discord.Embed(
                    title="Cat!",
                    description=f"[*Meow~*]",
                    timestamp=datetime.datetime.utcnow(),
                    color=discord.Color.red(),
                )
                embed_meow.set_image(url=data[0]["url"])
                embed_meow.set_footer(
                    text="{}".format(ctx.author.name), icon_url=ctx.author.avatar.url
                )
                embed_meow.set_author(name=ctx.me.name, icon_url=ctx.me.avatar.url)
            await ctx.reply(embed=embed_meow)

    @commands.hybrid_command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://random.dog/woof.json") as r:
                data = await r.json()
                embed_woof = discord.Embed(
                    title="Dog!",
                    description=f'[*Woof~*]({data["url"]})',
                    timestamp=datetime.datetime.utcnow(),
                    color=discord.Color.red(),
                )
                embed_woof.set_image(url=data["url"])
                embed_woof.set_footer(
                    text="{}".format(ctx.author.name),
                    icon_url=ctx.author.avatar.url,
                )
                embed_woof.set_author(
                    name=ctx.me.name, icon_url=ctx.me.avatar.url
                )
            await ctx.reply(embed=embed_woof)

    @commands.hybrid_command()
    async def fox(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://randomfox.ca/floof/") as r:
                data = await r.json()
                embed_floof = discord.Embed(
                    title="Fox!",
                    description=f'[*Floof~*]({data["image"]})',
                    timestamp=datetime.datetime.utcnow(),
                    color=discord.Color.red(),
                )
                embed_floof.set_image(url=data["image"])
                embed_floof.set_footer(
                    text="{}".format(ctx.author.name),
                    icon_url=ctx.author.avatar.url,
                )
                embed_floof.set_author(
                    name=ctx.me.name, icon_url=ctx.me.avatar.url
                )
            await ctx.reply(embed=embed_floof)

    @commands.hybrid_command()
    async def duck(self, ctx):
        subreddit = reddit.subreddit("duck")
        all_subs = []
        top = subreddit.top(limit=5)
        for submission in top:
            all_subs.append(submission)
        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url
        embed = discord.Embed(
            title=f"Duck!",
            description=f"[*{name}*]({url})",
            timestamp=datetime.datetime.utcnow(),
            color=discord.Color.red(),
        )
        embed.set_image(url=url)
        embed.set_author(name=ctx.me.name, icon_url=ctx.me.avatar.url)
        embed.set_footer(
            text="{}".format(ctx.author.name), icon_url=ctx.author.avatar.url
        )
        await ctx.reply(embed=embed)

    @commands.hybrid_command()
    async def frog(self, ctx):
        subreddit = reddit.subreddit("frogs")
        all_subs = []
        top = subreddit.top(limit=5)
        for submission in top:
            all_subs.append(submission)
        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url
        embed = discord.Embed(
            title=f"Frog!",
            description=f"[*{name}*]({url})",
            timestamp=datetime.datetime.utcnow(),
            color=discord.Color.red(),
        )
        embed.set_image(url=url)
        embed.set_author(name=ctx.me.name, icon_url=ctx.me.avatar.url)
        embed.set_footer(
            text="{}".format(ctx.author.name), icon_url=ctx.author.avatar.url
        )
        await ctx.reply(embed=embed)

    @commands.hybrid_command()
    async def ferret(self, ctx):
        subreddit = reddit.subreddit("ferrets")
        all_subs = []
        top = subreddit.top(limit=5)
        for submission in top:
            all_subs.append(submission)
        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url
        embed = discord.Embed(
            title=f"Ferret!",
            description=f"[*{name}*]({url})",
            timestamp=datetime.datetime.utcnow(),
            color=discord.Color.red(),
        )
        embed.set_image(url=url)
        embed.set_author(name=ctx.me.name, icon_url=ctx.me.avatar.url)
        embed.set_footer(
            text="{}".format(ctx.author.name), icon_url=ctx.author.avatar.url
        )
        await ctx.reply(embed=embed)

    @commands.hybrid_command()
    async def awwnime(self, ctx):
        subreddit = reddit.subreddit("awwnime")
        all_subs = []
        top = subreddit.top(limit=5)
        for submission in top:
            all_subs.append(submission)
        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url
        embed = discord.Embed(
            title=f"Moe!",
            description=f"[*{name}*]({url})",
            timestamp=datetime.datetime.utcnow(),
            color=discord.Color.red(),
        )
        embed.set_image(url=url)
        embed.set_author(name=ctx.me.name, icon_url=ctx.me.avatar.url)
        embed.set_footer(
            text="{}".format(ctx.author.name), icon_url=ctx.author.avatar.url
        )
        await ctx.reply(embed=embed)
