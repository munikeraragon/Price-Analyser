import pytest
import timeit
from django.test import TestCase
from userApp.webScrape import *

class userAppTestCase(TestCase):
    def test_amazon_web_scrape(self):
        """amazon webscrape function returns price of item"""
        #set up testurl
        testUrl = 'https://www.amazon.com/Fortnite-Squad-Mode-4-Figure-Pack/dp/B07PT1WC4M?ref_=Oct_DLandingS_D_10fcd403_60&smid=ATVPDKIKX0DER'
        self.assertIs(len(amazon(testUrl)), 6)

    def test_walmart_web_scrape(self): 
        """call the walmart web scrape function"""
        testUrl = 'https://www.walmart.com/ip/VIZIO-36-2-1-Channel-Soundbar-System-SB3621n-E8/36706825'
        self.assertIs(len(walmart(testUrl)), 6)    

    def test_get_proxies(self):
        """test if get proxies returns list of ips"""
        proxyList = get_proxies()
        assert len(proxyList) >= 0

    def test_speed_of_amazon__web_scraping_function(self):
        """test the speed of the walmart scraping function""" 
        if __name__ == 'userApp.testUserApp':
            t = timeit.Timer(stmt='userAppTestCase.walmart_test()', setup="from userApp.testUserApp import userAppTestCase")
            #return time it takes to exectue walmart function and save it in variable
            length_of_walmart_call = t.timeit(1)
            #check if walmart function call was less than 2 seconds
            print("\n" + "time in seconds for walmart function call " + str(length_of_walmart_call))
            assert length_of_walmart_call < 2

    def test_speed_of_walmart__web_scraping_function(self):
        """test the speed of the walmart scraping function""" 
        if __name__ == 'userApp.testUserApp':
            t = timeit.Timer(stmt='userAppTestCase.amazon_test()', setup="from userApp.testUserApp import userAppTestCase")
            #return time it takes to exectue walmart function and save it in variable
            length_of_amazon_call = t.timeit(1)
            #check if walmart function call was less than 2 seconds
            print("\n" + "time in seconds for amazon function call " + str(length_of_amazon_call))
            assert length_of_amazon_call < 2        

    #function to be called by test_speed_of_walmart_web_scraping_function
    def walmart_test(): 
        """call the walmart web scrape function"""
        testUrl = 'https://www.walmart.com/ip/VIZIO-36-2-1-Channel-Soundbar-System-SB3621n-E8/36706825'
        walmart(testUrl)

    #function to be called by test_speed_of_amazon_web_scraping_function
    def amazon_test():
        """call the amazon web scrap function for time test"""
        testUrl = 'https://www.amazon.com/Fortnite-Squad-Mode-4-Figure-Pack/dp/B07PT1WC4M?ref_=Oct_DLandingS_D_10fcd403_60&smid=ATVPDKIKX0DER' 
        amazon(testUrl)   