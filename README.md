# JSONDataFormatting
Python program to format JSON data from Weather API URL

1.	Write a console application to return a JSON string with weather and airport information for US cities (assume 10 for this exercise). The response should contain the following data:

-	Count: No of cities
-	List of cities with details
o	Id 
o	Name
o	Weather details
	Longitude
	Latitude
	Min Temp
	Max Temp
	Primary condition*
	Wind speed
o	Airport
	Primary airport **
	Secondary airports

You can hard code the Airport data or save it a file and read it into your program
Notes

1) *There could be multiple weather conditions reported for a city. Use the first as the primary weather condition
2) **The id is same as the id in Weather API response. The nearest airports can be retrieved from the code field. The code field can contain multiple airports delimited by ~. The first airport is always the primary airport and all others are secondary airports. 

Airport Information: 
Use the following JSON string (this can be hard coded):
{"AirportList":[{"id":4887398,"city":"Chicago","code":"ORD~MDW"},{"id":4684888,"city":"Dallas","code":"DAL"},{"id":5809844,"city":"Seattle","code":"SEA"},{"id":5419384,"city":"Denver","code":"DEN"},{"id":5128581,"city":"New York","code":"JFK~LGA~EWR"},{"id":5780993,"city":"Salt Lake City","code":"SLC"},{"id":5506956,"city":"Las Vegas","code":"LAS"},{"id":5391959,"city":"San Francisco","code":"SFO~SJC~OAK"},{"id":4930956,"city":"Boston","code":"BOS"},{"id":4180439,"city":"Atlanta","code":"ATL"}]}



