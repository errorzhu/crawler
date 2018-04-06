# -*- coding: utf-8 -*-
from spider.quest import HttpQuest

from bs4 import BeautifulSoup

"""
66ip.cn
data5u.com
ip181.com
xicidaili.com
goubanjia.com
xdaili.cn
kuaidaili.com
cn-proxy.com
www.mimiip.com
proxy-list.org
cz88.net
ip181.com
"""


class ProxyGetter(object):
    def __init__(self):
        self.__quest = HttpQuest()

    def get_proxy_first(self):
        url = r'http://www.xicidaili.com/'
        html = self.__quest.get_html(url)
        bs = BeautifulSoup(html, 'lxml')
        res = bs.find_all('tr')
        for item in res:
            try:
                tds = item.find_all('td')
                ip = tds[1].text
                port = tds[2].text
                yield (ip + ":" + port)
            except IndexError:
                pass


if __name__ == "__main__":
    proxy = ProxyGetter()
    proxys = proxy.get_proxy_first()
    for p in proxys:
        print (p)
