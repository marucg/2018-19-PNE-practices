
import http.client
import json

capital = input('Please introduce a city: ')
HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/search/?query="+capital
METHOD = "GET"

headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)
r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()
place = json.loads(text_json)

if len(place) == 0:
    print('We do not have information for that city')
else:
    LOCATION_WOEID = place[0]['woeid']
    LOCATION_WOEID = str(LOCATION_WOEID)

    HOSTNAME = "www.metaweather.com"
    ENDPOINT = "/api/location/"
    METHOD = "GET"
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection(HOSTNAME)
    conn.request(METHOD, ENDPOINT + LOCATION_WOEID + '/', None, headers)
    r1 = conn.getresponse()
    text_json = r1.read().decode("utf-8")
    conn.close()
    weather = json.loads(text_json)
    print(weather)
    time = weather['time']
    temp0 = weather['consolidated_weather'][0]
    temp = temp0['the_temp']
    place = weather['title']
    sunset = weather['sun_set']
    print()
    print("Place:", place)
    print("Current time:", time)
    print("Current temp:", temp, 'degrees')
    print('Sunset in the city', sunset)
