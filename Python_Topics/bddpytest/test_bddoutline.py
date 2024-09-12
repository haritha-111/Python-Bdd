from pytest_bdd import scenario, given, when, then, scenarios
from pathlib import Path
import pytest


featureFileDir = 'myfeatures'
featureFile = 'sceneoutline.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE= BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

#scenarios(FEATURE_FILE)

@scenario(FEATURE_FILE, 'Scenario outline test')
def test_outline():
    pass

@given(parsers.parse('there are {start:d} cucumbers'), target_fixture='cucumbers')
def existing_cucumbers(start):
        return dict(start = start)

@when(parsers.parse('I deposit {deposit:d} cucumbers'))
def deposit_cucumbers(cucumbers, deposit):
        cucumbers["deposit"] = deposit
        print(cucumbers)
        print(cucumbers)
        print(cucumbers)
        print(cucumbers)
        print(cucumbers)

@when(parsers.parse('I withdraw {withdraw:d} cucumbers'))
def withdraw_cucumbers(cucumbers, withdraw):
        cucumbers["withdraw"] = withdraw
        print(cucumbers)

@then(parsers.parse('I should have {final:d} cucumbers'))
def final_cucumbers(cucumbers, final):
    assert cucumbers['start'] + cucumbers ['deposit'] - cucumbers['withdraw'] == final

