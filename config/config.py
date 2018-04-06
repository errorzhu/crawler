# -*- coding: utf-8 -*-

import configparser
import os


# 获取config配置文件
def get_config(section, key):
    config = configparser.ConfigParser()
    tmp_path = os.path.split(os.path.realpath(__file__))[0]
   # print(os.path.dirname(tmp_path))
    path = os.path.join(os.path.dirname(tmp_path), 'crawler.conf')
    path = os.path.realpath(path)
    config.read(path)
    return config.get(section, key)

if __name__ =="__main__":
    print (get_config('database','dbtype'))
