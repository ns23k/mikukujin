import discord
from discord.ext import commands
import requests
from io import BytesIO


def get_image_format(link: str) -> str:
    stripped = link.split("?", 1)[0]
    return stripped.split(".")[-1]


def convert_to_buffer(link: str):
    file = requests.get(link).content
    return BytesIO(file)


def has_question_paper(message: discord.Message) -> bool:
    # todo: make this function better
    if not message.attachments:
        return False

    return True


class QuesPaper(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command()
    @commands.has_permissions(administrator=True)
    async def send_ques_paper(self, ctx: commands.Context, message_id: str, title: str):
        msg = None
        try:
            msg = await ctx.fetch_message(int(message_id))
        except Exception:
            await ctx.send("Message not found")

        if msg is not None:
            if not has_question_paper(msg):
                await ctx.send("No question Paper found")
        base_msg = await ctx.send("preparing to send question paper")
        ques_paper_guild = 1287283095019454567
        channel = self.bot.get_channel(ques_paper_guild)
        await channel.send(content=title,
                           files=[discord.File(convert_to_buffer(i.url),
                           filename=f"{msg.attachments.index(i)}.{get_image_format(i.url)}") for i in msg.attachments])
        await base_msg.edit(content="Question Paper Sent")
