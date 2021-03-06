
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class Scraper:

    def __init__(self, webdriverpath):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.headless = True
        self.driver = webdriver.Chrome(webdriverpath, chrome_options=options)
        self.driver.set_window_size(1120,550)
        self.skip_ads = True
        self.skip_commercial_sellers = True
        self.skip_bidding = True
        self.skip_reserved = True

    def Scrape(self, url): # Scrapes a url through Selenium, uses a pattern to find listing details, and returns them.
        driver = self.driver
        driver.get(url)
        listings = {}
        original_count = len(driver.find_elements_by_class_name("mp-Listing--list-item"))
        
        for element in driver.find_elements_by_class_name("mp-Listing--list-item"):
            if ("mp-Listing--cas" in element.get_attribute('class')) and self.skip_ads:
                continue
            listing = {}
            listing['title'] = element.find_element_by_css_selector('h3.mp-Listing-title').text
            listing['description'] = element.find_element_by_css_selector('p.mp-Listing-description').text
            url = element.find_element_by_class_name("mp-Listing-coverLink").get_attribute("href")
            listing['price'] = element.find_element_by_class_name('mp-text-price-label').text
            listing['url'] = url
            listing['date'] = element.find_element_by_class_name("mp-Listing-date").text
            listing['seller_name'] = element.find_element_by_class_name("mp-Listing-seller-name").text
            try:
                listing['seller_website'] = element.find_element_by_class_name("mp-Listing-sellerCoverLink").get_attribute('href')
       
            except NoSuchElementException:
                listing['seller_website'] = False
            
            
            if self.skip_commercial_sellers and listing['seller_website'] != False:
                continue
            if self.skip_reserved and "Gereserveerd" in listing['price']:
                continue
            if self.skip_bidding and "Bieden" in listing['price']: 
                continue
                
            
            listings[url] = listing
           
                  
        
        return listings, original_count-len(listings)

    def SaveListings(self, listings, filename): # Saves listings to a file.
        with open(filename, "r") as json_file:
            listings_in_file = json.load(json_file)
            listings_in_file.update(listings)
            # Clear json file
            json_file.close()
            open(filename,"w").close()
        with open(filename, "w") as json_file:
            json.dump(listings_in_file, json_file)
            json_file.close()


    def CompareListingsToSavedListings(self, listings, filename): # This function finds "new listings" (those that have not been found before)
        with open(filename, 'r') as json_file:
            new_listings = {}
            saved_listings = json.load(json_file)
            json_file.close()
            for listing in listings:
                is_new = True
                for saved_listing in saved_listings:
                    if listing == saved_listing:
                        is_new = False
                if is_new:
                    new_listings[listing] = listings[listing]
            return new_listings
