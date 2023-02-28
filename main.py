import os
import discord

from dotenv import load_dotenv
load_dotenv(dotenv_path="config")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print("The bot is ready.")

@client.event
async def on_message(message):
    print("message read")
    if message.content.lower() == "ping":
        await message.channel.send("pong")
    elif "pas bu" in message.content.lower():
        await message.channel.send("WHAT ARE YOU WAITING FOR? HYDRATION NOW 🚰")

client.run(os.getenv("TOKEN"))