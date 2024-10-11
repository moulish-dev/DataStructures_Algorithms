# Code Formatting
useful in making code more readable and maintanable

# Python has an official style guide called PEP 8, which defines conventions for writing readable and consistent Python code. Some aspects of PEP 8 include:
Indentation: 4 spaces per indentation level.
Line Length: Keep lines to a maximum of 79 characters.
Blank Lines: Use blank lines to separate functions, classes, and blocks of code.
Spaces around Operators: Use spaces around operators (a = b + c), but not for function arguments (func(a, b)).
Naming Conventions: Use snake_case for variables and functions, and PascalCase for classes.

# Tools: yapf, black, ruff

# YAPF : Yet Another Python Formatter
formats code to balance readability

to install yapf
pip install yapf

to format a single file
yapf --in-place myfile.py

to format all files in a directory (rescursively)
yapf --in-place --recursive .

# Black
reformats code with strong set of rules
fast, deterministic and simple to use
strong focus on eliminating "bike-shedding" over code-style debates

to install black
pip install black

to format a file
black file_name.py

to format all files
black .

# Ruff : Formatter and Linter
configurable fast linter with formatting capability
supports code linting and autofixing
can be configured to enforce PEP 8 and other rules
configurations also done through pyproject.toml file

to install ruff
pip install ruff

using for linting and formatting
ruff check file_name.py

automatically fix formatting issues
ruff --fix file_name.py

# YAPF is useful when you want flexibility and control over how your code is formatted.

# Black is a zero-configuration tool that enforces a strict, uncompromising style.

# Ruff is a fast tool that combines linting and formatting, allowing you to maintain both code quality and consistency.

# For Workflow
Use Black as the primary formatter to maintain consistency across your project. It handles the bulk of the formatting.
Use Ruff as a linter and auto-fixer to catch style issues, unused imports, or potential bugs.
Optionally, use YAPF if you need fine-grained control over formatting, although in many cases, Black and Ruff together are enough.