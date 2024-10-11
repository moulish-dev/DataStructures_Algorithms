# Testing 

helps catch bugs in the projects

Tools: pytest, doctest, unittest, tox , nose

Unit Test: for individual parts of code (i.e functions, methods) to test in isolation
Integration Test: for different parts of the systemto work
End to End test: simulate real world user scenarios
Regression Tests: Ensure new changes don't break previous coded functions

# Pytest
support for reusable setup of resources (i.e fixtures)
builtin support for assertions
extensible with plugins

# Doctest
allows to write tests inside docstrings
verifies from examples in documentation

setup
import doctest
doctest.testmod() 

# unittest
object oriented test structure
provides several assert methods

to find all test files and run them all
python -m unittest discover

# pyunit is same as unittest

# tox
automate testing in multiple python environments
commonly used in ci/cd pipelines
linting and formatting enforcement included

# nose  -- superseeded by pytest
older and depreceated
similar to unittest but with plugin support
not recommended as not actively maintained
pytest recommended instead of this