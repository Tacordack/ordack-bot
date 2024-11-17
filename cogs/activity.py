import nextcord
from nextcord import Interaction
from nextcord import Member
from nextcord.ext import commands

class activity(commands.Cog):

    def __init__(self,bot):

        self.bot = bot

    @nextcord.slash_command(name='activity',description='نشون دادن وضعیت')
    async def activity(self,interaction:Interaction,user:Member):

        activity_color = nextcord.Colour

        activity = user.status

        if activity == 'online':

            activity_color = activity_color.green()
        
        if activity == 'offline':

            activity_color = activity_color.light_gray()
        
        if activity == 'idle':
            
            activity_color = activity_color.yellow()

        if activity == 'dnd':

            activity = 'do not disturb'

            activity_color = activity_color.brand_red()

        embed = nextcord.Embed(title='Activity',description=activity.title(),color=activity_color)
        embed.set_author(name=user,icon_url=user.avatar.url)

        await interaction.response.send_message(embed=embed)

async def setup(bot):

    bot.add_cog(activity(bot))