from logging import basicConfig, getLogger, StreamHandler, info, error, debug, warning, DEBUG

basicConfig(level=DEBUG)

def redefine_loglevel(_level: str):
    basicConfig(level=_level)
    logger = getLogger()
    for handler in logger.handlers:
        if isinstance(handler, type(StreamHandler())):
            handler.setLevel(level=_level)
