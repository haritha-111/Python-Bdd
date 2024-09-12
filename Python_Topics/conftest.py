import os

import pytest

QA_config = 'qa.prop'
prod_config = 'prod.prop'


def pytest_addoption(parser):
    parser.addoption("__cmdopt", default= 'QA')


@pytest.fixture()
def CmdOpt(pytestconfig):
    print ("\ In CmdOpt fixture function")
    opt = pytestconfig.getoption('cmdopt')
    if opt == 'prod':
        f = open(os.path.join(os.path.dirname(__file__), prod_config), 'r')
        
    else:
        f = open(os.path.join(os.path.dirname(__file__),QA_config), 'r')
        yield f


