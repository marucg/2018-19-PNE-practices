#The number of total jokes about Chuck Norris avaiable at the database
#The number and names of the different categories
#A random joke :-)

import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = "/categories"
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
#print("Response received: ", end='')
#print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
jokes = json.loads(text_json)

# -- Print the received URL

names = jokes["value"]
print('Name of the different categories', names)
