Feature: Testing Google Site
  Scenario: visit google and check content
    When visit url "http://www.google.com/"
    Then it should have a tag "html"


  Scenario: can find search results
      When visit url "http://git c.google.com/"
      When field with name "q" is given "Behave"
      Then title becomes "Behave"
