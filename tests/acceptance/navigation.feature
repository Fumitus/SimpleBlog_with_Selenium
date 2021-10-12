Feature: Patikrinti rysius tarp puslapiu
  SimpleBlog testavimo pavyzdys

  Scenario: Is Homepage puslapio galima nueiti i Blog puslapi
    Given Esu Home puslapyje
    When Paspaudziu nuoroda "Go to blog"
    Then Atsidaro "Blog" puslapis

  Scenario: Is Blog puslapio galima nueiti i Home puslapi
    Given Esu Blog puslapyje
    When Paspaudziu nuoroda "Go to home"
    Then Atsidaro "Home" puslapis
