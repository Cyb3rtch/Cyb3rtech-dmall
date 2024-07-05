        #Made By Cyb3rtech
     #Discord : @antidatabreach
#############################################

import discord
from discord.ext import commands
import requests
import asyncio
import os
from colorama import init, Fore, Style

init(autoreset=True)

#############################################

token = ''
prefix = '+'

#############################################

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=prefix, intents=intents, help_command=None)
bot.remove_command('help')

#############################################

def print_dark_red(text):
    print(f"\033[31m{text}\033[0m")

def print_dark_blue(text):
    print(f"\033[34m{text}\033[0m")
    
#############################################

@bot.command(name="help")
async def help_command(ctx):
    embed = discord.Embed(title="🔍 Dmall' help", description="Voici les commandes disponibles :", color=0x57F287)
    embed.add_field(name=f"{prefix}dmall", value="Envoyez un message à tous les membres", inline=False)
    embed.add_field(name=f"{prefix}stats", value="Affiche les statistiques du serveur", inline=False)
    embed.add_field(name=f"{prefix}ping", value="Affiche la latence du bot", inline=False)
    embed.add_field(name=f"{prefix}invite", value="Obtenez le lien d'invitation du bot", inline=False)
    embed.set_footer(text="Made By Cyb3rtech")
    embed.set_thumbnail(url=ctx.author.avatar.url)

    await ctx.send(embed=embed)
    
#############################################

@bot.command(name="dmall")
async def dmall(ctx):
    await ctx.send("**Entrer le message à envoyer (utilisez {user} pour mentionner le membre) :**")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        message = await bot.wait_for('message', check=check, timeout=60.0)
        message_content = message.content
        await ctx.send(f"Envoi du message à tous les membres : {message_content}")

        for member in ctx.guild.members:
            if member.bot:
                continue

            personalized_message = message_content.replace("{user}", member.mention)

            try:
                await member.send(personalized_message)
                print(Fore.GREEN + f"Message envoyé à {member.display_name}")
            except Exception as e:
                print(Fore.RED + f"Impossible d'envoyer un message à {member.display_name}. Erreur : {e}")

        await ctx.send("**Message envoyé à tous les membres.**")
    except asyncio.TimeoutError:
        await ctx.send("Trop long.")

#############################################

@bot.command(name="stats")
async def stats(ctx):
    if not ctx.guild:
        await ctx.send("Cette commande ne peut être utilisée que dans un serveur.")
        return
        
    total_members = ctx.guild.member_count
    online_members = sum(member.status != discord.Status.offline for member in ctx.guild.members)
    voice_channels = sum(1 for channel in ctx.guild.voice_channels if len(channel.members) > 0)
    bot_count = sum(1 for member in ctx.guild.members if member.bot)
    boost_count = ctx.guild.premium_subscription_count
    embed = discord.Embed(title="📊 Statistiques du serveur", description="Voici les statistiques actuelles du serveur.", color=0x57F287)
    embed.add_field(name="👥 Nombre total de membres", value=str(total_members), inline=False)
    embed.add_field(name="🟢 Membres en ligne", value=str(online_members), inline=False)
    embed.add_field(name="🔊 Membres en vocal", value=str(voice_channels), inline=False)
    embed.add_field(name="🤖 Nombre de bots", value=str(bot_count), inline=False)
    embed.add_field(name="✨ Nombre de boosts", value=str(boost_count), inline=False)
    embed.set_footer(text="Made by cyb3rtech")

    await ctx.send(embed=embed)

##############################################

@bot.command(name="ping")
async def ping(ctx):
    latency = bot.latency * 1000
    await ctx.send(f"Ping : {int(latency)}ms")

#############################################

@bot.command(name="invite")
async def invite(ctx):
    client_id = bot.user.id
    permissions = discord.Permissions(permissions=8)
    invite_url = discord.utils.oauth_url(client_id, permissions=permissions)
    await ctx.send(f"**Lien d'invitation du bot :** {invite_url}")

#############################################

@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print_dark_red(r""" ▄████▄▓██   ██▓ ▄▄▄▄   ▓█████  ██▀███  ▄▄▄█████▓▓█████  ▄████▄   ██░ ██ 
▒██▀ ▀█ ▒██  ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒▓  ██▒ ▓▒▓█   ▀ ▒██▀ ▀█  ▓██░ ██▒
▒▓█    ▄ ▒██ ██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒▒ ▓██░ ▒░▒███   ▒▓█    ▄ ▒██▀▀██░
▒▓▓▄ ▄██▒░ ▐██▓░▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  ░ ▓██▓ ░ ▒▓█  ▄ ▒▓▓▄ ▄██▒░▓█ ░██ 
▒ ▓███▀ ░░ ██▒▓░░▓█  ▀█▓░▒████▒░██▓ ▒██▒  ▒██▒ ░ ░▒████▒▒ ▓███▀ ░░▓█▒░██▓
░ ░▒ ▒  ░ ██▒▒▒ ░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░  ▒ ░░   ░░ ▒░ ░░ ░▒ ▒  ░ ▒ ░░▒░▒
  ░  ▒  ▓██ ░▒░ ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░    ░     ░ ░  ░  ░  ▒    ▒ ░▒░ ░
░       ▒ ▒ ░░   ░    ░    ░     ░░   ░   ░         ░   ░         ░  ░░ ░
░ ░     ░ ░      ░         ░  ░   ░                 ░  ░░ ░       ░  ░  ░
░       ░ ░           ░                                 ░                """)

    print_dark_blue("\n             Made By Cyb3rtech                  \n")  
    print_dark_red(f"❮+❯・{bot.user.name} est en ligne !")
    print_dark_red("❮+❯・discord : https://discord.gg/HBVt4vZ77g")
    
    await bot.change_presence(activity=discord.Streaming(name="Made By Cyb3rtech", url="https://www.twitch.tv/cyb3rtech_kdo"))

bot.run(token)