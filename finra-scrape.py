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

pages = 20

def main():
    options = webdriver.ChromeOptions() 
    options.add_argument('--headless')

    with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as driver: 
        driver.get(url) 

        ## Get to search Bar, navigate to search
        search_parent = driver.find_element(By.XPATH, "//div[@class='flex-1 w-full min-w-0 h-10 sm:flex-none sm:mb-4']")
        search_bar = search_parent.find_element(By.XPATH, ".//input")
        search_bar.send_keys("Smith" + "\n")
        time.sleep(1)
        
        i = 0
        while i <= pages:
        ## Go through rows crawling spans for info
            parent_element = driver.find_element(By.XPATH, "//div[@class='flex w-full flex-row flex-wrap justify-around gap-3']")
            parent_cards = parent_element.find_elements(By.XPATH, "//div[@class='mb-2 card-dimensions flex-1 text-center ng-star-inserted']") 
            print(len(parent_cards))
            for card in parent_cards:
                text = card.find_element(By.XPATH, ".//div[@class='text-gray-85 text-left font-semibold mt-1 text-xs ng-star-inserted']//span[2]")
                print(text.text)
            next_button = driver.find_element(By.XPATH, "//div[@class='px-2 ng-star-inserted']//button")
            next_button.click()
            time.sleep(1)
            i+=1






if __name__ == '__main__':
    main()