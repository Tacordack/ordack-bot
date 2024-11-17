import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from nextcord.ext import application_checks
from nextcord.ext.commands import has_permissions, MissingPermissions

class ban(commands.Cog):

    def __init__(self,bot:nextcord.Client):
        self.bot = bot

    # ban
    @nextcord.slash_command(name='ban',description='بن کردن')
    @application_checks.has_permissions(ban_members=True)
    async def ban(self,interaction:Interaction,user:nextcord.Member,reason=False):
        embed = nextcord.Embed(title='',description=f':hammer: {user} has been banned :hammer:',color=nextcord.Color.brand_green())
        await user.ban(reason=reason)
        await interaction.response.send_message(embed=embed)
    
    @ban.error
    async def ban_error(self,error,interaction:Interaction):
        if isinstance(error,MissingPermissions):
            embed = nextcord.Embed(title=':warning: you dont have permission to use this command :warning:',color=nextcord.Color.yellow())
            await interaction.response.send_message(embed=embed)

    # unban
    @nextcord.slash_command(name='unban',description='آن بن کردن')
    @application_checks.has_permissions(ban_members=True)
    async def unban(self,interaction:Interaction,user:nextcord.Member,reason):
        embed = nextcord.Embed(title='',description=f'{user.mention} has been unbanned',color=nextcord.Color.green())
        await interaction.guild.unban(user,reason=reason)
        await interaction.response.send_message(embed=embed)

    @unban.error
    async def unban_error(self,error,interaction:Interaction):
        if isinstance(error,MissingPermissions):
            embed = nextcord.Embed(title=':warning: you dont have permission to use this command :warning:',color=nextcord.Color.yellow())
            await interaction.response.send_message(embed=embed) 

async def setup(bot):
    
    bot.add_cog(ban(bot))