import pytest


def test_case01():
    with pytest.raises(Exception):
         assert (1/0)

def test_case02():
    with pytest.raises(ZeroDivisionError):
         assert (1/0)

def test_case03():
    with pytest.raises(AssertionError):
         assert 3 > 3


def func1():
    raise ValueError("Exception func1 raised")

def test_case04():
    with pytest.raises(AssertionError) as exif:
         #assert (1,2,3) == (1,2,4)
        func1()
    print (str(exif.value))
