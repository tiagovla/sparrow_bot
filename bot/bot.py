import os, aiohttp, logging
from discord.ext import commands
from discord.ext.commands.errors import ExtensionFailed

log = logging.getLogger(__name__)
    
class SparrowBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', fetch_offline_members=False)
        self.loop.run_until_complete(self._setup())
    
    async def on_ready(self):
        self.remove_command('help')
        log.info(f'{self.user} has connected.')
        
    async def _setup(self):
        self.load_cogs()
        
    def load_cogs(self):
        try:
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    try:
                        self.load_extension(f'cogs.{filename[:-3]}')
                    except ExtensionFailed as e:
                        log.error(f"Failed to load extension {filename} - Error: {e}")
        except FileNotFoundError:
            log.error("Wrong path to cogs or no cogs to load.")
        
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
