import json
from urllib.request import urlopen
weatherInfo = urlopen('http://api.openweathermap.org/data/2.5/group?id=4887398,4684888,5809844,5419384,5128581,5780993,5506956,5391959,4930956,4180439&appid=30b3db4152f8ddd4bd894e9ea5be2246&units=imperial')
weatherInfoJson = weatherInfo.read()
data = json.loads(weatherInfoJson)

airportData = {"AirportList":[{"id":4887398,"city":"Chicago","code":"ORD~MDW"},{"id":4684888,"city":"Dallas","code":"DAL"},{"id":5809844,"city":"Seattle","code":"SEA"},{"id":5419384,"city":"Denver","code":"DEN"},{"id":5128581,"city":"New York","code":"JFK~LGA~EWR"},{"id":5780993,"city":"Salt Lake City","code":"SLC"},{"id":5506956,"city":"Las Vegas","code":"LAS"},{"id":5391959,"city":"San Francisco","code":"SFO~SJC~OAK"},{"id":4930956,"city":"Boston","code":"BOS"},{"id":4180439,"city":"Atlanta","code":"ATL"}]}

output = {}
output['cnt'] = data['cnt']
inner = {}
innerList = []


for j in range(10):
    inner = {}
    i = data['list'][j]
    inner['id'] = i['id']
    inner['name'] = i['name']
    WeatherDetails = {}
    WeatherDetails['lon'] = i['coord']['lon']
    WeatherDetails['lat'] = i['coord']['lat']
    WeatherDetails['temp_min'] = i['main']['temp_min']
    WeatherDetails['temp_max'] = i['main']['temp_max']
    WeatherDetails['primaryCondition'] = i['weather'][0]['main']
    WeatherDetails['speed'] = i['wind']['speed']
    inner['WeatherDetails'] = WeatherDetails
    airport = {}
    airportString = airportData['AirportList'][j]['code'].split('~')
    airport['primaryAirport'] = airportString[0]
    secondaryAirports = []
    for k in range(1, len(airportString)):
        secondaryAirports.append(airportString[k])
    airport['secondaryAirports'] = secondaryAirports
    inner['Airport'] = airport
    innerList.append(inner)
output['list'] = innerList
json_data = json.dumps(output)
print(json_data)
