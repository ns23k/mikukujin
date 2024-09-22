from discord.ext import commands
import discord
import requests
from typing import Optional


class API:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://waifu.it/api/v4/"

    def _base_request(self, endpoint):
        req = requests.get(self.base_url + endpoint, headers={
            "Authorization": self.token,
        })
        return req.json()

    def api_request(self, endpoint):
        return self._base_request(endpoint).get("url")


class AnInteraction(commands.Cog):
    """Anime Interaction shit"""

    def __init__(self, bot: commands.Bot, token) -> None:
        self.bot = bot
        self.api = API(token=token)

    def create_embed(self, ctx: commands.Context, title, name, url):
        embed = discord.Embed(
            title=f"{ctx.author.display_name} is {title}" + " " + name.display_name,
            color=discord.Color.red(),
        )
        embed.set_image(url=url)
        embed.set_author(name=ctx.me.name, icon_url=ctx.me.avatar.url)
        embed.set_footer(
            text="{}".format(ctx.author.name), icon_url=ctx.author.avatar.url
        )
        return embed

    async def base_message(self, ctx, endpoint, title, user):
        url = self.api.api_request(endpoint)
        if user is None:
            await ctx.reply(f"user bhi mention kr le pyare")
        else:
            await ctx.send(embed=self.create_embed(ctx, title=title, url=url, name=user))

    @commands.hybrid_command()
    async def angry(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "angry", "angry at", user)

    @commands.hybrid_command()
    async def baka(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "baka", "", user)

    @commands.hybrid_command()
    async def blush(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "blush", "blushing at", user)

    @commands.hybrid_command()
    async def bite(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "bite", "biting", user)

    @commands.hybrid_command()
    async def bonk(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "bonk", "bonking", user)

    @commands.hybrid_command()
    async def bully(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "bully", "bullying",user)

    @commands.hybrid_command()
    async def bye(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "bye", "saying bye to", user)

    @commands.hybrid_command()
    async def chase(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "chase", "chasing", user)

    @commands.hybrid_command()
    async def cheese(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "cheese", "", user)

    @commands.hybrid_command()
    async def cheer(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "cheer", "cheering", user)

    @commands.hybrid_command()
    async def cringe(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "cringe", "cringing at", user)

    @commands.hybrid_command()
    async def cry(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "cry", "crying for", user)

    @commands.hybrid_command()
    async def cuddle(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "cuddle", "cuddling", user)

    @commands.hybrid_command()
    async def dab(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "dab", "dabbing", user)

    @commands.hybrid_command()
    async def dance(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "dance", "dancing wit", user)

    @commands.hybrid_command()
    async def die(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "die", "", user)

    @commands.hybrid_command()
    async def disgust(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "disgust", "disgusted at", user)

    @commands.hybrid_command()
    async def facepalm(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "facepalm", "is facepalming at", user)

    @commands.hybrid_command()
    async def feed(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "feed", "feeding", user)

    @commands.hybrid_command()
    async def glomp(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "glomp", "glomping", user)

    @commands.hybrid_command()
    async def happy(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "happy", "happy at", user)

    @commands.hybrid_command()
    async def hi(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "hi", "saying hi to", user)

    @commands.hybrid_command()
    async def highfive(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "highfive", "is giving highfive to", user)

    @commands.hybrid_command()
    async def hold(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "hold", "holding", user)

    @commands.hybrid_command()
    async def hug(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "hug", "hugging", user)

    @commands.hybrid_command()
    async def kick(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "kick", "kicking", user)

    @commands.hybrid_command()
    async def kiss(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "kiss", "kissing", user)

    @commands.hybrid_command()
    async def kill(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "kill", "killing", user)

    @commands.hybrid_command()
    async def laugh(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "laugh", "laughing at", user)

    @commands.hybrid_command()
    async def lick(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "lick", "licking", user)

    @commands.hybrid_command()
    async def love(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "love", "in love with", user)

    @commands.hybrid_command()
    async def lurk(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "lurk", "lurking around", user)

    @commands.hybrid_command()
    async def nervous(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "nervous", "is nervous with", user)

    @commands.hybrid_command()
    async def nom(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "nom", "nomming", user)

    @commands.hybrid_command()
    async def nope(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "nope", "saying no to", user)

    @commands.hybrid_command()
    async def nuzzle(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "nuzzle", "idk wtf is that shit", user)

    @commands.hybrid_command()
    async def panic(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "panic", "is panicking at", user)

    @commands.hybrid_command()
    async def pat(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "pat", "patting", user)

    @commands.hybrid_command()
    async def peck(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "peck", "pecking", user)

    @commands.hybrid_command()
    async def poke(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "poke", "poking", user)

    @commands.hybrid_command()
    async def pout(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "pout", "pouting", user)

    @commands.hybrid_command()
    async def punch(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "punch", "punching", user)

    @commands.hybrid_command()
    async def run(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "run", "running towards", user)

    @commands.hybrid_command()
    async def sip(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "sip", "is sipping <:smirk:>", user)

    @commands.hybrid_command()
    async def slap(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "slap", "slapping", user)

    @commands.hybrid_command()
    async def sleepy(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "sleepy", "is sleepy", user)

    @commands.hybrid_command()
    async def smile(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "smile", "smiling at", user)

    @commands.hybrid_command()
    async def smug(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "smug", "smugging", user)

    @commands.hybrid_command()
    async def stab(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "stab", "stabbing", user)

    @commands.hybrid_command()
    async def stare(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "stare", "staring at", user)

    @commands.hybrid_command()
    async def suicide(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "suicide", "", user)

    @commands.hybrid_command()
    async def tease(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "tease", "teasing", user)

    @commands.hybrid_command()
    async def think(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "think", "thinking about", user)

    @commands.hybrid_command()
    async def thumbsup(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "thumbsup", "showing thumbsup to",  user)

    @commands.hybrid_command()
    async def tickle(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "tickle", "ticking", user)

    @commands.hybrid_command()
    async def triggered(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "triggered", "triggered at", user)

    @commands.hybrid_command()
    async def wag(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "wag", "wagging at", user)

    @commands.hybrid_command()
    async def wave(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "wave", "waving at", user)

    @commands.hybrid_command()
    async def wink(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "wink", "winking at", user)

    @commands.hybrid_command()
    async def yes(self, ctx, user: Optional[discord.User] = None):
        await self.base_message(ctx, "yes", "saying yes to", user)

    @commands.hybrid_command()
    async def smash(self, ctx):
        await ctx.send("https://media.tenor.com/73J4EYNNvMcAAAAM/f-u-middle-finger.gif")

