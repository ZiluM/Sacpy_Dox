# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
import pathlib
import sys
import os
import matplotlib.sphinxext
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())
# sys.path.append(os.path.abspath('matplotlib'))


# -- Project information -----------------------------------------------------

project = 'Sacpy'
copyright = '2023, ZiluMeng'
author = 'ZiluMeng'

# The full version, including alpha/beta/rc tags
release = '0.16'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'nbsphinx',
    'sphinx.ext.autodoc',
]

html_theme_options = {
    'repository_url': 'https://github.com/ZiluM/sacpy',
    'use_edit_page_button': True,
    'use_repository_button': True,
    'use_issues_button': True,
    'use_fullscreen_button': False,
}
html_logo = 'sacpy.jpeg'
#     'sphinx.ext.duration',
#     'sphinx.ext.doctest',
#     'sphinx.ext.autodoc',
#     'sphinx.ext.autosummary',
#     'nbsphinx',
#     # 'matplotlib.sphinxext.only_directives',
#     'matplotlib.sphinxext.plot_directive',
#     'IPython.sphinxext.ipython_console_highlighting',
#     'IPython.sphinxext.ipython_directive',
# ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# html_theme_options = {
#     'repository_url': 'https://github.com/fzhu2e/cfr',
#     'use_edit_page_button': True,
#     'use_repository_button': True,
#     'use_issues_button': True,
#     'use_fullscreen_button': False,
# }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

