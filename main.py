import requests
from sendemail import send_email

#Linked news API

api_key = 'ac649fd9a8574e96b577f4f572ca3a56'
url ='https://newsapi.org/v2/everything?domains=wsj.com&apiKey=ac649fd9a8574e96b577f4f572ca3a56'

#API Request

request = requests.get(url)

#Accessed the content from API as dictionary

content = request.json()

totalmessage = ''

for article in content['articles']:
    sourcelist = article['source']
    totalmessage = totalmessage + f'\nTitle: {article["title"]} \n Link: {article["url"]} \n Source: {sourcelist["name"]}\n'


    
totalmessage = totalmessage.encode('utf-8')

send_email(message=totalmessage)
