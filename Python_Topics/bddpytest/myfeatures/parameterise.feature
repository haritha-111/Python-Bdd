
@bddparam
Feature: Parameterizing tests in Pytest BDD

    Scenario: Check varieties of fruits
      Given there are 3 varieties of fruits
      When we add a same variety of fruit
      Then there is same count of varieties
      But if we add a diff variety of fruit
      Then the count of varieties incresaes to 4


@bddscenario
      Scenario: Parameterised benefits
        Given Given there are 5 fruits
        When I eat 3 fruits
        And  I eat 2 fruits
        Then I should have 0 fruits




