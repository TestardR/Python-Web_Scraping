import requests
from bs4 import BeautifulSoup
from csv import writer
response = requests.get('https://romaintestard.netlify.com/work.html')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='item')

for post in posts:
    print(post)
