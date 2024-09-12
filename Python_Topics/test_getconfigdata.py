from Python_Topics.utils.myconfigparser import*
from Python_Topics.utils.ConfigFileParser import ConfigFileParser



config = ConfigFileParser('prod.ini')
def test_getGmailUrl():
    print(getGmailUrl())

def test_getOutlookUrl():
    print(config.getOutlookUrl())




