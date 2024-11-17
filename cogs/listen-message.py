import nextcord
from nextcord.ext import commands

class listen_message(commands.Cog):

    def __init__(self,bot:nextcord.Client):

        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message:nextcord.Message):

        if message.author.bot:

            return
        
        elif 'سلام' in message.content or 'salam' in message.content:

            await message.channel.send('سلام اسم من اردکه و یه ربات هستم')

        elif 'جوک' in message.content or 'joke' in message.content:

            import random

            joke_file = open('./joke.txt','r',encoding='utf-8')

            joke_list = []

            for i in joke_file:

                joke_list.append(i)

            joke_file.close()

            joke = random.choice(joke_list)

            embed = nextcord.Embed(title=f'{joke}',color=nextcord.Color.orange())

            await message.channel.send(embed=embed)

async def setup(bot):
    
    bot.add_cog(listen_message(bot))