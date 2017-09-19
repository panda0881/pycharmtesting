from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random

spider = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

test_url = 'http://www.dce.com.cn/dalianshangpin/xqsj/tjsj26/rtj/rxq/index.html'
target_url = "http://www.dce.com.cn/publicweb/quotesdata/dayQuotesCh.html"
spider.get(target_url)
calender = spider.find_elements_by_xpath("//div[@id='calender']/table/tbody/tr")
found = 0
for week in calender:
    if found == 0:
        if week.get_attribute('class') == 'week':
            days = week.find_elements_by_tag_name('td')
            for day in days:
                if day.text == '15':
                    day.click()
                    found = 1
                    break
    else:
        break

options = spider.find_elements_by_xpath("//div[@class='selBox noBorder']/div/ul/li")
for option in options:
    if option.text == "期权":
        option.click()

print('end')


