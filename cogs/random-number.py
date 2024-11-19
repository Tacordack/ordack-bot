import nextcord
from nextcord import Interaction
from nextcord.ext import commands

class random_number(commands.Cog):

    def __init__(self,bot):

        self.bot = bot
    
    @nextcord.slash_command(name='random-number',description='فرستادن عدد شانسی')
    async def random_number(self,interaction:Interaction,start:int,stop:int):

        import random

        random_number = random.randrange(start,stop)

        await interaction.response.send_message(random_number)

async def setup(bot):

    bot.add_cog(random_number(bot))