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
    
    filePointer = open('proxies.txt', 'w')

    print(str(proxies), file = filePointer)
    filePointer.close()

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
    

'''def amazon(URL):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',}
    #url = "https://www.bestbuy.com/site/google-pixel-4-with-64gb-cell-phone-unlocked-just-black/6382490.p?skuId=6382490"
    #url = "https://www.bestbuy.com/site/microsoft-xbox-one-s-1tb-nba-2k20-bundle-white/6350265.p?skuId=6350265"
    url = URL
    # store page html
    htmlPage = requests.get(url, headers=headers)
    # store in beatiful soup format
    soup = BeautifulSoup(htmlPage.text, "html.parser")
    print(soup)
    productPrice = soup.find("div", {"class":"a-section a-spacing-small"})
    print(productPrice)
'''
def amazon(URL):
    try:
        # Create an Extractor by reading from the YAML file
        e = Extractor.from_yaml_file('/home/treverhibbs/Documents/projects/Price-Analyser/app/webapp/userApp/selectors.yml')

        user_agent = 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
        headers = {'User-Agent': user_agent}

        # Download the page using requests
        
        r = requests.get(URL, headers=headers)
        # Pass the HTML of the page and create 
        data = e.extract(r.text)

        #print the data to a file
        filePointer = open('AmazonWebPage.txt', 'w')
        print(r.text, file = filePointer)
        filePointer.close()

        # Print the data 
        #print(json.dumps(data, indent=True))
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
        return False