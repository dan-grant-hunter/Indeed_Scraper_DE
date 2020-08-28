from bs4 import BeautifulSoup
import requests

URL_PREFIX = 'https://de.indeed.com'
NUMBER_OF_SEARCH_PAGES = 10
PAGE_RESULTS_NUMBERS = list(range(0, NUMBER_OF_SEARCH_PAGES*11, 10))

# Loop through number of search pages
def main_page_setup():
    # for search_page in PAGE_RESULTS_NUMBERS:
    #     # Set up links for scraping
    url = f'https://de.indeed.com/Jobs?l=Berlin&sort=date&lang=en&start=0'
    main_jobs_page = requests.get(url).text
    soup = BeautifulSoup(main_jobs_page, 'lxml')
    return soup

# Prepare list of job links
def prepare_job_links(soup):
    job_links = []
    results = soup.find_all('div', {"data-tn-component":"organicJob"})
    for i in range(len(results)):
        job_link = f"{URL_PREFIX}{results[i].h2.a['href']}"
        job_links.append(job_link)
    return job_links

# Pass links to single page scraper function
def scrape_page_data():
    pass



main_page_setup()
# Loop through elements and open


# Scrape page
# On indeed_job_info

# Write to file

# Continue for next page of results

