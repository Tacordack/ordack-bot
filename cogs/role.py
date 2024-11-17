import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from nextcord.ext import application_checks
from nextcord.ext.commands import MissingPermissions

class role(commands.Cog):

    def __init__(self,bot:nextcord.Client):
        
        self.bot = bot

    # create role
    @nextcord.slash_command(name='role-create',description='ساخت رول')
    @application_checks.has_permissions(manage_roles=True)
    async def create_role(self,interaction:Interaction,name:str):

        await interaction.guild.create_role(name=name)

        await interaction.response.send_message('role created')

    # delete role
    @nextcord.slash_command(name='role-delete',description='حذف رول')
    @application_checks.has_permissions(manage_roles=True)
    async def delete_role(self,interaction:Interaction,role:nextcord.Role):

        await role.delete()

        await interaction.response.send_message('role deleted')

    # add role
    @nextcord.slash_command(name='role-add',description='اضافه کردن رول')
    @application_checks.has_permissions(manage_roles=True)
    async def add_role(self,interaction:Interaction,user:nextcord.Member,role:nextcord.Role):

        if role in user.roles:

            embed = nextcord.Embed(title='',description=f':warning: {user.mention} already has the {role.mention} :warning:',color=nextcord.Color.yellow())

            await interaction.response.send_message(embed=embed)
        
        else:
            embed = nextcord.Embed(title='',description=f':white_check_mark: added {role.mention} to {user.mention} :white_check_mark:',color=nextcord.Color.brand_green())

            await user.add_roles(role)

            await interaction.response.send_message(embed=embed)
        
    @add_role.error
    async def add_role_error(self,error,interaction:Interaction):

        if isinstance(error,MissingPermissions):

            embed = nextcord.Embed(title='',description=':warning: you dont have permission to use this command :warning:',color=nextcord.Color.yellow())

            await interaction.response.send_message(embed=embed)
            
    # remove role
    @nextcord.slash_command(name='role-remove',description='برداشتن رول')
    @application_checks.has_permissions(manage_roles=True)
    async def remove_role(self,interaction:Interaction,user:nextcord.Member,role:nextcord.Role):

        if role in user.roles:

            embed = nextcord.Embed(title='',description=f':cross_mark: removed {role.mention} from {user.mention} :cross_mark:',color=nextcord.Color.brand_green())

            await user.remove_roles(role)

            await interaction.response.send_message(embed=embed)

        else:

            embed = nextcord.Embed(title='',description=f':warning: {user.mention} does not have the {role.mention} :warning:',color=nextcord.Color.yellow())

            await interaction.response.send_message(embed=embed)
    
    @remove_role.error
    async def remove_role_error(self,error,interaction:Interaction):

        if isinstance(error,MissingPermissions):

            embed = nextcord.Embed(title='',description=':warning: you dont have permission to use this command :warning:',color=nextcord.Color.yellow())

            await interaction.response.send_message(embed=embed)

async def setup(bot):

    bot.add_cog(role(bot))