from pytest_bdd import scenario, given, when, then, scenarios
from pathlib import Path
import pytest


featureFileDir = 'myfeatures'
featureFile = 'first101.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE= BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

scenarios(FEATURE_FILE)

@given('there are 3 varieties of fruits', target_fixture='fruits')
def existing_fruits():
    fruits = {'apples', 'grapes', 'bananas'}
    return fruits

@when('we add a same variety of fruit')
def add_fruit(fruits):
    fruits.add('plums')

@then('there is same count of varieties')
def same_count(fruits):
    assert len(fruits) == 3

@then('if we add a diff variety of fruit')
def add_diff_variety(fruits):
    frutis.add("cherrys")

@then(parsers.parse('the count of varieties incresaes to {count:d}'))
def count_increases(fruits, count):
    print(fruits)
    assert len(fruits) == count
###end of the 1st scenario#####
pytest.total_fruits = 0

@given(parsers.parse('Given there are {count:d} fruits'), target_fixture='start_fruits')
def existing_fruits(count):
    pytest.total_fruits = count
    return dict(start = count, eat = 0)

@when(parsers.parse('I eat {count:d} fruits'))
def eat_fruit(start_fruits, eat):
        start_fruits["eat"] += eat
        print(start_fruits)

@then(parsers.parse('I should have {left:d} fruits'))
def should_have_left_fruits(start_fruits, left):
    assert start_fruits['start'] == pytest.total_fruits
    assert pytest.total_fruits - start_fruits['eat'] == left




