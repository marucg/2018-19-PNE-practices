#The number of total jokes about Chuck Norris avaiable at the database
#The number and names of the different categories
#A random joke :-)

import http.client
import json

# ---- RANDOM JOKE ----
HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes/random"
METHOD = "GET"

headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)
r1 = conn.getresponse()
print()
text_json = r1.read().decode("utf-8")
conn.close()
jokes = json.loads(text_json)
random_joke = jokes["value"]['joke']
print('A random joke:', random_joke)

# ---- NUMBER OF CATEGORIES ----
HOSTNAME = "api.icndb.com"
ENDPOINT = "/categories"
METHOD = "GET"

headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)
r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()
categories = json.loads(text_json)
number_c = categories['value']
print('The number of the different categories is', len(number_c))
print('The names of the different categories are', number_c[0], 'and', number_c[1])

# ----NUMBER OF JOKES----
HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes/count"
METHOD = "GET"

headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)
r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()
number = json.loads(text_json)
total_number = number['value']
print('The number of total jokes about Chuck Norris is', total_number)
