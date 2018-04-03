from __future__ import absolute_import, print_function, unicode_literals
from cavorite.HTML import *
from cavorite import t
from .historygraphfrontend import initialise_document_collection, download_document_collection, documentcollection
from historygraph import fields, Document, DocumentObject
from cavorite.ajaxget import ajaxget


class PetrolStation(DocumentObject):
    address = fields.CharRegister()
    price = fields.FloatRegister()

class FuelLookup(Document):
    status = fields.IntRegister() # 0 = Initialised, 1 = Server to process, 2 = client result available
    lat = fields.FloatRegister()
    lng = fields.FloatRegister()

    petrol_stations = fields.Collection(PetrolStation)

class MainScreenView(div):
    def __init__(self, *args, **kwargs):
        super(MainScreenView, self).__init__(*args, **kwargs)

    def lookup_onclick(self, e):
        print('lookup_onclick called')

    def was_mounted(self):
        super(MainScreenView, self).was_mounted()
        if documentcollection is None:
            ajaxget('/api/historygraph/dcid/', self.projects_api_dcid_result_handler)

    def projects_api_dcid_result_handler(self, xmlhttp, response):
        if xmlhttp.status >= 200 and xmlhttp.status <= 299:
            dcid = xmlhttp.responseText

            initialise_document_collection(dcid, self.on_historygraph_download_complete)
    
    def on_historygraph_download_complete(self):
        print('on_historygraph_download_complete called')

    def get_children(self):
        return [
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
                   html_button({'onclick': self.lookup_onclick}, 'Lookup'),
                 ]),
               ]

def mainscreen_view():
    return MainScreenView()
