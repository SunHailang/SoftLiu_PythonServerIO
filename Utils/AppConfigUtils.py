'''
    __author__ = Sun Hai Lang
    __date__ = 2019-09-16

'''

import json

app_config = {}

def initAppConfig(path):
    with open(path, 'r') as js:
        global app_config
        app_config = json.load(js)

def getPlatform():
    global app_config
    platform = app_config['platform']
    return platform

def getMySqlConfig():
    global app_config
    ip = app_config['mysql_IP']
    username = app_config['mysql_username']
    password = app_config['mysql_password']
    database = app_config['mysql_database']
    return ip, username, password, database


def getTcpConfig():
    global app_config
    host = app_config['tcp_host']
    ip = app_config['tcp_IP']
    port = app_config['tcp_port']
    return host, ip, port

def getUdpConfig():
    global app_config
    ip = app_config['udp_IP']
    port = app_config['udp_port']
    return ip, port

if __name__ == "__main__":
    path = 'Resources/AppConfig.json'
    initAppConfig(path)
    print(getMySqlConfig())
    print(getTcpConfig())
    print(getUdpConfig())
