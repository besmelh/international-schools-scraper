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


def scrapePage(pageNumber):
    # initialize webpage
    PATH = '/Users/besmelhalshaalan/Desktop/Education/MillieGroup/project1b/chromedriver'
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.nesacenter.org/membership-directory/contacts")

    try:

        link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="fsEl_2214"]/div/div[3]/a[{pageNumber}]'))
        )
        link.click()
        time.sleep(3)

        # navigate to the section where all the indivdual cells are located
        mainList = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="fsEl_2214"]/div'))
        )
        
        # save all the individual cells that contain advisor info into an array - all have the same class
        cells = mainList.find_elements_by_class_name("fsConstituentItem")
        print(cells)
        
        # loop through all the items, and access the required information
        for cell in cells:
            # may need to be set as optional variables
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
        print("Source 1 done scraping.")
        driver.quit()

def scrapeSource():
    scrapePage(4)


scrapeSource()