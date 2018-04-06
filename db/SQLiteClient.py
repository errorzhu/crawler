# -*- coding: utf-8 -*-
import sqlite3
import datetime
import random
import os

tmp_path = os.path.split(os.path.realpath(__file__))[0]
# print(os.path.dirname(tmp_path))
db_file = os.path.join(tmp_path, 'proxy.db')


class SQLiteClient(object):
    def __init__(self):
        self.connection = sqlite3.connect(db_file)


    def connect(self):
        self.connection = sqlite3.connect(db_file)

    def close(self):
        self.connection.close()
    def get(self):
        cursor = self.connection.cursor()
        proxys = cursor.execute('SELECT ip FROM proxy').fetchall()
        result = random.choice(proxys)[0]
        cursor.close()
        return result

    def get_all(self):
        cursor = self.connection.cursor()
        proxys = cursor.execute('SELECT ip FROM proxy').fetchall()
        cursor.close()
        return [x[0] for x in proxys]

    def update(self, ip):
        sql = "update proxy set inserttime ='%s' where ip ='%s'" % (
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ip)
        self.connection.execute(sql)
        self.connection.commit()

    def put(self, data):
        self.connection.executemany(
            'INSERT INTO proxy VALUES (?,?)',
            [(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x) for x in data]
        )
        self.connection.commit()
        self.connection.close()

    def delete(self, ip):
        sql = "delete from proxy where ip ='%s'" % ip
        self.connection.execute(sql)
        self.connection.commit()



# conn = sqlite3.connect('proxy.db')


if __name__ == "__main__":
    client = SQLiteClient()
    client.delete('114.239.253.38:6666')
