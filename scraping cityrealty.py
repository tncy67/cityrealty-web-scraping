from selenium import webdriver
import time
import re
import pandas as pd
import json
import urllib.request
from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup
from seleniumwire import webdriver


driver=webdriver.Chrome()
url="https://www.cityrealty.com/nyc/apartments-for-rent/search-results#?page=1"
driver.get(url)


index=0
while index <=0:
    try:
        print("Scraping Page number " + str(index))
        index = index + 1
        reviews = driver.find_elements_by_xpath('//div[@class="right_side info clearfix"]')
        for review in reviews:

            review_dict = {}
            try:
                address = review.find_element_by_xpath('.//span[@class="lst_name"]').text
            except:
                continue
            print('address = {}'.format(address))

            try:
                sub_boro = review.find_element_by_xpath('.//div[@class="infos ng-binding ng-scope"]').text
            except:
                continue
            print('sub_boro = {}'.format(sub_boro))

            try:
                rent_price = review.find_element_by_xpath('.//span[@class="price big ng-binding"]').text
            except:
                continue
            print('rent_price = {}'.format(rent_price))

            try:
                price_sqft = review.find_element_by_xpath('.//span[@class="price-ppsqft ng-binding ng-scope"]').text
            except:
                continue
            print('price_sqft = {}'.format(price_sqft))

            try:
                beds = review.find_element_by_xpath('.//span[@class="beds ng-binding"]').text
            except:
                continue
            print('beds = {}'.format(beds))

            try:
                baths = review.find_element_by_xpath('.//span[@class="baths ng-binding"]').text
            except:
                continue
            print('baths = {}'.format(baths))

            try:
                total_sqft = review.find_element_by_xpath('.//span[@class="square ng-binding"]').text
            except:
                continue
            print('total_sqft = {}'.format(total_sqft))

            try:
                list_date = review.find_element_by_xpath('.//span[@class="date ng-binding"]').text
            except:
                continue
            print('list_date = {}'.format(list_date))

            try:
                list_by = review.find_element_by_xpath('.//span[@class="listed_managed_data ng-binding"]').text
            except:
                continue
            print('list_by = {}'.format(list_by))



        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button = driver.find_element_by_xpath('//div[@class="see-more__cta see-more--blue see-more__cta-bottom kmx-typography--display-1"]')
        button.click()
        time.sleep(2)


    except Exception as e:
        print(e)
        #driver.close()
        break




# download json files

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
          }
x = range(1572150000000,1572160000000)
for n in x:
    try:
        reg_url = 'https://www.cityrealty.com/rpc/search/get-rental-listings?f%5B%5D=priceRangeRent&f%5B%5D=location&f%5B%5D=bedroomFullMulti&f%5B%5D=rentalBuildingTypeMulti&f%5B%5D=doorman&f%5B%5D=dateListed&f%5B%5D=priceChange&f%5B%5D=searchTermListings&f%5B%5D=subHoods&s%5B%5D=salePrice&s%5B%5D=dateListed&s%5B%5D=noFee&s%5B%5D=offerTag&s%5B%5D=ppsqft&s%5B%5D=neighborhood2&s%5B%5D=registration&type=json&uniqueid=1571933495144'
        response = requests.get(reg_url, headers=headers)
        writeFile =open(str(n)+'file_name.json', 'w')
        writeFile.write(response.text)
    except:
        pass
