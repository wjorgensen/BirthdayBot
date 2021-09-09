import os

import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!Hello'):
        await message.channel.send('Hey')


client.run(os.getenv('DISCORD_TOKEN'))
