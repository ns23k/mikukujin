import discord
from discord.ext import commands
import requests
from io import BytesIO
from PIL import Image


def get_image_format(link: str) -> str:
    stripped = link.split("?", 1)[0]
    return stripped.split(".")[-1]


def convert_to_buffer(url: str):
    file = requests.get(url).content
    return BytesIO(file)


def has_question_paper(message: discord.Message) -> bool:
    # todo: make this function better
    if not message.attachments:
        return False

    return True


def is_landscape(img: BytesIO) -> bool:
    img = Image.open(img)
    return img.width > img.height


def image_to_bytesio(image: Image.Image, _format: str = 'PNG'):
    image_bytes = BytesIO()
    image.save(image_bytes, format=_format)
    image_bytes.seek(0)
    return image_bytes


def rotate_img(file):
    img = Image.open(file)
    img = img.rotate(90, expand=1)
    return image_to_bytesio(img)


def prepare_attachments(attachments):
    message_attachments = []
    for i in attachments:
        file = convert_to_buffer(i.url)
        if is_landscape(file) and ".pdf" not in i.url:
            file = rotate_img(file)
            message_attachments.append(discord.File(file, filename=f"{attachments.index(i)}.png"))
        else:
            message_attachments.append(discord.File(file, filename=f"{attachments.index(i)}.png"))

    return message_attachments


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
        await channel.send(content=title, files=prepare_attachments(msg.attachments))
        await base_msg.edit(content="Question Paper Sent")
