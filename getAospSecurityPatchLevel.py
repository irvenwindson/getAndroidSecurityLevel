import scrapy
import logging
class getAospSecurityPatchLevel(scrapy.Spider):
   name = 'getAospSecurityPatchLevel'
   start_urls = ['https://source.android.com/security/bulletin#bulletins']
   def parse(self, response):
      latestpatchlevel = response.css("table").xpath('//tr')[1].xpath('td/text()')[3].get()
      print( latestpatchlevel)


