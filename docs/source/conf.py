# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'IEA-ETSAP MARKAL/TIMES References'
copyright = '2023, ESMIA'
author = 'ESMIA'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.bibtex',
]

bibtex_bibfiles = ['ETSAP_TIMES References_2023-09-22.bib']
bibtex_default_style = 'plain'
bibtex_reference_style ='author_year'
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
