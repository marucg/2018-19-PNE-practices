import http.client
import json


PORT = 80
METHOD = 'GET'
ENDPOINT = '/info/species?content-type=application/json'
HOSTNAME = 'rest.ensembl.org'


headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)
r1 = conn.getresponse()
print()
data = r1.read().decode("utf-8")
conn.close()

# ----------------------------------
def species():
    information = json.loads(data)
    species_info = information['species']
    for element in species_info:
        name = element['display_name']
        print(name)

name_sp = species()

