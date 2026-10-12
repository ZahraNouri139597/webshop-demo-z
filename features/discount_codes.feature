
Feature: Discount codes at checkout
  As a logged-in customer
  I want to apply a discount code at checkout
  So that I pay less for my order
  Background:
    Given the current date is "2026-10-07"
    And shipping costs are €4.95
  @AC1
  Scenario: Valid code discounts the products but not the shipping
    Given I am logged in as "ben@test.example"
    And my product subtotal is €80.00
    When I apply the code "SPRING10"
    Then the discount is €8.00
    And the order total is €76.95



@AC2
  Scenario: Code is not case-sensitive and surrounding spaces are ignored
    Given I am logged in as "ben@test.example"
    And my product subtotal is €80.00
    When I apply the code " spring10 "
    Then the discount is €8.00
    And the order total is €76.95

@AC4
  Scenario: Code that does not exist is rejected
    Given I am logged in as "ben@test.example"
    And my product subtotal is €80.00
    When I apply the code "TEST1234"
    Then I see the message "This discount code does not exist."
    And the order total is €84.95


 @AC5
  Scenario: Expired code is rejected
    Given I am logged in as "ben@test.example"
    And my product subtotal is €150.00
    When I apply the code "SUMMER20"
    Then I see the message "This discount code expired on 2026-08-31."
    And the order total is €154.95


