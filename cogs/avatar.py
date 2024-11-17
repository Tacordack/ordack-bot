import nextcord
from nextcord import Interaction, Member
from nextcord.ext import commands

class avatar(commands.Cog):

    def __init__(self,bot):

        self.bot = bot

    @nextcord.slash_command(name='avatar',description='نشون دادن آواتار')
    async def user_avatar(self,interaction:Interaction,user:Member):

        embed = nextcord.Embed(title=user.name,color=nextcord.Color.blue())
        embed.set_image(url=user.avatar.url)

        await interaction.response.send_message(embed=embed)

async def setup(bot):

    bot.add_cog(avatar(bot))