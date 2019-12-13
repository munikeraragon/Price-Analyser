from django.test import TestCase
from userApp.webScrape import *

class userAppTestCase(TestCase):
    def test_amazon_web_scrape(self):
        """amazon webscrape function returns price of item"""
        #set up testurl
        testUrl = 'https://www.amazon.com/Fortnite-Squad-Mode-4-Figure-Pack/dp/B07PT1WC4M?ref_=Oct_DLandingS_D_10fcd403_60&smid=ATVPDKIKX0DER'
        self.assertIs(len(amazon(testUrl)), 1)

    def test_get_proxies(self):
        """test if get proxies returns list of ips"""
        proxyList = get_proxies()
        self.assertIs(len(proxyList), 1)


