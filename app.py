import discord
from discord.ext import commands
from discord import app_commands
import os

TOKEN = os.getenv("DISCORD_TOKEN") or "COLOQUE_SEU_TOKEN_AQUI"

intents = discord.Intents.default()

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents
        )

    async def setup_hook(self):
        await self.tree.sync()
        print("✅ Slash commands sincronizados")

bot = MyBot()

@bot.event
async def on_ready():
    print(f"🤖 Bot ligado como {bot.user}")

@bot.tree.command(name="perfil", description="Mostra seu perfil")
async def perfil(interaction: discord.Interaction):
    await interaction.response.send_message(
        "👤 **Seu perfil**\n❤️ Likes: 0",
        ephemeral=False
    )

bot.run(TOKEN)
