project = 'Shot Manager'
author = 'Pablo Tochez'

master_doc = 'index'

extensions = ['sphinx.ext.autosectionlabel',
              'sphinx.ext.autodoc',
              'sphinx.ext.autosummary']

language = "en"

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

html_theme_options = {
    "sidebar_hide_name": True,
}

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#7C4DFF",
        "color-brand-content": "#7C4DFF",
    },
}