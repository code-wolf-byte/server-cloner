import discord, os, platform

from src.utils import *
from colorama import Fore, init, Style
from os import system
init(autoreset=True, convert=True) # feel free to remove this line if you are having print issues
os_ = platform.system()
if os_ == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.CYAN}
                       
░█▀▀▄ ▀█▀ ░█▀▀▀█ ░█▀▀█ ░█▀▀▀█ ░█▀▀█ ░█▀▀▄ 　 ░█▀▀▀█ ░█▀▀▀ ░█▀▀█ ░█──░█ ░█▀▀▀ ░█▀▀█ 　 ░█▀▀█ ░█─── ░█▀▀▀█ ░█▄─░█ ░█▀▀▀ ░█▀▀█ 
░█─░█ ░█─ ─▀▀▀▄▄ ░█─── ░█──░█ ░█▄▄▀ ░█─░█ 　 ─▀▀▀▄▄ ░█▀▀▀ ░█▄▄▀ ─░█░█─ ░█▀▀▀ ░█▄▄▀ 　 ░█─── ░█─── ░█──░█ ░█░█░█ ░█▀▀▀ ░█▄▄▀ 
░█▄▄▀ ▄█▄ ░█▄▄▄█ ░█▄▄█ ░█▄▄▄█ ░█─░█ ░█▄▄▀ 　 ░█▄▄▄█ ░█▄▄▄ ░█─░█ ──▀▄▀─ ░█▄▄▄ ░█─░█ 　 ░█▄▄█ ░█▄▄█ ░█▄▄▄█ ░█──▀█ ░█▄▄▄ ░█─░█             
                                    
{Style.RESET_ALL}                                  {Fore.MAGENTA}Developed by: whoevenistanay#0249{Style.RESET_ALL}
        """)
token = input(f'Please enter your token:\n >')
guild_s = input('Please enter guild id you want to copy:\n >')
guild = input('Please enter guild id where you want to copy:\n >')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your Account token
client = discord.Client()
if os_ == "Windows":
    os.system("title ServerCloner - Starting...")
print("ServerCloner - Starting...\n")

from src import ServerCloner
            
async def clone():
    guild = client.get_guild(int(input_guild_id))
    new_guild = client.get_guild(int(output_guild_id))

    cloner = ServerCloner(client, guild, new_guild, clear=True)
    await cloner.start()
    log(blue+'[ServerCloner]'+r, 'Server cloning process completed.')
    if os_ == "Windows":
        os.system('title ServerCloner - Completed')
        os.system('pause')

@client.event
async def on_ready():
    await clone()

client.run(token, bot=False)