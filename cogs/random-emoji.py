import random

import nextcord
from nextcord import Interaction
from nextcord.ext import commands

class random_emoji(commands.Cog):

    def __init__(self,bot):

        self.bot = bot

    @nextcord.slash_command(name='random-emoji',description='فرستادن ایموجی به صورت شانسی')
    async def random_emoji(self,interaction:Interaction):

        emoji_list = []

        for emoji in interaction.guild.emojis:

            emoji_list.append(emoji)

        await interaction.response.send_message(random.choice(emoji_list))

async def setup(bot):
    
    bot.add_cog(random_emoji(bot))