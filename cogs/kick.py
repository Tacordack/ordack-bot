import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from nextcord.ext import application_checks
from nextcord.ext.commands import has_permissions, MissingPermissions

class kick(commands.Cog):
    
    def __init__(self,bot:nextcord.Client):

        self.bot = bot

    @nextcord.slash_command(name='kick',description='بیرون کردن')
    @application_checks.has_permissions(kick_members=True)
    async def kick(self,interaction:Interaction,user:nextcord.Member,reason=False):

        embed = nextcord.Embed(title='',description=f':outbox_tray: {user.mention} has been kicked :outbox_tray:',color=nextcord.Color.brand_green())

        await user.kick(reason=reason)

        await interaction.response.send_message(embed=embed)
    
    @kick.error
    async def kick_error(self,error,interaction:Interaction):

        if isinstance(error,commands.MissingPermissions):

            embed = nextcord.Embed(title=':warning: you dont have permission to use this command :warning:',color=nextcord.Color.yellow())

            await interaction.response.send_message(embed=embed)

async def setup(bot):
    
    bot.add_cog(kick(bot))