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

    def printAdv(self):
        print(f'Name: {self.name}, Title: {self.title}, Location: {self.location}, Email: {self.email}')

    #set advisor info, and return 0 if the information is not complete, else return 1
    def setAdv(self, cell):
        try:
            self.name = cell.find_element_by_class_name("fsFullName").text
        except:
            return 0
        
        try:
            self.title = cell.find_element_by_class_name("fsTitles").text
        except:
            return 0

        try:
            self.location = cell.find_element_by_class_name("fsLocations").text
        except:
            return 0

        try:
            self.email = cell.find_element_by_class_name("fsEmail").text
        except:
            return 0

        return 1
    
    #clean the advisor information, return 0 if any error occurs while cleaning, that will likely mean that the info is missing
    def cleanAdv(self):
        try:
            self.removeAdvAttr()
            # exclude NON high schools and affilated organization
            if (self.isHighSchool() != 1 or self.isOrganization() == 1):
                return 0
            self.cleanLocation()
            return 1
        except:
            return 0

    # remove the attribute that comes with the strings i.e. "Titles:", "Location:" 
    def removeAdvAttr(self):
        self.title = self.title.split("Titles: ")[1]
        self.location = self.location.split("Locations: ")[1]
        self.email = self.email.split("Email: ")[1]

    # clean the location by removing the description of the location i.e. remove "Affiliate School" or "Member"
    def cleanLocation(self):
        loc = self.location
        descFound = 0 #if the location description exists in the location

        if ("Member" in loc):
            loc = loc.replace("Member", "")
            descFound = 1
        elif ("Affiliate School" in loc):
            loc = loc.replace("Affiliate School", "")
            descFound = 1

        if (descFound == 1):
            if (loc[0] == ","):
                try:
                    loc = loc[2:]
                except:
                    print("unable to remove ,")
            else:
                try:
                    loc = loc[:-2]
                except:
                    print("unable to remove ,")
            self.location = loc

    # check if the advisor is not from a school - i.e. an Affiliat Organization
    def isOrganization(self):
        if ("Affiliate Organization" in self.location):
            return 1
        else:
            return 0


    # check if the advisor is for high school students
    def isHighSchool(self):
        if (("Elementary" in self.title) or ("Middle School" in self.title)):
            return 0
        else:
            return 1


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
            
            # loop through all the items, and access the required information
            for cell in cells:
                advisor=Advisor()
                if (advisor.setAdv(cell) == 1):
                    if (advisor.cleanAdv() == 1):
                        advisor.printAdv()

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
