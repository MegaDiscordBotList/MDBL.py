import discord
from discord.ext.commands import Bot
import logging
import config
import random
import sys, os, time
import json
import timeit
import psutil
import subprocess
start = timeit.default_timer()

def fcount(path):
    #Counts the number of files in a directory
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

logging.basicConfig(level=logging.INFO) # Configurates the logger
logger = logging.getLogger('discord')
bot = Bot(command_prefix=config.prefix) # Sets the client and sets the prefix
startup_extensions = ["bot"]

@bot.event
async def on_ready():
    cmds = len(bot.commands)
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    shards = ["1", "2", "3", "4"]
    game = "https://mdbl.surge.sh/"
    clear_screen()
    await bot.change_presence(game=discord.Game(name=game))
    if __name__ == "__main__":
        for extension in startup_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('Failed to load extension {}\n{}'.format(extension, exc))
    print("-=-=-=-=-=-=-=-\n"
          " MDBL\n"
          "-=-=-=-=-=-=-=-\n")
    print("Servers  {}\n"
          "Channels {}\n"
          "Users    {}\n".format(servers, channels, users))
    print("\n"
          "URL : https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=-1".format(bot.user.id))

@bot.command(pass_context=True)
async def reload(ctx, *, cog):
    """Admin Command!"""
    me = ctx.message.author
    if me.id in config.mods:
        try:
            bot.unload_extension(cog)
            bot.load_extension(cog)
            await bot.say("Reloaded!")
            print("The cog '{}' was reloaded".format(cog))
        except Exception as e:
            exc = ':x: {}: {}'.format(type(e).__name__, e)
            await bot.say(exc)
    else:
        await bot.say(":x:")

@bot.command(pass_context=True)
async def avatar(ctx, *, url=""):
    """Admin Command!"""
    author = ctx.message.author
    if author.id in config.mods:
        with open('avatar.jpg', 'rb') as f:
            await bot.edit_profile(avatar=f.read())

@bot.command(pass_context=True)
async def load(ctx, *, cog):
    """Admin Command!"""
    author = ctx.message.author
    if author.id in config.mods:
        try:
            bot.load_extension(cog)
            await bot.say("Loaded!")
            print("The cog '{}' was loaded".format(cog))
        except Exception as e:
            exc = ':x: {}: {}'.format(type(e).__name__, e)
            await bot.say(exc)
    else:
        await bot.say(":x:")

def start():
    try:
       bot.run(config.token)
    except:
        time.sleep(3)
        start()

start()
    
