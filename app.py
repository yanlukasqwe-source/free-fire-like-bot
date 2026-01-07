import os
import threading
from flask import Flask
import discord
from discord.ext import commands

# =====================
# DISCORD BOT
# =====================
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print("Bot Free Fire Like iniciado com sucesso!")

# EXEMPLO DE COMANDO (teste)
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

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
