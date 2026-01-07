import os
import json
import threading
from flask import Flask
import discord
from discord.ext import commands
from discord import app_commands

# =====================
# TOKEN
# =====================
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise RuntimeError("TOKEN não configurado no Render")

# =====================
# BANCO DE DADOS (JSON)
# =====================
DB_FILE = "likes.json"

def load_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump({}, f)
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# =====================
# DISCORD BOT
# =====================
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"✅ Bot conectado como {bot.user}")

# =====================
# SLASH COMMANDS
# =====================
@bot.tree.command(name="ping", description="Teste do bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!")

@bot.tree.command(name="like", description="Dar like em um ID Free Fire")
@app_commands.describe(player_id="ID do jogador Free Fire")
async def like(interaction: discord.Interaction, player_id: str):
    db = load_db()
    db[player_id] = db.get(player_id, 0) + 1
    save_db(db)

    await interaction.response.send_message(
        f"❤️ Like enviado!\n🎮 ID: `{player_id}`\n⭐ Total de likes: **{db[player_id]}**"
    )

@bot.tree.command(name="perfil", description="Ver likes de um ID Free Fire")
@app_commands.describe(player_id="ID do jogador Free Fire")
async def perfil(interaction: discord.Interaction, player_id: str):
    db = load_db()
    likes = db.get(player_id, 0)

    await interaction.response.send_message(
        f"👤 Perfil Free Fire\n🎮 ID: `{player_id}`\n❤️ Likes: **{likes}**"
    )

# =====================
# FLASK (KEEP ALIVE)
# =====================
app = Flask(__name__)

@app.route("/")
def home():
    return "🤖 Bot Free Fire Like ONLINE 24h!"

def run_flask():
    app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run_flask, daemon=True).start()

# =====================
# START
# =====================
bot.run(TOKEN)
