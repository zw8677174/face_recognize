from app import app
import json


class Log:

    @staticmethod
    def debug(content):
        if content is str:
            app.logger.debug(content)
        else:
            app.logger.debug(json.dumps(content))

    @staticmethod
    def warning(content):
        app.logger.debug(content)
