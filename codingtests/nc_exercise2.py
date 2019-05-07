# 2019.05.07 45 minute exercise/discussion with James at NovaCredit
# Environment issues slowed the progress, and this assumed the use of the third
# party library BeautifulSoup, which had some issues on installation.

import urllib.request
import os.path
from bs4 import BeautifulSoup


# This a specific solution for scraping a specific site (lolcats.com) and it
# makes many assumptions about the way the site html is set up.
def solution():
    root_url = 'http://www.lolcats.com/'
    num_pages_to_scrape = 5  # number of pages to scrape from site
    page_contents = urllib.request.urlopen(root_url)
    soup = BeautifulSoup(page_contents, 'html.parser')

    while num_pages_to_scrape > 0:  # defined above
        next_page = soup.find_all("a", text="next")
        next_url = root_url + next_page[0]['href']

        images = soup.select(".lolcat")  # get the images on the current page
        for image in images:
            if image['src']:  # if we're able to parse the src url, write the image locally
                urllib.request.urlretrieve(root_url + image['src'], os.path.basename(image['src']))

        # We're done with all images on this page loaded, load the next page
        page_contents = urllib.request.urlopen(next_url)
        soup = BeautifulSoup(page_contents, 'html.parser')
        num_pages_to_scrape -= 1  # decrement the count for pages to scrape


solution()
