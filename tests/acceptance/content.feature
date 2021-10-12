Feature: Test that pages have correct content
  Scenario: Blog page has a correct title
    Given Esu Blog puslapyje
    Then Puslapyje yra rodoma antraste
    And Puslapio antraste yra "This is the blog page"

  Scenario: Home page has a correct title
    Given Esu Home puslapyje
    Then Puslapyje yra rodoma antraste
    And Puslapio antraste yra "This is the home page"

  Scenario: Vartotojas gali sukurti nauja irasa
    Given Esu Naujo Iraso puslapyje
    When Ivedu "naujas irasas" i "title" laukeli
    And Ivedu "naujo iraso tekstas" i "content" laukeli
    And Paspaudziu "submit" mygtuka
    Then Atsidaro "Blog" puslapis
    Given Laukti kol puslapis uzsikraus, bet ne ilgaiu nei 5s
    Then  Matau irasa kurio title yra "naujas irasas"


  Scenario: Blog puslapis uzkrauna irasus
    Given Esu Blog puslapyje
    And Laukti kol puslapis uzsikraus, bet ne ilgaiu nei 5s
    Then Irasu skiltis yra Post puslapyje
