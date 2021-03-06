from selenium import webdriver
from selenium.webdriver.common.keys import Keys # in order to be able to hit keys like enter and esc, etc.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time  # to add timers
import os # to set chromedriver relative path



# School Class ******************************************************************
# object constructor for each school, contains methods to save and clean it's info
class School:
    def print_school(self):
        print(f'School Location: {self.location}, School Name: {self.name}, Curriculum: {self.curriculum}, Language: {self.language}, Ages: {self.ages}, Fees: {self.fees}')

    # set school location, it's in it's own method because all schools in the same search reult page will have the same location
    def set_school_location(self, loc):
        self.location = loc

    # set school info, and return 0 if the information is not complete, else return 1
    def set_school_properties(self, cell):
        # properties = [curriculum, language, ages, fees]
        properties = cell.find_elements_by_css_selector("dt")
        # check that all info is available
        if len(properties) < 4:
            return 0
        try:
            self.name = cell.find_element_by_class_name("school-name").text
            self.curriculum = properties[0].text
            self.language = properties[1].text
            self.ages = properties[2].text
            self.fees = properties[3].text
            return 1
        except:
            return 0

    def clean_school(self):
        try:
            self.clean_fees()
            if (self.is_highSchool() != 1):
                return 0
            return 1
        except:
            return 0
        
    def clean_fees(self):
        fee = self.fees
        fee = fee.replace("from: ", "del")
        fee = fee.replace("to: ", "del")
        fee = fee.replace("\n", "del")
        fee = fee.split("del") # fee = ['', 'feeMin', '', 'feeMax']
        fee = fee[1] + " - " + fee[3]
        self.fees = fee
    
    def is_highSchool(self):
        if ("18" in self.ages):
            return 1
        else:
            return 0




# scraping class ******************************************************************
# Contains methods to scrape through webpages
class Scraper_ISD:
      # initialize webdriver
    def __init__(self):
        PATH = os.path.abspath("chromedriver") #access chromedriver path in this directory
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://www.international-schools-database.com/")
        self.allSchools = list()
    
     # quit webdriver
    def quitDriver(self):
        self.driver.quit()

    def print_AllSchools(self):
        for sch in self.allSchools:
            sch.print_school()
    
    def scrapePage(self, locationString):
        try:
            self.driver.get(f"https://www.international-schools-database.com/in/{locationString}?filter=on")
            # time.sleep(1)
            # find location of page
            thisLocation = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'span.text-secondary'))
            )
            thisLocation = thisLocation.text
            time.sleep(2)
            # navigate to the section where all the indivdual cells are located
            mainList = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'cards-row'))
            )
            # save all the individual cells that contain schools info into an array
            cells = mainList.find_elements_by_class_name("card-row-inner")
            # loop through all the advisors, set the required information, and append them to the advisors' list
            for cell in cells:
                school = School()
                school.set_school_location(thisLocation)
                if (school.set_school_properties(cell) == 1):
                    if (school.clean_school() == 1):
                        self.allSchools.append(school)
            print(f"Page for {thisLocation} scrape succeeded.")
            return 1
        except:
            print(f"Page for {thisLocation} scrape failed.")
            return 0

    # def find_location_links:


    # scrape all the search result pages
    def scrapeSource(self):

        # retrieve all location links in the menu
        menu = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/form/div[2]"))
        )

        # fetch the strings that represent each location
        locationLinks = menu.find_elements_by_css_selector("option")
        locationStrings = list()
        for l in locationLinks:
            lString = l.get_attribute("value")
            locationStrings.append(lString)
        
        # use the location string to access the corresponding urls
        for l in locationStrings:
            if (l != ""):
                self.scrapePage(l)
       
        print("All the source's pages have been scraped.")
