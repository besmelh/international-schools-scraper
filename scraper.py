from selenium import webdriver
# in order to be able to hit keys like enter and esc, etc.
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # to add timers

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
        PATH = '/Users/besmelhalshaalan/Desktop/Education/MillieGroup/project1b/chromedriver'
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://www.nesacenter.org/membership-directory/contacts")
    


    def scrapePage(self, pageNumber):

        try:
            # retreive the link to the sepcific page number
            link = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="fsEl_2214"]/div/div[3]/a[{pageNumber}]'))
            )
            link.click()
            time.sleep(3)

            # navigate to the section where all the indivdual cells are located
            mainList = WebDriverWait(self.driver, 10).until(
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
            
            
        finally:
            print(f"Page {pageNumber} done scraping.")

    def scrapeSource(self):
        self.scrapePage(4)
        print("All sources done scraping.")
        self.driver.quit()


#Main function calls ***************************
scraper = Scraper()
scraper.scrapeSource()
