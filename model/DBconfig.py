from peewee import *


class DatabaseConfig:

    @staticmethod
    def get_zpc_base():
        return MySQLDatabase('face_reg', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': '49.232.87.103', 'port': 3306, 'user': 'zw', 'password': 'Zongwen123!@#'})
