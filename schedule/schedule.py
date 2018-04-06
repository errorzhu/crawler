# -*- coding: utf-8 -*-
# 定时任务 1 验证代理

from db.dbclient import DbClient
from proxy.proxy import ProxyGetter
from spider.quest import HttpQuest
import time
import sys
sys.path.append('../')
class ProxySchedule(object):
    def __init__(self):
        self.__db = DbClient()
        self.__quest = HttpQuest()
        self.__proxy = ProxyGetter()

    def delete_unused_proxy(self):
        for ip in self.__db.get_all():
            if self.__quest.valid_proxy(ip):
                self.__db.update(ip)
                print('proxy {ip} has updated'.format(ip=ip))
            else:
                self.__db.delete(ip)
                print('proxy {ip} has deleted'.format(ip=ip))
            time.sleep(1)
        self.__db.close()

    def get_proxy(self):
        proxys = self.__proxy.get_proxy_first()
        self.__db.put(proxys)
        self.__db.close()


def refresh():
    schedule = ProxySchedule()
    while True:
        schedule.delete_unused_proxy()
        time.sleep(60 * 60 * 1)


def download():
    schedule = ProxySchedule()
    while True:
        schedule.get_proxy()
        time.sleep(60 * 60 * 5)


if __name__ == "__main__":
    schedule = ProxySchedule()
