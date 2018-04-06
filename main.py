# -*- coding: utf-8 -*-
from multiprocessing import Process
from api.api import run as  api
from schedule.schedule import refresh as  ProxyRefresh
from schedule.schedule import download as  ProxyDownload
def run():
    p_list = list()
    p1 = Process(target=api, name='ProxyApiRun')
    p_list.append(p1)
    p2 = Process(target=ProxyRefresh, name='ProxyRefresh')
    p_list.append(p2)
    p3 = Process(target=ProxyDownload, name='ProxyDownload')
    p_list.append(p3)

    for p in p_list:
        p.daemon = True
        p.start()
    for p in p_list:
        p.join()


if __name__ == '__main__':
    run()
