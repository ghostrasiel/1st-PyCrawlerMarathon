#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scrapy
import re
import bs4
from urllib.parse import urljoin
from pprint import pprint
import requests

class pttSpider(scrapy.Spider):
    name='ptt'
    start_urls=['https://www.ptt.cc/bbs/Boy-Girl/M.1578074538.A.7FB.html']
    allowed_domains = ['www.ptt.cc']
    cookies = {'over18': '1'}
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies=self.cookies)

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text , 'html.parser')
        a = soup.find('span',class_='article-meta-value').string
        date={
            'titile':a,
            'url':response.url
        }
        yield date


# In[ ]:




