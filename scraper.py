from selenium import webdriver
# in order to be able to hit keys like enter and esc, etc.
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # to add timers
import os # to set chromedriver relative path

# source1 - object constructor for school advisors

class Advisor:
    def setAdv(self, name, title, location, email):
        self.name = name
        self.title = title
        self.location = location
        self.email = email

    def printAdv(self):
        print(f'Name: {self.name}, Title: {self.title}, Location: {self.location}, Email: {self.email}')


class Scraper:
    def __init__(self):
        PATH = os.path.abspath("chromedriver") #access chromedriver path in this directory
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://www.nesacenter.org/membership-directory/contacts")
    
    def quitDriver(self):
        self.driver.quit()


    def scrapePage(self, pageNumber):

        try:
            # retreive the link to the sepcific page number
            link = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, f"//a[contains(@href,'?const_page={pageNumber}&')]"))
            )
            link.click()
            time.sleep(3)

            # navigate to the section where all the indivdual cells are located
            mainList = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="fsEl_2214"]/div'))
            )
            # save all the individual cells that contain advisor info into an array
            cells = mainList.find_elements_by_class_name("fsConstituentItem")
            # for testing purposes...
            print(cells)
            
            # loop through all the items, and access the required information
            for cell in cells:
                name=cell.find_element_by_class_name("fsFullName").text
                try:
                    title=cell.find_element_by_class_name("fsTitles").text
                except:
                    title="n/a"
                try:
                    location=cell.find_element_by_class_name("fsLocations").text
                except:
                    location="n/a"
                try:
                    email=cell.find_element_by_class_name("fsEmail").text
                except:
                    email="n/a"

                advisor=Advisor()
                advisor.setAdv(name, title, location, email)
                advisor.printAdv
                print(f'Name: {name}, Title: {title}, Location: {location}, Email: {email}')
            print(f"Page {pageNumber} scrape succeeded.")
            return 1
        except:
            print(f"Page {pageNumber} scrape failed.")
            return 0


    def scrapeSource(self):
        pageNumber = 1
        while ( self.scrapePage(pageNumber) == 1):
            pageNumber = pageNumber + 1
        
        print("All the source's pages have been scraped.")


# Main function calls ***************************
scraper = Scraper()
# scraper.scrapeSource()
scraper.scrapePage(2)
scraper.quitDriver()