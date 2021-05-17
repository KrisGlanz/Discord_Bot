#bot.py

import discord
import random
import os
import weather_bot
import astro_photo
import news_bot

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #calls for weather of location of your picking 
    if message.content.startswith('qt*'):
        location = ''.join(message.content[3:])
        response = weather_bot.weather(location)
        await message.channel.send(response)

    #calls for the apod    
    elif message.content.startswith('apod*'):
        photo = astro_photo.astro()
        await message.channel.send(photo)
        
    #calls news bot
    elif message.content.startswith('news*'):
        search = ''.join(message.content[5:])
        result = news_bot.news(search)
        await message.channel.send(f"Here is the latest article for {search}")
        await message.channel.send(result)
        
        
client.run(TOKEN)
