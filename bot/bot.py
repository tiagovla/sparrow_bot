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
        self.loop.run_until_complete(self._setup())
    
    async def on_ready(self):
        self.remove_command('help')
        print(f'{self.user} has connected.')
        
    async def _setup(self):
        self.load_cogs()
        
    def load_cogs(self):
        try:
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    try:
                        self.load_extension(f'cogs.{filename[:-3]}')
                        print(f"Extension {filename} was loaded.")
                    except ExtensionFailed as e:
                        print(f"Failed to load extension {filename} - Error: {e}")
        except FileNotFoundError:
            print("No cogs to load.")
        
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
