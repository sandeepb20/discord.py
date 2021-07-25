import os
import random

import discord
from dotenv import load_dotenv

from discord.ext import commands
client = commands.Bot(command_prefix='!')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

def random_line(file_name):
    lines = open(file_name).read().splitlines()
    return random.choice(lines)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    """
    UltraPureWords = [
        'I\'m the human form of the 💯 emoji.',
        'Bsdk',
        'bc',
        'mc',
        'You suck men',
        
    ]
    """
    if client.user.id != message.author.id:
        if message.content.startswith('!'):
            author = message.author
            response = random_line('wishes.txt')
            await message.channel.send(response)
            await test(author, message)
        
        if 'Hello' in message.content:
            await client.send_message(message.channel, 'Hey')
async def test(author, message):

    await message.channel.send(F'Hi {author}, I heard you.')

client.run(TOKEN)
