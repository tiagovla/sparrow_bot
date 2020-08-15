import os, aiohttp, asyncio

from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands.errors import ExtensionFailed

#load enviroment variables from ./bot.env
load_dotenv(dotenv_path='../env/bot.env')

#try to use uvloop policy
try:
    import uvloop
except ImportError:
    pass
else:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    
class SparrowBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', fetch_offline_members=False)
    
    async def on_ready(self):
        self.remove_command('help')
        print(f'{self.user} has connected.')
        
    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)
    
    def run(self):
        token = os.environ.get('BOT_TOKEN')
        super().run(token, reconnect=True)
        
        
if __name__ == "__main__":
    bot = SparrowBot()
    bot.run()
