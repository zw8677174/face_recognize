import json
from app import log


def debug(content):
    if content is str:
        log.debug(content)
    else:
        log.debug(json.dumps(content))


def warning(content):
    log.debug(content)
