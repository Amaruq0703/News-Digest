import requests

#Linked news API

api_key = 'ac649fd9a8574e96b577f4f572ca3a56'
url ='https://newsapi.org/v2/everything?domains=wsj.com&apiKey=ac649fd9a8574e96b577f4f572ca3a56'

#API Request

request = requests.get(url)

#Accessed the content from API as dictionary

content = request.json
