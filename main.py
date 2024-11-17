import json
import os
import asyncio

import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='!',intents=intents)

file = open('config.json')
json_file = json.load(file)
BOTTOKEN = json_file['bot-token']
file.close()

@bot.event
async def on_ready():

    await bot.change_presence(activity=nextcord.Game('🦆'),status=nextcord.Status.online)

    print(f'{bot.user.name} is READY')
    print('---------------')

async def main():

    initial_extension = []

    for filename in os.listdir('cogs/'):

        if filename.endswith('.py'):

            initial_extension.append('cogs.'+filename[:-3])
            
    print(initial_extension)
    print('---------------')

    for cogsfile in initial_extension:

        bot.load_extension(cogsfile)
        
    await bot.start(BOTTOKEN)

asyncio.run(main())