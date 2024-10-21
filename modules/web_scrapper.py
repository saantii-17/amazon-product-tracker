from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class web_scrapper:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.driver = webdriver.Chrome()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
    
    def get_price(self, url):
        self.driver.get(url)
        sleep(1)
        
        try:
            # price_element = self.driver.find_element(By.CLASS_NAME, 'aok-offscreen')
            price_element = self.driver.find_element(By.CSS_SELECTOR, 'h1 a')
            price = price_element.text
            price = price.replace(' ', '').replace('€', '').replace(',', '.').replace(' ', '')
            
            # return float(price)
            return price
        
        except NoSuchElementException:
            print(f"No se pudo encontrar el precio en la página: {url}")
            return None
        except Exception as e:
            print(f"Error inesperado al obtener el precio: {e}")
            return None
    
    def destruct_driver(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    scrapper = web_scrapper()
    price = scrapper.get_price('https://quotes.toscrape.com/')
    print(price)
    scrapper.destruct_driver()