from flask import Flask
app = Flask(__name__)

import bs4
import sys
from urllib.request import urlopen 
import urllib
from urllib.request import Request
from bs4 import BeautifulSoup as soup



@app.route('/')
def hello_world():
    name = "naina"
    print(name)
    name = urllib.parse.quote_plus(name)
    my_url = 'https://www.musixmatch.com/search/'+name+'#'

    print(my_url)

    req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
    page_html = urlopen(req).read()
    page_soup = soup(page_html,"html.parser")

    containers = page_soup.findAll("h2",{"class":"media-card-title"})
    songs = containers[0].findAll("a",{"class":"title"})

    print(songs[0])

    links = songs[0].get('href')
    link = "https://www.musixmatch.com"+links

    print(link)

    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    page_html = urlopen(req).read()
    page_soup = soup(page_html,"html.parser")

    containers = page_soup.findAll("p",{"class":"mxm-lyrics__content "})
    for container in containers:
        lyric = container.text
        print(lyric)
    lyric = lyric.replace('\n','<br>');
    return lyric


if __name__ == '__main__':
  app.run()
