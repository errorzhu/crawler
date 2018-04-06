# -*- coding: utf-8 -*-

from config import config
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class DbClient(object):
    def __init__(self):
        self.__dbtype = config.get_config('database', 'dbtype')
        self.__initDbClient()

    def __initDbClient(self):
        """
        init DB Client
        :return:
        """
        __type = None
        if "sqlite" == self.__dbtype:
            __type = "SQLiteClient"
        else:
            pass
        assert __type, 'type error, Not support DB type: {}'.format(self.config.dbtype)
        self.client = getattr(__import__(__type), __type)()

    def get(self):
        return self.client.get()

    def get_all(self):
        return self.client.get_all()

    def update(self, ip):
        self.client.update(ip)

    def put(self, data):
        self.client.put(data)

    def delete(self, ip):
        self.client.delete(ip)

    def close(self):
        self.client.close()


if __name__ == "__main__":
    db = DbClient()
    db.get_client()
