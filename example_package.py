# On terminal (change at bottom of screen) typed pip install requests and this appeared on the Pycharm interpreter
import requests
# URL of website
url = 'https://www.bbc.co.uk/news'
# get url and print the status code - whether it is working or not (200 is working, 404 is no content found)
response = requests.get(url)
print(response.status_code)
print(response.content)
print(response)