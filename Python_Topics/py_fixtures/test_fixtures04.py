import pytest

months = ["jan", "feb", "march"]

def test_checkrequest(setup04):
    assert "april" in setup04
    assert len(setup04) == 4


def test_fact_ficture(setup05):
    assert type (setup05('list')) == list
    assert type(setup05('tuple')) == tuple

