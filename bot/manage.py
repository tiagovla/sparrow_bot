import asyncio
from dotenv import load_dotenv
from logging_config import LOGGING_CONFIG
from contextlib import contextmanager
import logging
from bot import SparrowBot
import click

#load enviroment variables from bot.env
load_dotenv(dotenv_path='../env/bot.env')

#try to use uvloop policy
try:
    import uvloop
except ImportError:
    pass
else:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    
@click.group()
def cli():
  pass

@cli.command()
def runbot():
    with load_logging_config(LOGGING_CONFIG):
        bot = SparrowBot()
        bot.run()
    
@contextmanager
def load_logging_config(logging_config=None):
    """load logging config"""
    
    try:
        log = logging.getLogger(__name__)
        if logging_config:
            logging.config.dictConfig(logging_config)
        yield
         
    finally:
        handlers = log.handlers[:]
        for handler in handlers:
            handler.close()
            log.removeHandler(handler)
    
if __name__ == "__main__":
    cli()