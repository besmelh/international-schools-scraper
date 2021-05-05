
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys #in order to be able to hit keys like enter and esc, etc.
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time #to add timers

# # source1 - object constructor for school advisors
# class Advisor:
#     def setAdv(self, name, title, location, email):
#         self.name = name
#         self.title = title
#         self.location = location
#         self.email = email
    
#     def printAdv(self):
#         print(f'Name: {name}, Title: {title}, Location: {location}, Email: {email}')

# #return a default value to variable if it's unknown
# def checkValue(main, default):
#     value = ""
#     try:
#         value = main
#     except:
#         value = default
#     return value

# def scrapeSource1():
#     #initialize webpage
#     PATH = '/Users/besmelhalshaalan/Desktop/Education/MillieGroup/project1b/chromedriver'
#     driver = webdriver.Chrome(PATH)
#     driver.get("https://www.nesacenter.org/membership-directory/contacts")

#     #scan through all result pages
#     pageNumber = 1
#     while (pageNumber <= 10):
#         try:
#             link = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, '//*[@id="fsEl_2214"]/div/div[3]/a[2]'))
#             )
#             link.click()
#             pageNumber = pageNumber + 1
#             #navigate to the section where all the indivdual cells are located
#             mainList = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, '//*[@id="fsEl_2214"]/div'))
#             )

#             #save all the individual cells that contain advisor info into an array - all have the same class
#             cells = mainList.find_elements_by_class_name("fsConstituentItem")

#             #loop through all the items, and access the required information
#             for cell in cells:
#                 # may need to be set as optional variables
#                 name = checkValue(cell.find_element_by_class_name("fsFullName"), "n/a")
#                 title = checkValue(cell.find_element_by_class_name("fsTitles"), "n/a")
#                 location = checkValue(cell.find_element_by_class_name("fsLocations"), "n/a")
#                 email = checkValue(cell.find_element_by_class_name("fsEmail"), "n/a")

#                 advisor = Advisor()
#                 advisor.setAdv(name, title, location, email)
#                 advisor.printAdv()
        
#         finally:
#             driver.quit()

# scrapeSource1()






        # # page number link //*[@id="fsEl_2214"]/div/div[3]/a[{page-number}]
        # link=driver.find_element_by_xpath('//*[@id="fsEl_2214"]/div/div[3]/a[2]')
        # link.click()
        # time.sleep(3)
        # # navigate to the section where all the indivdual cells are located
        # mainList=WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, '//*[@id="fsEl_2214"]/div'))
        # )
        
        # # save all the individual cells that contain advisor info into an array - all have the same class
        # cells = mainList.find_elements_by_class_name("fsConstituentItem")
        # # loop through all the items, and access the required information
        # for cell in cells:
        #     # may need to be set as optional variables
        #     name=cell.find_element_by_class_name("fsFullName").text
        #     try:
        #         title=cell.find_element_by_class_name("fsTitles").text
        #     except:
        #         title="n/a"
        #     try:
        #         location=cell.find_element_by_class_name("fsLocations").text
        #     except:
        #         location="n/a"
        #     try:
        #         email=cell.find_element_by_class_name("fsEmail").text
        #     except:
        #         email="n/a"
        #     advisor=Advisor()
        #     advisor.setAdv(name, title, location, email)
        #     print(f'Name: {name}, Title: {title}, Location: {location}, Email: {email}')
        




# with loop

   try:
        #scan through all result pages
        pageNumber = 1
        while pageNumber <= 10:
            # Select the next page link once it's available
            pageXPath = f'//*[@id="fsEl_2214"]/div/div[3]/a[{pageNumber}]'
            pageLink = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, pageXPath)) 
            )
            pageLink.click()
            #prepare for the next loop
            pageNumber = pageNumber + 1
            
            # navigate to the section where all the indivdual cells are located, as soon as they're loaded
            mainList = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="fsEl_2214"]/div'))
            )
            print("here4")
            
            # save all the individual cells that contain advisor info into an array - all have the same class
            cells = mainList.find_elements_by_class_name("fsConstituentItem")

            # loop through all the items, and access the required information
            for cell in cells:
                #access the info
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
                #save the info of each advisor
                advisor = Advisor()
                advisor.setAdv(name, title, location, email)
                advisor.printAdv()


        # # page number link //*[@id="fsEl_2214"]/div/div[3]/a[{page-number}]
        # link=driver.find_element_by_xpath('//*[@id="fsEl_2214"]/div/div[3]/a[2]')
        # link.click()
        # time.sleep(3)
        # # navigate to the section where all the indivdual cells are located
        # mainList=WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, '//*[@id="fsEl_2214"]/div'))
        # )
        
        # # save all the individual cells that contain advisor info into an array - all have the same class
        # cells = mainList.find_elements_by_class_name("fsConstituentItem")
        # # loop through all the items, and access the required information
        # for cell in cells:
        #     # may need to be set as optional variables
        #     name=cell.find_element_by_class_name("fsFullName").text
        #     try:
        #         title=cell.find_element_by_class_name("fsTitles").text
        #     except:
        #         title="n/a"
        #     try:
        #         location=cell.find_element_by_class_name("fsLocations").text
        #     except:
        #         location="n/a"
        #     try:
        #         email=cell.find_element_by_class_name("fsEmail").text
        #     except:
        #         email="n/a"
        #     advisor=Advisor()
        #     advisor.setAdv(name, title, location, email)
        #     print(f'Name: {name}, Title: {title}, Location: {location}, Email: {email}')
        
    #     print("Source 1 scraped successfully.")
    # finally:
    #         driver.quit()
