"""
cogs\weapon_stats.py

This cog is for the weapon stats command.
"""

import discord
from discord.ext import commands
import os
import json

# Default weapon stats
DEFAULT_WEAPON_STATS = {
    "name": "Argenti r.II Rifle",
    "icon": "https://example.com/link-to-image.png",
    "faction": "Colonial",
    "type": "Rifle",
    "category": "Small Arms",
    "equipment_slot": "Primary (#1)",
    "ammunition": "7.62mm",
    "damage": {
        "min": 45,
        "max": 67,
        "subtype": "SB"
    },
    "fire_rate": "81 rounds/min",
    "firing_mode": "Semi-automatic",
    "range": {
        "effective": "25 meters",
        "max": "40 meters"
    },
    "magazine_size": 12,
    "reload_time": "3.5 seconds",
    "weight": {
        "base": 70,
        "with_uniform_bonus": 52
    },
    "amount_per_crate": "Unknown"
}

class WeaponStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Load weapon stats
    def load_weapon_stats(self):
        if not os.path.exists("weapon_stats.json"):
            return []
        with open("weapon_stats.json", "r") as file:
            return json.load(file)

    # Save weapon stats
    def save_weapon_stats(self, weapon_stats):
        with open("weapon_stats.json", "w") as file:
            json.dump(weapon_stats, file, indent=4)

    # Add a new weapon
    @commands.command(name="add_weapon", help="Add a new weapon to the weapon stats file")
    async def add_weapon(self, ctx):
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        weapon_stats = {}

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

        # Iterate through DEFAULT_WEAPON_STATS to collect data
        for key, value in DEFAULT_WEAPON_STATS.items():
            if isinstance(value, dict):  # Handle nested dictionaries
                weapon_stats[key] = {}
                for sub_key, sub_value in value.items():
                    if isinstance(sub_value, (int, float)):  # Numeric nested fields
                        weapon_stats[key][sub_key] = await get_numeric_value(f"What is the {sub_key} for {key}?")
                    else:  # String nested fields
                        weapon_stats[key][sub_key] = await get_value(f"What is the {sub_key} for {key}?")
            elif isinstance(value, (int, float)):  # Numeric top-level fields
                weapon_stats[key] = await get_numeric_value(f"What is the {key}?")
            else:  # String top-level fields
                weapon_stats[key] = await get_value(f"What is the {key}?")

        # Load, update, and save weapon stats
        current_stats = self.load_weapon_stats()
        current_stats.append(weapon_stats)
        self.save_weapon_stats(current_stats)

        await ctx.send("Weapon added successfully!")

# Cog setup
async def setup(bot):
    await bot.add_cog(WeaponStats(bot))
    print("WeaponStats cog loaded")
