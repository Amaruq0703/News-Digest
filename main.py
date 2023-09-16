import requests
from sendemail import send_email

#Linked news API

topic = 'wsj'
api_key = 'ac649fd9a8574e96b577f4f572ca3a56'
url =f'https://newsapi.org/v2/everything?domains={topic}.com&apiKey=ac649fd9a8574e96b577f4f572ca3a56'

#API Request

request = requests.get(url)

#Accessed the content from API as dictionary

content = request.json()

totalmessage = ''

for article in content['articles'][0:20]:
    sourcelist = article['source']
    totalmessage =totalmessage + f'\nTitle: {article["title"]} \n Link: {article["url"]} \n Source: {sourcelist["name"]}\n'

totalmessage = 'Subject: Todays News' + totalmessage

    
totalmessage = totalmessage.encode('utf-8')

send_email(message=totalmessage)
