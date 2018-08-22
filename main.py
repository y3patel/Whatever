from flask import Flask
from flask import request
app = Flask(__name__)

import bs4
import sys
from urllib.request import urlopen 
import urllib
from urllib.request import Request
from bs4 import BeautifulSoup as soup

@app.route('/')
def hello_world():
    return 'Hello,World'


if __name__ == '__main__':
  app.run()
