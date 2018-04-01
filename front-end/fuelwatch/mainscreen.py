from __future__ import absolute_import, print_function, unicode_literals
from cavorite.HTML import *
from cavorite import t

def mainscreen_view():
    return div([
                 p("Fuel watch"),
                 p([t("Choose fuel type-")] + [
                   select([
                     option({'value': 1}, 'Unleaded Petrol'),
                     option({'value': 2}, 'Premium Unleaded'),
                     option({'value': 4}, 'Diesel'),
                     option({'value': 5}, 'LPG'),
                     option({'value': 6}, '98 RON'),
                     option({'value': 10}, 'E85'),
                     option({'value': 11},' Brand diesel'),
                   ]),
                   p(''),
                   html_button('Lookup'),
                 ]),
               ])
