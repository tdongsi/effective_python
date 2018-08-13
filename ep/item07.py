import logging
from contextlib import contextmanager


@contextmanager
def debug_logging(level):
    """Set logging context to the given level"""
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


@contextmanager
def swallow_exception(cls):
    """Ignore exception of the given class"""
    try:
        yield
    except cls:
        logging.exception('Swallow exception')


@contextmanager
def log_level(level, name):
    """Get logger of the specified name and level"""
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)


logging.getLogger().setLevel(logging.WARNING)


def my_function():
    logging.debug('Some debug info')
    logging.error('A real error!')
    logging.debug('More debugging')


def main():
    my_function()

    with debug_logging(logging.DEBUG):
        my_function()

    with swallow_exception(ZeroDivisionError):
        value = 20 / 0

    with log_level(logging.DEBUG, 'mylogger') as logger:
        logger.debug('test')
        logging.debug('Global logger: test')


if __name__ == '__main__':
    main()
