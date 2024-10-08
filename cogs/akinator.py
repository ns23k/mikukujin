import discord
from discord.ext import commands, tasks
import akipy as ak
import random
import traceback
import asyncio


class Aki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["aki"])
    async def akinator(self, ctx):
        intro = discord.Embed(title="Akinator",
                              description="Hello, " + ctx.author.mention +
                                          "I am Akinator!!!",
                              color=discord.Colour.blue())
        intro.set_thumbnail(
            url=
            "https://en.akinator.com/assets/img/akinator.png"
        )
        intro.set_footer(
            text=
            "Think about a real or fictional character. I will try to guess who it is"
        )
        bye = discord.Embed(title="Akinator",
                            description="Bye, " + ctx.author.mention,
                            color=discord.Colour.blue())
        bye.set_footer(text="Akinator left the chat!!")
        bye.set_thumbnail(
            url=
            "https://i.pinimg.com/originals/28/fc/0b/28fc0b88d8ded3bb8f89cb23b3e9aa7b.png"
        )
        await ctx.send(embed=intro)

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
            ) in ["y", "n", "p", "b", "yes", "no", "probably", "idk", "back"]

        try:
            aki = ak.Akinator()
            q = aki.start_game()
            while not aki.win:
                    question = discord.Embed(title="Question",
                                             description=aki.question,
                                             color=discord.Colour.blue())
                    ques = [
                        "https://i.imgflip.com/uojn8.jpg",
                        "https://ih1.redbubble.net/image.297680471.0027/flat,750x1000,075,f.u1.jpg"
                    ]
                    question.set_thumbnail(url=ques[random.randint(0, 1)])
                    question.set_footer(text="Your answer:(y/n/p/idk/b)")
                    question_sent = await ctx.send(embed=question)
                    try:
                        msg = await self.bot.wait_for("message",
                                                      check=check,
                                                      timeout=30)
                    except asyncio.TimeoutError:
                        await question_sent.delete()
                        await ctx.send(
                            "Sorry you took too long to respond!(waited for 30sec)"
                        )
                        await ctx.send(embed=bye)
                        return

                    if msg.content.lower() in ["b", "back"]:
                        try:
                            q = aki.back()
                        except ak.CantGoBackAnyFurther:
                            await ctx.send(e)
                            continue
                    else:
                        try:
                            q = aki.answer(msg.content.lower())
                        except Exception as e:
                            await ctx.send(e)
                            continue

            print(aki.name_proposition)
            print(aki.description_proposition)
            print(aki.pseudo)
            print(aki.photo)
            answer = discord.Embed(title=str(aki.name_proposition),
                                   description=str(aki.description_proposition),
                                   color=discord.Colour.blue())
            answer.set_image(url=str(aki.photo))
            answer.set_footer(text="Was I correct?(y/n)")
            await ctx.send(embed=answer)
            try:
                correct = await self.bot.wait_for("message",
                                                  check=check,
                                                  timeout=30)
            except asyncio.TimeoutError:
                await ctx.send(
                    "Sorry you took too long to respond!(waited for 30sec)")
                await ctx.send(embed=bye)
                return
            if correct.content.lower() == "y":
                yes = discord.Embed(title="Yeah!!!",
                                    color=discord.Colour.blue())
                yes.set_thumbnail(
                    url=
                    "https://i.pinimg.com/originals/ae/aa/d7/aeaad720bd3c42b095c9a6788ac2df9a.png"
                )
                await ctx.send(embed=yes)
            else:
                no = discord.Embed(title="Oh Noooooo!!!",
                                   color=discord.Colour.blue())
                no.set_thumbnail(
                    url=
                    "https://i.pinimg.com/originals/0a/8c/12/0a8c1218eeaadf5cfe90140e32558e64.png"
                )
                await ctx.send(embed=no)
            await ctx.send(embed=bye)

        except Exception as e:
            print(traceback.format_exc())
