import random

import nextcord
from nextcord import Interaction
from nextcord.ext import commands

class joke(commands.Cog):
    
    def __init__(self,bot:nextcord.Client):

        self.bot = bot
    
    # joke
    @nextcord.slash_command(name='joke',description='فرستادن جوک')
    async def joke(self,interaction:Interaction):

        joke_file = open('./joke.txt','r',encoding='utf-8')

        joke_list = []

        for i in joke_file:

            joke_list.append(i)

        joke_file.close()

        joke = random.choice(joke_list)

        embed = nextcord.Embed(title=f'{joke}',color=nextcord.Color.orange())

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    
    bot.add_cog(joke(bot))