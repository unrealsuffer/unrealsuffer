import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.slash_command(name="ping", description="Check bot status")
async def ping(ctx):
    await ctx.respond("🏓 Pong!")

bot.run("")
