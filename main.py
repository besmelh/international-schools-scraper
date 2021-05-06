from scraper_NESA import *
from scraper_ISD import *
from dataToCsv import *


def nesa_test():
    # Scrape NESA - source 1
    scraperNESA = Scraper_NESA()
    scraperNESA.scrapeSource()
    scraperNESA.quitDriver()
    # Save NESA's information to a cvs file
    csvNESA = NESA_CSV()
    csvNESA.writeFile(scraperNESA.allAdvisors)

def isd_test():
    # Scrape ISD - source 2
    scraperISD = Scraper_ISD()
    scraperISD.scrapeSource()
    scraperISD.quitDriver()
    # Save NESA's information to a cvs file
    csvISD = ISD_CSV()
    csvISD.writeFile(scraperISD.allSchools)

#nesa_test()
isd_test()

