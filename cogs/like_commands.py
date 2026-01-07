import discord
from discord.ext import commands
from discord import app_commands
import aiohttp
from datetime import datetime
import asyncio

class LikeCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
        self.api_url = "https://ff-like-api-dun.vercel.app/like"

    @app_commands.command(name="like", description="Enviar likes no Free Fire")
    @app_commands.describe(uid="UID do jogador")
    async def like(self, interaction: discord.Interaction, uid: str):
        await interaction.response.defer(thinking=True)

        if not uid.isdigit():
            await interaction.followup.send("❌ UID inválido.")
            return

        try:
            async with self.session.get(f"{self.api_url}?uid={uid}") as resp:
                if resp.status != 200:
                    await interaction.followup.send("⚠️ Erro na API.")
                    return
                data = await resp.json()

            embed = discord.Embed(
                title="🔥 FREE FIRE LIKE",
                color=0x2ecc71,
                timestamp=datetime.now()
            )
            embed.add_field(name="UID", value=uid)
            embed.add_field(name="Likes antes", value=data.get("likes_before"))
            embed.add_field(name="Likes depois", value=data.get("likes_after"))
            embed.set_footer(text="Bot Free Fire Like")

            await interaction.followup.send(embed=embed)

        except Exception as e:
            await interaction.followup.send("❌ Erro inesperado.")

    async def cog_unload(self):
        await self.session.close()

async def setup(bot):
    await bot.add_cog(LikeCommands(bot))
