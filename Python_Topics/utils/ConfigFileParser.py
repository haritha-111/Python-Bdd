import configparser
from pathlib import Path

from Python_Topics.utils.myconfigparser import cfgFile


class ConfigFileParser():
    cfgFile = 'qa.ini' #default config file
    cfgFileDirectory = 'config' #config Directory
    config = configparser.ConfigParser()

def __init__(self, cfg=cfgFile):
    self.cfgFile = cfg
    self.BASE_DIR= Path(__file__).parent.absolute().resolve().parent.parent
    self.CONFIG_FILE = self.BASE_DIR.joinpath(self.cfgFileDirectory).joinpath(self.cfgFile)
    self.config.read(self.CONFIG_FILE)

def getGmailUrl(self):
    return self.config['gmail']['Url']

def getGmailUser(self):
    return self.config['gmail']['user']

def getGmailPassword(self):
    return self.config['gmail']['pass']

def getOutlookUrl(self):
    return self.config['outlook']['url']

if __name__ == '__main__':
    config = ConfigFileParser('prod.ini')
    print(config.getGmailUser())
    print(config.getOutlookUrl)




