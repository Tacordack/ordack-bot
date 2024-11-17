import nextcord
from nextcord import Interaction
from nextcord import TextChannel
from nextcord.ext import application_checks
from nextcord.ext import commands

class delete_message(commands.Cog):

    def __init__(self,bot:nextcord.Client):

        self.bot = bot

    @nextcord.slash_command(name='delete-message',description='حذف کردن پیام ها')
    @application_checks.has_permissions(manage_messages=True)
    async def delete_message(self,interaction:Interaction,channel:TextChannel,amount:int):
        
        await channel.purge(limit=amount+1)

        embed = nextcord.Embed(title=f':white_check_mark: {amount} messages deleted :white_check_mark:',color=nextcord.Color.brand_green())

        await interaction.response.send_message(embed=embed,ephemeral=True)
    
async def setup(bot):
    
    bot.add_cog(delete_message(bot))