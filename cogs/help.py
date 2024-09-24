import discord
from discord.ext import commands
import asyncio


class HelpCog(commands.Cog, name="Help"):
    def __init__(self, bot):
        self.bot = bot

    # Custom help command with pagination
    @commands.command(help="Shows this help message with pagination if there are more than 25 commands.")
    async def help(self, ctx):
        # Collect all commands from all cogs
        all_commands = []
        for cog_name in self.bot.cogs:
            cog = self.bot.get_cog(cog_name)
            commands_list = cog.get_commands()
            if commands_list:
                all_commands.extend([(command.name, command.help, cog_name) for command in commands_list])

        # Sort and paginate commands (25 per page)
        per_page = 25
        pages = [all_commands[i:i + per_page] for i in range(0, len(all_commands), per_page)]
        total_pages = len(pages)

        if total_pages == 0:
            embed = discord.Embed(title="Error", description="No commands found.", color=discord.Color.red())
            return await ctx.send(embed=embed)

        current_page = 0

        # Function to create an embed for a specific page
        def create_embed(page):
            embed = discord.Embed(title="Help", description=f"Page {page + 1}/{total_pages}",
                                  color=discord.Color.blue())
            for command_name, command_help, cog_name in pages[page]:
                embed.add_field(name=f"`{command_name}` ({cog_name})", value=command_help or "No description",
                                inline=False)
            return embed

        # Send the initial help message
        message = await ctx.send(embed=create_embed(current_page))

        # Only add pagination if there are more than 1 page
        if total_pages > 1:
            # Add reaction emojis for navigation
            await message.add_reaction("⬅️")
            await message.add_reaction("➡️")

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in ["⬅️", "➡️"] and reaction.message.id == message.id

            while True:
                try:
                    reaction, user = await self.bot.wait_for("reaction_add", timeout=60.0, check=check)

                    if str(reaction.emoji) == "⬅️" and current_page > 0:
                        current_page -= 1
                        await message.edit(embed=create_embed(current_page))
                    elif str(reaction.emoji) == "➡️" and current_page < total_pages - 1:
                        current_page += 1
                        await message.edit(embed=create_embed(current_page))

                    # Remove the user's reaction after processing
                    await message.remove_reaction(reaction.emoji, user)

                except asyncio.TimeoutError:
                    # Timeout, remove reactions and stop listening for them
                    await message.clear_reactions()
                    break
