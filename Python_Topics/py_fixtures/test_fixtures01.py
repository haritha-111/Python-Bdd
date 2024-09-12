import pytest

@pytest.fixture()
def setup_list():
    print("\n in fixtures...\n")
    city = [ 'newyork', 'london', 'singapore', 'mumbai', 'delhi']
    return city

def test_getItem(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == 'newyork'
    assert setup_list[::2] == ['newyork',  'singapore', 'delhi']

def myReverse(lst):
    lst.reverse()
    return lst

def test_reverseList(setup_list):
        assert setup_list[::-2] == ['delhi', 'singapore', 'newyork']
        assert setup_list[::-1] == myReverse(setup_list)


@pytest.mark.xfail(reason= "known issue: usefixutres cannt use the  fixtures retun value")
@pytest.mark.usefixtures("setup_list")
def test_usefixturedemo():
    assert 1 == 1
    print (setup_list[0])

