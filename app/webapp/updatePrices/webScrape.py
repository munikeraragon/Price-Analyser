#import the library used to query a website
import urllib.request  #if you are using python3+ version, import urllib.request
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
import requests
from lxml.html import fromstring

from selectorlib import Extractor
import requests 
import json 
import argparse
from itertools import cycle
from .userAgentList import userAgentList

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

def bestBuy(URL):
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',}
        #url = "https://www.bestbuy.com/site/google-pixel-4-with-64gb-cell-phone-unlocked-just-black/6382490.p?skuId=6382490"
        #url = "https://www.bestbuy.com/site/microsoft-xbox-one-s-1tb-nba-2k20-bundle-white/6350265.p?skuId=6350265"
        url = URL
        # store page html
        htmlPage = requests.get(url, headers=headers)
        # store in beatiful soup format
        soup = BeautifulSoup(htmlPage.text, "html.parser")
        productPrice = soup.find("div", {"class":"priceView-hero-price priceView-customer-price"}).span.text
        print(productPrice)
        return productPrice
    except ValueError:
        return False
    


def amazon(URL):
    try:
        #get proxy ip
        proxies = get_proxies()
        proxy_pool = cycle(proxies)
        userAgent_pool = iter(userAgentList)
        # Create an Extractor by reading from the YAML file
        e = Extractor.from_yaml_file("C:/Users/santi/Desktop/CS320 project/Dajngo_webapp/app/webapp/updatePrices/selectors.yml") 
        #santiago path = C:\\Users\\santi\\Desktop\\CS320 project\\Dajngo_webapp\\app\\webapp\\userApp\\selectors.yml
        #Trever's path = /home/treverhibbs/Documents/projects/Price-Analyser/app/webapp/userApp/selectors.yml
        for i in range(1,4):
            #get proxy from pool
            try:
                proxy = next(proxy_pool)
            except Exception as e:
                #skip if no connect
                print(str(e))
                return False
            #get user agent from user agent pool
            user_agent = next(userAgent_pool)
            print(user_agent)
            print(proxy)
            print("Request #%d"%i)
            headers = {'http': proxy, 'https': proxy, 'User-Agent': user_agent}
            try:
                # Download the page using requests
                r = requests.get(URL, headers=headers)
                break
                # Pass the HTML of the page and create 
            except Exception as e:
                #skip if no connect
                print(str(e))

        data = e.extract(r.text)
        return(data["sale_price"])
    except ValueError:
        return False

def walmart(URL):
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',}
        #url = "https://www.bestbuy.com/site/google-pixel-4-with-64gb-cell-phone-unlocked-just-black/6382490.p?skuId=6382490"
        #url = "https://www.bestbuy.com/site/microsoft-xbox-one-s-1tb-nba-2k20-bundle-white/6350265.p?skuId=6350265"
        url = URL
        # store page html
        htmlPage = requests.get(url, headers=headers)
        # store in beatiful soup format
        soup = BeautifulSoup(htmlPage.text, "html.parser")
        priceContainer = soup.find("div", {"class":"prod-PriceHero"})
        price = priceContainer.find("span",{"class":"visuallyhidden"}).text
        return price
    except ValueError:
        print("fail")
        return False