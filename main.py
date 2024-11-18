""" main.py

    This is the main file for the project. It will be used to run the discord bot project.
    
"""

# Importing the discord library
import discord
from discord.ext import commands

# Importing the os library
import os

# Importing the dotenv library
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create the bot with intents
intents = discord.Intents.default()
intents.message_content = True  # Enable the intents you need

bot = commands.Bot(command_prefix='!', intents=intents)

# Event when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'Failed to sync commands: {e}')

# Slash command
@bot.tree.command(name='hello', description='Say hello')
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message('Hello!')

# Run the bot
bot.run(TOKEN)
