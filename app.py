import os
import threading
from flask import Flask
import discord
from discord.ext import commands
from discord import app_commands

# =====================
# DISCORD BOT (SEM INTENTS PRIVILEGIADOS)
# =====================
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot Free Fire Like iniciado com sucesso!")

# =====================
# SLASH COMMAND
# =====================
@bot.tree.command(name="ping", description="Teste se o bot está online")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong! Bot online 24h")

# =====================
# FLASK KEEP ALIVE
# =====================
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot online 24h"

def run_flask():
    app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run_flask).start()

# =====================
# START BOT
# =====================
bot.run(TOKEN)
