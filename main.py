import json
from turtle import pd

import pandas
import requests

"""response = requests.get("https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=ilevia-parcbus&q=&facet=typevehicule&facet=modele&facet=marque&facet=decorationspecifiquevehicule")
print(response.status_code)"""
"""response = requests.get("http://api.zippopotam.us/us/90210")"""
"""response = requests.get(
    "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=ilevia-parcbus&q=&facet=typevehicule&facet=modele&facet=marque&facet=decorationspecifiquevehicule")
"""
"""response = requests.get(
    " https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=objets-trouves-dans-les-gares-en-temps-reel&q=&facet=date&facet=gc_obo_gare_origine_r_name&facet=gc_obo_type_c")
"""
"""response.json"""


response = requests.get(
    "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=disponibilite-parkings&q=&facet=libelle&facet=ville&facet=etat")

def jprint(obj):
    # create a formatted string of the Python JSON object
    response = json.dumps(obj, sort_keys=True, indent=4)
    print(response)
jprint(response.json())



