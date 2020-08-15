import discord
from discord.ext import commands

import logging

log = logging.getLogger(__name__)

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client
        log.info(f'Cog was loaded.')

    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print('Bot is online.')

    @commands.command()
    async def ping(self,ctx):
        await ctx.send('Pong!')
            
    def cog_unload(self):
        log.info(f'Cog was unloaded.')
        

def setup(client):
    client.add_cog(Example(client))
