import nextcord
from nextcord import Interaction
from nextcord.ext import commands

import requests

base_url = "https://mineskin.eu"

class mc_skin(commands.Cog):

    def __init__(self,bot):

        self.bot = bot

    @nextcord.slash_command(name='mc-skin',description='نشون دادن اسکین ماینکرفت')
    async def mc_skin(self,interaction:Interaction,name:str):

        skin_url = f'{base_url}/armor/body/{name}'

        response = requests.get(skin_url)

        if response.status_code == 200:

            color = nextcord.Color.green()

            embed = nextcord.Embed(title=f'{name}\'s Minecraft Skin',color=color)
            embed.set_image(url=skin_url)

            await interaction.response.send_message(embed=embed)

async def setup(bot):

    bot.add_cog(mc_skin(bot))