
def test_orgtest01(CmdOpt):
    #print ("Read Config file" + CmdOpt.readline())

    assert CmdOpt.readline().index('Lab')
