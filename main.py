from scraper_NESA import *
from scraper_ISD import *
from dataToCsv import *

# # Scrape NESA - source 1
# scraperNESA = Scraper_NESA()
# scraperNESA.scrapeSource()
# scraperNESA.quitDriver()
# # Save NESA's information to a cvs file
# csvNESA = NESA_CSV()
# csvNESA.writeFile(scraperNESA.allAdvisors)

scraperISD = Scraper_ISD()
scraperISD.scrapePage()
scraperISD.quitDriver()