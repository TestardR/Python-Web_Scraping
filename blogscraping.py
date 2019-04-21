import requests
from bs4 import BeautifulSoup
from csv import writer
response = requests.get('https://romaintestard.netlify.com/work.html')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='item')

with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Link', 'Date']
    csv_writer.writerow(headers)

    for post in posts:
        title = post.find(id="description_title").get_text()
        technologies = post.find(
            id="description_title").find_next_sibling().get_text().replace('\n', '').replace('             ', '').replace('            ', ' ')
        link = post.select('a')[1]['href']
        csv_writer.writerow([title, technologies, link])
