import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import json
import config
import aiohttp
import os, random
import asyncio
import subprocess


#TODO:
#Add web bot description

class bt():
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    @commands.command(pass_context=True)
    async def rulesaccept(self, ctx):
        """Accept rules :D"""
        author = ctx.message.author
        role = discord.utils.get(author.server.roles, name="Accepted")
        await self.bot.add_roles(author, role)
        await self.bot.send_message(author, "Welcome to MDBL!")
        await self.bot.say("Accepted rules!")

    #role = get(ctx.message.server.roles, name='member')
    #await bot.remove_roles(user, role)

    @commands.command(pass_context=True)
    async def nsfw(self, ctx, opt=""):
        """Hide/Show Nsfw Channels"""
        author = ctx.message.author
        if opt == "":
            await self.bot.say("<@{}> usage: `@!nsfw show/hide`".format(ctx.message.author.id))
        if opt == "show":
            try:
                role = discord.utils.get(ctx.message.server.roles, name='NoNsfw')
                await self.bot.remove_roles(ctx.message.author, role)
                await self.bot.say("You can now view NSFW channels")
            except Exception as e:
                exc = ':x: {}: {}'.format(type(e).__name__, e)
                await self.bot.say(exc)
                await self.bot.say("You can now view NSFW channels")
        if opt == "hide":
            role = discord.utils.get(author.server.roles, name="NoNsfw")
            await self.bot.add_roles(author, role)
            await self.bot.say("You can no longer view NSFW channels")
            
        
    

    
def setup(bot):
    bot.add_cog(bt(bot))
