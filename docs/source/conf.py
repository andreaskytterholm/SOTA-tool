# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys; sys.setrecursionlimit(3000)

project = 'SOTA tool'
copyright = '2024, Andrea Skytterholm and Nektaria Kaloudi'
author = 'Andrea Skytterholm and Nektaria Kaloudi'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'

html_theme = 'sphinx_rtd_theme'

RTD_NEW_THEME = True

html_theme_options = {
    'display_version': False,
}

html_show_sphinx = False

html_static_path = ['_static']

html_css_files = [
    'nemecys_theme.css',
]

html_logo = "nemecys_logo.png"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}
