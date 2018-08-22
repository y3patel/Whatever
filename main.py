from flask import Flask
from flask import request
app = Flask(__name__)


import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from firebase import firebase
import json
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import smtplib
import time
from PyPDF2 import PdfFileMerger

@app.route('/')
def hello_world():
    scrapeother('http://www.sscias.com/p/indian-express-epaper.html','tie')	
    return 'Hello,World'

def scrapeother(main_url,code):
    req = Request(main_url,headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
    page_html = urlopen(req).read()
    page_soup = soup(page_html,'html.parser')
    containersbtn = page_soup.find('button',{'class':'button_next'})
    lnk = containersbtn.parent.get('href')
    print(lnk)
    req = Request(lnk,headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
    page_html = urlopen(req).read()
    page_soup = soup(page_html,'html.parser')
    container = page_soup.find('div',{'class':'bars'})
    dlnk = container.a.get('href')
    response = urlopen(dlnk)
    fl = open(code+'.pdf','wb')
    fl.write(response.read())
    fl.close()


if __name__ == '__main__':
  app.run()
