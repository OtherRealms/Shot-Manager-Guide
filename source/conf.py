project = 'Shot Manager'
author = 'Pablo Tochez'

master_doc = 'index'

extensions = ['sphinx.ext.autosectionlabel',
              'sphinx.ext.autodoc',
              'sphinx.ext.autosummary']

html_theme = 'furo'

html_logo = "logo_350.png"


html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/navigation.html",
        "sidebar/scroll-end.html",
    ]
}