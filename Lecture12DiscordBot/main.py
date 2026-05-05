

import discord
from dotenv import load_dotenv
import os
from google import genai



load_dotenv()

googleKEY=os.getenv("GoogleAPI_KEY")
discordToken=os.getenv("DISCORD_TOKEN")






intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author==client.user:
        return
    if client.user in message.mentions:
        
        clientGoogle = genai.Client(api_key=googleKEY)
        response = clientGoogle.models.generate_content(
            model="gemini-3-flash-preview", contents=message.content
        )
        # print(response.text)
        await message.channel.send(response.text)

client.run(discordToken)
