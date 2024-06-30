import discord
from discord.ext import commands
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import json
import asyncio
import uvicorn
import os
from Config.Funciones.registrar import registrar_rutas_desde_directorio
from Config.Funciones.datos_json import load_data
from Config.Funciones.guardar_json import save_data
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.reactions = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
app = FastAPI()



@bot.event
async def on_raw_reaction_add(payload):
    data = load_data()
    guild = bot.get_guild(payload.guild_id)
    for role_entry in data.get("reacion", []):
        if (role_entry["channel_id"] == str(payload.channel_id) and
                role_entry["message_id"] == str(payload.message_id) and
                role_entry["emoji"] == str(payload.emoji)):
            role = guild.get_role(int(role_entry["role_id"]))
            if role:
                member = guild.get_member(payload.user_id)
                await member.add_roles(role)
                print(f"Added {role.name} to {member.name}")

@bot.event
async def on_raw_reaction_remove(payload):
    data = load_data()
    guild = bot.get_guild(payload.guild_id)
    for role_entry in data.get("reacion", []):
        if (role_entry["channel_id"] == str(payload.channel_id) and
                role_entry["message_id"] == str(payload.message_id) and
                role_entry["emoji"] == str(payload.emoji)):
            role = guild.get_role(int(role_entry["role_id"]))
            if role:
                member = guild.get_member(payload.user_id)
                await member.remove_roles(role)
                print(f"Removed {role.name} from {member.name}")



@app.get("/roles")
def read_roles():
    return load_data()







carpeta_api = os.path.join(os.path.dirname(__file__), 'Config')
router_principal = APIRouter()
registrar_rutas_desde_directorio(router_principal, carpeta_api)
app.include_router(router_principal)


def run_api():
    uvicorn.run(app, host="0.0.0.0", port=8000)



discord_token = os.getenv("DISCORD_TOKEN")
# h

async def main():
    await asyncio.gather(
        asyncio.to_thread(run_api),
        bot.start(discord_token)
    )

asyncio.run(main())

