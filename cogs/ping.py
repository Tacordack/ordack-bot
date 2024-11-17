import nextcord
from nextcord import Interaction
from nextcord.ext import commands

class ping(commands.Cog):

    def __init__(self,bot:nextcord.Client):

        self.bot = bot

    @nextcord.slash_command(name='ping',description='Pong')
    async def ping(self,interaction:Interaction):

        ping = round(self.bot.latency*1000)

        embed = nextcord.Embed(title=':ping_pong: Pong!',description=f':wireless: {ping} ms',color=nextcord.Color.blue())

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    
    bot.add_cog(ping(bot))