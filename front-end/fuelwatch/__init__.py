from __future__ import absolute_import, unicode_literals, print_function
try:
    import js
except ImportError:
    js = None
from cavorite import c, t, Router, callbacks, timeouts, ajaxget
from .mainscreen import mainscreen_view

def start():
    callbacks.initialise_global_callbacks()
    timeouts.initialise_timeout_callbacks()
    ajaxget.initialise_ajaxget_callbacks()
    body = js.globals.document.body

    error_404_page = c("div", [c("p", "No match 404 error"),
                               c("p", [c("a", {"href": "/#!"}, "Back to main page")])])


    r = Router({r'^$':  mainscreen_view(),
                },
                error_404_page, body)
    r.route()

