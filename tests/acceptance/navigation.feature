Feature: Patikrinti rysius ytarp puslapiu
  SimpleBlog testavimo pavyzdys

  Scenario: Is Homepage galima nueiti prie Blog
    Given Esu Home puslapyje
    When Paspaudziu nuoroda id "blog-link"
    Then Patenku i Blog puslapi
