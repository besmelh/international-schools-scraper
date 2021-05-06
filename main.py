from scraper_NESA import *
from dataToCsv import *

# Main function calls ******************************************************

scraperNESA = Scraper_NESA()
# scraperNESA.scrapePage(2)
scraperNESA.scrapeSource()
scraperNESA.quitDriver()

csvNESA = NESA_CSV()
csvNESA.writeFile(scraperNESA.allAdvisors)