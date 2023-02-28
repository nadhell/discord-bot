import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv(dotenv_path="config")

class PandoreBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all(), case_insensitive=True, self_bot=True)

    async def on_ready(self):
        print(f"{self.user.display_name} is connected.")

bot = PandoreBot()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif message.content == 'hello':
        await message.channel.send(f'Hi {message.author}')
    elif message.content == 'bye':
        await message.channel.send(f'Goodbye {message.author}')

    await bot.process_commands(message)

@bot.command()
async def delete(ctx, number_of_messages: int):
    async for message in ctx.history(limit=number_of_messages+1):
        await message.delete()

bot.run(os.getenv("TOKEN"))