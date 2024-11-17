import nextcord
from nextcord import Interaction
from nextcord.ext import commands

class say(commands.Cog):

    def __init__(self,bot):

        self.bot = bot
    
    @nextcord.slash_command(name='say',description='گفتن پیام شما')
    async def say(self,interaction:Interaction,message:str):
        
        await interaction.response.send_message(message)

async def setup(bot):

    bot.add_cog(say(bot))