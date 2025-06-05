# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys; sys.setrecursionlimit(3000)

project = 'Cyber compass tool'
copyright = '2025 All Rights Reserved by the NEMECYS Consortium'
author = 'Andrea Skytterholm'
release = '1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_design',
              'sphinx_tabs.tabs']

templates_path = ['_templates']
exclude_patterns = []

remove_from_toctrees = []



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

html_logo = "logo.png"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'prev_next_buttons_location': None,
}

