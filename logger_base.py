from logging import *

basicConfig(level=INFO,
            format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
            datefmt = '%I:%M:%S %p',
            handlers = [
                    FileHandler('dates_users.log'),
                    StreamHandler()
                ])

if __name__ == '__main__':
    debug('DEBUG MESSAGE')
    info('INFORMATION MESSAGE')
    warning('WARNING MESSAGE')
    error('ERROR MESSAGE')
    critical('CRITICAL MESSAGE')
