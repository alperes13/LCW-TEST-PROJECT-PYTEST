----------------------"INSTALLATION"--------------------
Before you start, you need to be sure about you have several tools as:

pytest
selenium
webdriver-manager
pytest-html (if you run single test, it is not necessarry)
softest
---------------------------"RUN"------------------------
if you have, there are different options to run test cases:

1- Single: go to any test case (under of testcases folder), right click,
run. (But you can not get html report if you run single.)

2- Multiple:

	2.1: Copy "testcases" folder path, open a command prompt, navigate the path,
	then paste that : "pytest -v --html=../reports/automation_test_report.html"

ABOUT LOGGERS : You can see test logs in the html report.

--------------------------
terminal: python --help
pytest: pytest --help

alper.ees1@gmail.com
https://www.linkedin.com/in/alperes/
--------------------------