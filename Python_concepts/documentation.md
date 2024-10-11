# Sphinix : for Python Documentation

automatically creates documentation from source code using reST(reStructuredText) or Markdown
supports various output formats: HTML, LaTeX, ePub, PDF and many more
also has many advanced features like tools of Read the Docs and automatically generates API documentations
also customizes documentation look

# Setting up

install sphinix
pip install sphinix

for configuration process
sphinix-quickstart

index.rst  -- starting point of documentation

to generate html pages
make html

various extensions also available

sphinx.ext.autodoc: Automatically generates documentation from Python docstrings.
sphinx.ext.napoleon: Supports Google style and NumPy style docstrings.
sphinx.ext.viewcode: Adds links to the Python source code in the documentation.
sphinx.ext.githubpages: Creates documentation that can be hosted on GitHub Pages

also can change from rst to Markdown formatting
pip install recommonmark
extensions = ['recommonmark']
source_suffix = ['.rst', '.md']

to change themes
pip install sphinx_rtd_theme
then in conf.py
html_theme = 'sphinx_rtd_theme'

# Sphinx is a robust tool for generating project documentation.

# It supports docstring parsing to create documentation from your codebase.

# You write documentation using reStructuredText or Markdown.

# It provides various extensions and themes for customizing your documentation.

# You can host the documentation on services like Read the Docs or GitHub Pages.