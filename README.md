# Discord Bot Setup Instructions

## Prerequisites

Before setting up the bot, ensure you have the following:
- **Python**: Version 3.8 or higher.
- **Discord Account**: With access to the [Discord Developer Portal](https://discord.com/developers/applications).
- **Bot Token**: Generated from the Developer Portal.
- **Required Libraries**: `discord.py`, `python-dotenv`.

---

## Project Structure

Organize your project folder as follows:

```plaintext
discord_bot/
├── main.py                 # Main bot file
├── cogs/                   # Folder for bot cogs
│   ├── __init__.py         # Makes the folder a Python package (can be empty)
│   ├── weapon_stats.py     # Cog for weapon stats
│   ├── ammunition_stats.py # Cog for ammunition stats
├── .env                    # Environment file for your bot token
├── weapon_stats.json       # File for storing weapon stats
├── ammunition_stats.json   # File for storing ammunition stats
├── requirements.txt        # List of dependencies

Setup Instructions
Step 1: Install Required Libraries
Run the following command to install required libraries:

pip install discord.py python-dotenv

Save the dependencies to a requirements.txt file:

Step 2: Set Up Your Bot on Discord
Go to the Discord Developer Portal.
Click New Application and give your bot a name.
Navigate to the Bot tab:
Click Add Bot.
Copy the TOKEN under the bot settings.
Under OAuth2 > URL Generator:
Select the bot and applications.commands scopes.
Under Bot Permissions, choose appropriate permissions (e.g., Administrator).
Copy the generated URL and invite the bot to your server.

Step 3: Configure the .env File
Create a .env file in the project root directory and add your bot token:

DISCORD_TOKEN=your-bot-token-here

Replace your-bot-token-here with the token you copied from the Developer Portal.

Step 4: Create and Configure main.py
Ensure main.py is set up to load cogs and run the bot. Here’s an example:

# main.py
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Create the bot with intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Load cogs asynchronously
async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded cog: {filename}")
            except Exception as e:
                print(f"Failed to load cog {filename}: {e}")

async def main():
    await load_cogs()
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())


Step 5: Create Cogs
Place your cogs (e.g., weapon_stats.py, ammunition_stats.py) in the cogs folder. Example structure for weapon_stats.py:

# cogs/weapon_stats.py
import discord
from discord.ext import commands
import json
import os

class WeaponStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Add your weapon stats commands here...

async def setup(bot):
    await bot.add_cog(WeaponStats(bot))
    print("WeaponStats cog loaded")


Here's the entire content in Markdown format, ready to copy and paste into a README.md file:

markdown
Copy code
# Discord Bot Setup Instructions

## Prerequisites

Before setting up the bot, ensure you have the following:
- **Python**: Version 3.8 or higher.
- **Discord Account**: With access to the [Discord Developer Portal](https://discord.com/developers/applications).
- **Bot Token**: Generated from the Developer Portal.
- **Required Libraries**: `discord.py`, `python-dotenv`.

---

## Project Structure

Organize your project folder as follows:

```plaintext
discord_bot/
├── main.py                 # Main bot file
├── cogs/                   # Folder for bot cogs
│   ├── __init__.py         # Makes the folder a Python package (can be empty)
│   ├── weapon_stats.py     # Cog for weapon stats
│   ├── ammunition_stats.py # Cog for ammunition stats
├── .env                    # Environment file for your bot token
├── weapon_stats.json       # File for storing weapon stats
├── ammunition_stats.json   # File for storing ammunition stats
├── requirements.txt        # List of dependencies
Setup Instructions
Step 1: Install Required Libraries
Run the following command to install required libraries:

bash
Copy code
pip install discord.py python-dotenv
Save the dependencies to a requirements.txt file:

plaintext
Copy code
discord.py
python-dotenv
Step 2: Set Up Your Bot on Discord
Go to the Discord Developer Portal.
Click New Application and give your bot a name.
Navigate to the Bot tab:
Click Add Bot.
Copy the TOKEN under the bot settings.
Under OAuth2 > URL Generator:
Select the bot and applications.commands scopes.
Under Bot Permissions, choose appropriate permissions (e.g., Administrator).
Copy the generated URL and invite the bot to your server.
Step 3: Configure the .env File
Create a .env file in the project root directory and add your bot token:

plaintext
Copy code
DISCORD_TOKEN=your-bot-token-here
Replace your-bot-token-here with the token you copied from the Developer Portal.

Step 4: Create and Configure main.py
Ensure main.py is set up to load cogs and run the bot. Here’s an example:

python
Copy code
# main.py
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Create the bot with intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Load cogs asynchronously
async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded cog: {filename}")
            except Exception as e:
                print(f"Failed to load cog {filename}: {e}")

async def main():
    await load_cogs()
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
Step 5: Create Cogs
Place your cogs (e.g., weapon_stats.py, ammunition_stats.py) in the cogs folder. Example structure for weapon_stats.py:

python
Copy code
# cogs/weapon_stats.py
import discord
from discord.ext import commands
import json
import os

class WeaponStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Add your weapon stats commands here...

async def setup(bot):
    await bot.add_cog(WeaponStats(bot))
    print("WeaponStats cog loaded")
Step 6: Run Your Bot
Open a terminal in the project folder.
Run the bot using:
bash
Copy code
python main.py
If everything is configured correctly, you should see output like:
plaintext
Copy code
Logged in as YourBotName#1234
Synced 1 command(s)
Loaded cog: weapon_stats.py

Optional: Deployment
To keep your bot running continuously, you can deploy it using a hosting service:

Replit
Heroku
AWS
Let me know if you'd like more information on deployment!

Contributing
Feel free to open issues or submit pull requests to improve the bot!

License
This project is licensed under the MIT License. See the LICENSE file for details.


This Markdown file is formatted specifically for GitHub with syntax highlighting, clear sections, and professional structure. You can copy and paste this directly into a `README.md` file in your repository. Let me know if you need further changes!

