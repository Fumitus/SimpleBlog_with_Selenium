Feature: Test that pages have correct content
  Scenario: Blog page has a correct title
    Given Esu Blog puslapyje
    Then Puslapyje yra rodoma antraste
    And Puslapio antraste yra "This is the blog page"

  Scenario: Home page has a correct title
    Given Esu Home puslapyje
    Then Puslapyje yra rodoma antraste
    And Puslapio antraste yra "This is the home page"
