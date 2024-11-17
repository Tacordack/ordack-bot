import nextcord
from nextcord import Interaction
from nextcord.ext import commands

class info(commands.Cog):

    def __init__(self,bot:nextcord.Client):
        
        self.bot = bot
    
    # user info
    @nextcord.slash_command(name='user-info',description='نشون دادن اطلاعات ممبر')
    async def user_info(self,interaction:Interaction,user:nextcord.Member):

        embed = nextcord.Embed(title=user.name,color=nextcord.Color.blue())
        embed.set_thumbnail(url=user.avatar.url)
        embed.add_field(name=':bust_in_silhouette: Joined Discord:',value=user.created_at.date(),inline=False)
        embed.add_field(name=f':globe_with_meridians: Joined {interaction.guild.name}:',value=user.joined_at.date(),inline=False)
        embed.add_field(name=':id: User ID:',value=user.id,inline=False)

        await interaction.response.send_message(embed=embed)

    # server info
    @nextcord.slash_command(name='server-info',description='نشون دادن اطلاعات سرور')
    async def server_info(self,interaction:Interaction):
        
        channel_list = []
        member_list = []
        role_list = []

        server = interaction.guild

        channel_count = 0

        for channel in server.text_channels:

            channel_count = channel_count + 1

            channel_list.append(channel.mention)

        for member in server.members:

            member_list.append(member.mention)

        role_count = 0

        for role in server.roles:

            role_count = role_count + 1

            role_list.append(role.mention)

        server_owner = server.owner.mention
        
        embed = nextcord.Embed(title=interaction.guild.name,color=nextcord.Color.blue())
        embed.add_field(name=':id: Server ID:',value=server.id,inline=False)
        embed.add_field(name=':crown: Owner:',value=server_owner,inline=False)
        embed.add_field(name=f':busts_in_silhouette: Members {server.member_count}:',value=','.join((member_list)),inline=False)
        embed.add_field(name=f':speech_balloon: Channels {channel_count}:',value=','.join((channel_list)),inline=False)
        embed.add_field(name=f':identification_card: Roles {role_count}:',value=','.join((role_list)),inline=False)
        embed.set_thumbnail(url=server.icon)

        await interaction.response.send_message(embed=embed)

async def setup(bot):

    bot.add_cog(info(bot))