#!/usr/bin/env python3
#antuor:Alan

####假设的数据库####

from config import settings

def db_auth(configs):
    if configs.DATABASE["user"] == 'root' and configs.DATABASE['password'] == 123:
        print("db authentication passed")
        return True
    else:
        print("db loggin error...")

def select(table,column):
    if db_auth(settings):  #通常不写这，为了省时间 调用settings.DATABASE
        if table =='user':
            user_info = {
                "001":['alan',27,'engineer'],
                "002":['kobe',39,'bbplayer'],
                "003":['jackey',45,'singer'],
            }
            return user_info

