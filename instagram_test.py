import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import json
import urllib

def link_type(url):
    url_pieces = url.split('/')
    if len(url_pieces)>=5:
        if url_pieces[3]=="p":
            return "media"
    return None

def get_username(browser, item_id):
    print "Getting username..."
    url = "https://www.instagram.com/p/"+item_id
    browser.get(url)
    source = BeautifulSoup(browser.page_source, 'lxml')
    return source.find_all('a')[1]['title']

def get_item_id(url):
    "Getting item id..."
    url_pieces = url.split('/')
    item_id = url_pieces[4]
    return item_id

def get_media(username, item_id):
    print "attempting to grab media.."
    url = 'http://instagram.com/' + username + '/media'
    try:
        media = json.loads(requests.get(url).text)
    except requests.exceptions.RequestException as e:
        return None, None
    items = media['items']
    for item in items:
        if item['code']==item_id:
            try:
                 videos = item['videos']
                 media_type = 'video'
                 return media_type, videos['standard_resolution']['url']
            except KeyError:
                images = item['images']
                media_type = 'photo'
                return media_type, images['standard_resolution']['url']

def parse_instagram_url(url):
    print "Got instagram URL.. parsing now.."
    item = get_item_id(url)
    print "Opening selenium and grabbing username..."
    browser = webdriver.PhantomJS("/Applications/phantomjs")
    username = get_username(browser, item)
    media_type, url = get_media(username, item)
    browser.quit()
    return media_type, url

def download_media(media_type, url):
    if media_type:
        opener = urllib.FancyURLopener()
        path = './temp_vids/' + url.split('/')[-1]
        opener.retrieve(url, path)
        return path
    return None
#url = 'https://www.instagram.com/p/BDCSEZHjvMS/?taken-by=taylorswift'
#media_type, url =  parse_instagram_url(url)
#print download_media(media_type, url)
