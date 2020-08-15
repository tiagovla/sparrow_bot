import logging, os
import logging.config

os.makedirs('logs', exist_ok=True)

class ExactLevelFilter(logging.Filter):
    def __init__(self, level):
        self.__level = level

    def filter(self, record):
        return record.levelno == self.__level

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': { 
        'standard': { 
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'filters': {
        'info_filter': {
            '()': ExactLevelFilter,
            'level': logging.INFO,
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'DEBUG'
        },
        'file_bot_info': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filters': ['info_filter'],
            'filename': 'logs/bot_info.log',
            'formatter': 'standard',
            'maxBytes': 2048, 
            'backupCount':1,
        },
        'file_bot_error': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/bot_error.log',
            'formatter': 'standard',
            'level': 'WARNING',
            'maxBytes': 2048, 
            'backupCount':1,
        },
        'file_error': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/error.log',
            'formatter': 'standard',
            'level': 'WARNING',
            'maxBytes': 2048, 
            'backupCount':1,
        },
    },
    'loggers': { 
        '': {
            'level': 'WARNING',
            'handlers': ['file_error']
        },
        'bot': { 
            'level': 'INFO',
            'handlers': ['console','file_bot_info', 'file_bot_error'],
        },
        'cogs':{
            'level': 'INFO',
            'handlers': ['console','file_bot_info', 'file_bot_error'],
        },
        '__main__':{
            'level': 'INFO',
            'handlers': ['console','file_bot_info', 'file_bot_error'],
        },
        'discord': { 
            'level': 'WARNING',
        },
    }
}


if __name__ == '__main__':
    logging.config.dictConfig(LOGGING_CONFIG)
    logging.debug('debug')
    logging.info('info')
    logging.error('error')