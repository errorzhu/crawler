# -*- coding: utf-8 -*-
import requests
from common import const


class HttpQuest(object):
    def __init__(self):
        pass

    def get_html(self, url):
        try:
            html = requests.get(url, headers=const.HEADER)
            return html.text
        except  Exception as e:
            print(e)

    def valid_proxy(self,proxy):
        proxies = {"http": "http://{proxy}".format(proxy=proxy)}
        try:
            # 超过20秒的代理就不要了
            r = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=10, verify=False)
            if r.status_code == 200:
                return True
        except Exception as e:
            return False


if __name__ == "__main__":
    url = r'http://www.xicidaili.com/'
    quest = HttpQuest()
    html = quest.get_html(url)
    print(html)
