from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 

html_parser = 'html.parser'
user_agent = 'User-Agent'
mozilla_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

url = 'https://scrapeme.live/shop/'

def main():
    req = Request('https://www.geeksforgeeks.org/extract-title-from-a-webpage-using-python/')
    req.add_header(user_agent, mozilla_agent)
    soup = BeautifulSoup(urlopen(req).read(), html_parser)
    print(soup.title)

    options = webdriver.ChromeOptions() 
    options.add_argument('--headless')

    with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as driver: 
        driver.get(url) 
        #driver.get_screenshot_as_file("capture.png")
        soup = BeautifulSoup(urlopen(driver.current_url), html_parser)
        print(soup.title)

        pokemon_data = []
        parent_elements = driver.find_elements(By.XPATH, "//a[@class='woocommerce-LoopProduct-link woocommerce-loop-product__link']") 
        for parent_element in parent_elements: 
            pokemon_name = parent_element.find_element(By.XPATH, ".//h2")
            pokemon_link = parent_element.get_attribute("href")
            price = parent_element.find_element(By.XPATH, ".//span")
            temp_poke_data = {
                "name": pokemon_name.text,
                "link": pokemon_link,
                "price": price.text
            }
            pokemon_data.append(temp_poke_data)
            print(temp_poke_data)


if __name__ == '__main__':
    main()