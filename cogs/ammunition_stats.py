"""
cogs\ammunition_stats.py

This cog is for the ammunition stats command.
"""

import discord
from discord.ext import commands
import os
import json

# Default ammunition stats
DEFAULT_AMMUNITION_STATS = {
    "name": "8mm",
    "icon": "https://example.com/link-to-image.png",
    "faction": "Both",
    "type": "Magazine",
    "category": "Small Arms",
    "damage": {
        "min": 30,
        "max": 45,
        "subtype": "SB"
    },
    "weight": 10,
    "amount_per_crate": 40
}

class AmmunitionStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Load ammunition stats
    def load_ammunition_stats(self):
        if not os.path.exists("ammunition_stats.json"):
            return []
        with open("ammunition_stats.json", "r") as file:
            return json.load(file)

    # Save ammunition stats
    def save_ammunition_stats(self, ammunition_stats):
        with open("ammunition_stats.json", "w") as file:
            json.dump(ammunition_stats, file, indent=4)

    # Add new ammunition
    @commands.command(name="add_ammunition", help="Add new ammunition to the stats file")
    async def add_ammunition(self, ctx):
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        ammunition_stats = {}

        async def get_value(prompt):
            await ctx.send(prompt)
            response = await self.bot.wait_for("message", check=check)
            return response.content

        async def get_numeric_value(prompt, value_type=int):
            while True:
                await ctx.send(prompt)
                try:
                    response = await self.bot.wait_for("message", check=check)
                    return value_type(response.content)
                except ValueError:
                    await ctx.send(f"Invalid input. Please enter a valid {value_type.__name__}.")

        # Iterate through DEFAULT_AMMUNITION_STATS to collect data
        for key, value in DEFAULT_AMMUNITION_STATS.items():
            if isinstance(value, dict):  # Handle nested dictionaries
                ammunition_stats[key] = {}
                for sub_key, sub_value in value.items():
                    if isinstance(sub_value, (int, float)):  # Numeric nested fields
                        ammunition_stats[key][sub_key] = await get_numeric_value(f"What is the {sub_key} for {key}?")
                    else:  # String nested fields
                        ammunition_stats[key][sub_key] = await get_value(f"What is the {sub_key} for {key}?")
            elif isinstance(value, (int, float)):  # Numeric top-level fields
                ammunition_stats[key] = await get_numeric_value(f"What is the {key}?")
            else:  # String top-level fields
                ammunition_stats[key] = await get_value(f"What is the {key}?")

        # Load, update, and save ammunition stats
        current_stats = self.load_ammunition_stats()
        current_stats.append(ammunition_stats)
        self.save_ammunition_stats(current_stats)

        await ctx.send("Ammunition added successfully!")

# Cog setup
async def setup(bot):
    await bot.add_cog(AmmunitionStats(bot))
    print("AmmunitionStats cog loaded")
