import nextcord
from nextcord import Interaction
from nextcord.ext import commands

class ping(commands.Cog):

    def __init__(self,bot:nextcord.Client):

        self.bot = bot

    @nextcord.slash_command(name='ping',description='نشون دادن پینگ')
    async def ping(self,interaction:Interaction):

        colors = {
            "green": nextcord.Color.green(),
            "yellow": nextcord.Color.yellow(),
            "red": nextcord.Color.red()
        }

        color = None

        ping = round(self.bot.latency*1000)

        if ping <= 100:

            color = colors["green"]
        
        elif ping > 101 and ping < 300:

            color = colors["yellow"]

        elif ping > 300:

            color = colors["red"]
            
        embed = nextcord.Embed(title=':ping_pong: پنگ',description=f':wireless: پینگ شما {ping} است',color=color)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    
    bot.add_cog(ping(bot))