import time

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 

html_parser = 'html.parser'
user_agent = 'User-Agent'
mozilla_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

url = 'https://brokercheck.finra.org/'

def main():
    options = webdriver.ChromeOptions() 
    options.add_argument('--headless')

    with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as driver: 
        driver.get(url) 

        ## Get to search Bar, navigate to search
        search_parent = driver.find_element(By.XPATH, "//div[@class='flex-1 w-full min-w-0 h-10 sm:flex-none sm:mb-4']")
        search_bar = search_parent.find_element(By.XPATH, ".//input")
        search_bar.send_keys("Smith" + "\n")
        time.sleep(2)
        
        ## Go through rows crawling spans for info
        parent_card_elements = driver.find_elements(By.XPATH, "//div[@class='flex flex-col border-t-4 px-4 py-2 h-60 border-gray-70 bg-gray-20']") 
        for element in parent_card_elements:
            text = element.find_element(By.XPATH, "//div[@class='text-gray-85 text-left font-semibold mt-1 text-xs ng-star-inserted']//span[2]")
            print (text.text)





if __name__ == '__main__':
    main()