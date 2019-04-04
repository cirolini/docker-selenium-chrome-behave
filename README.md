# Docker Selenium Chrome and Behave

This project generate a Docker container with Behave <https://behave.readthedocs.io>, Selenium <https://github.com/SeleniumHQ/selenium> and Chrome Headless.

This ideia is create a container with all necessary to run behave tests in a pipeline workflow. With this container you can simulate a user with a chrome browser to open your pages, clic in buttons, expect things and tests your entire application.

## Execute

'''
$ docker build -t docker-behave .
$ docker run docker-behave
Feature: Testing Google Site # features/google.feature:1

  Scenario: visit google and check content  # features/google.feature:2
    When visit url "http://www.google.com/" # features/steps/steps.py:3
    Then it should have a tag "html"        # features/steps/steps.py:7

  Scenario: can find search results            # features/google.feature:7
    When visit url "http://www.google.com/"    # features/steps/steps.py:3
    When field with name "q" is given "Behave" # features/steps/steps.py:12
    Then title becomes "Behave"                # features/steps/steps.py:19

1 feature passed, 0 failed, 0 skipped
2 scenarios passed, 0 failed, 0 skipped
5 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m10.177s
'''
