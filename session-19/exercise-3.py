import http.client
import json

username = input('Please enter a github username: ')

HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
METHOD = "GET"
headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT + username, None, headers)
r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()
user = json.loads(text_json)
login = user['login']
name = user['name']
print()
print("User: ", login)
print("Name: ", name)

# ----LIST OF REPOS----
HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
METHOD = "GET"
headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT + username + "/repos", None, headers)
r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()
user = json.loads(text_json)
print('Name of repos: ', user[0]['name'])

# ----NUMBER OF COMMITS----
HOSTNAME = "api.github.com"
ENDPOINT = "/repos/" + username + "/2018-2019-practices/commits"
METHOD = "GET"
headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)
r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()
user = json.loads(text_json)
print('The number of commits is: ', len(user))



