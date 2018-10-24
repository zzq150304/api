# import os
# import configparser
#
# cur_path = os.path.dirname(os.path.realpath(__file__))
# configPath = os.path.join(cur_path,'config.ini')
# conf = configparser.ConfigParser()
# conf.read(configPath)
#
# smtp_server = conf.get('email','smtp_server')
# sender = conf.get("email","sender")
# psw = conf.get("email",'psw')
# receiver = conf.get('email','receiver')
#
# port = conf.get('email','port')
from configparser import ConfigParser

class ReadConfig:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read('./config.ini')

    def get_server(self,name):
        print(self.config.sections())
        #读取配置文件
        value =self.config.get('testServer', name)
        return value

