import os
import discord
from discord.ext import commands
from flask import Flask
import threading
import asyncio

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🔄 Slash commands sincronizados: {len(synced)}")
    except Exception as e:
        print(e)

async def load_cogs():
    await bot.load_extension("cogs.like_commands")

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot online 24h"

def run_flask():
    app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run_flask).start()

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

asyncio.run(main())
