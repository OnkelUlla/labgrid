#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# labgrid documentation build configuration file, created by
# sphinx-quickstart on Mon Feb 20 10:00:00 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from pkg_resources import get_distribution

# Import read_the_docs theme
import sphinx_rtd_theme

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.napoleon',
              'sphinx.ext.coverage',
              'sphinx.ext.viewcode',
              'sphinx.ext.autosectionlabel']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'labgrid'
copyright = '2016-2021 Pengutronix, Jan Luebbe and Rouven Czerwinski'
author = 'Jan Luebbe, Rouven Czerwinski'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = get_distribution('labgrid').version
# The short X.Y version.
version = '.'.join(release.split('.')[:2])

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['.build', 'Thumbs.db', '.DS_Store', 'RELEASE.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Set correct html_path for rtd theme:
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'labgriddoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'labgrid.tex', 'labgrid Documentation',
     'Jan Luebbe, Rouven Czerwinski', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'labgrid', 'labgrid Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'labgrid', 'labgrid Documentation',
     author, 'labgrid', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for autodoc --------------------------------------------------

autodoc_member_order = 'bysource'
autodoc_default_options = {
        'special-members': True,
}
autodoc_mock_imports = ['onewire',
                        'txaio',
                        'autobahn',
                        'autobahn.asyncio',
                        'autobahn.asyncio.wamp',
                        'autobahn.wamp',
                        'autobahn.wamp.types',
                        'autobahn.twisted',
                        'autobahn.twisted.wamp',
                        'autobahn.wamp.exception',
                        'twisted.internet.defer',
                        'gi',
                        'gi.repository',]

# -- Options for autosection ----------------------------------------------
autosectionlabel_prefix_document = True


from unittest.mock import Mock
for mod in autodoc_mock_imports:
    sys.modules[mod] = Mock()

def run_apidoc(app):
    from sphinx.ext.apidoc import main
    module = os.path.abspath(os.path.join(app.srcdir, '..', 'labgrid'))
    output = os.path.abspath(os.path.join(app.srcdir, 'modules'))
    cmd = [module, '-a', '-M', '-H', 'Modules', '-o', output]
    main(cmd)

def setup(app):
    app.connect('builder-inited', run_apidoc)
    app.connect('doctree-read', write_literal_blocks)

# -- Options for doctest --------------------------------------------------

doctest_global_setup = '''
import os
import shutil
from unittest.mock import Mock, patch

doctest_dir = '.build/doctest'

if not os.getcwd().endswith(doctest_dir):
    os.chdir(doctest_dir)
'''

doctest_global_cleanup = '''
if os.getcwd().endswith(doctest_dir):
    os.chdir('../..')
'''

def write_literal_blocks(app, doctree):
    """
    Writes named literal blocks to a file with that respective name in the temporary doctest build
    directory. This allows doctest to test code snippets referring to these files as-is.
    """
    blocks = doctree.traverse(
        condition=lambda node: node.tagname == 'literal_block'
    )

    for block in blocks:
        name = '_'.join(block['names'])

        if not name:
            continue

        out_path = os.path.join(app.outdir, name)

        if os.path.exists(out_path):
            raise Exception(f'literal block name "{name}" used multiple times')

        with open(out_path, 'w') as f:
            f.write(block.astext())
