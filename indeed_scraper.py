from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

URL_PREFIX = 'https://de.indeed.com'
NUMBER_OF_SEARCH_PAGES = 1
PAGE_RESULTS_NUMBERS = list(range(0, NUMBER_OF_SEARCH_PAGES*11, 10))

# Loop through number of search pages
def main_page_setup(search_page):
    # Create soup object for main jobs page
    url = f'https://de.indeed.com/Jobs?l=Berlin&sort=date&lang=en&start={search_page}'
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

# Set up links for scraping
def single_page_setup(job_link):
    job_link_url = job_link
    job_information = requests.get(job_link_url).text
    soup = BeautifulSoup(job_information, 'lxml')
    return soup

# Scrape data from individual job listing page
def scrape_page_data(soup):
    title = soup.find('h1').text
    company = soup.find('div', class_="icl-u-lg-mr--sm icl-u-xs-mr--xs").text
    location = soup.find('div', class_="icl-u-xs-mt--xs icl-u-textColor--secondary jobsearch-JobInfoHeader-subtitle jobsearch-DesktopStickyContainer-subtitle").find_all('div')[-1].text
    job_info = soup.find('div', id="jobDescriptionText").text
    job_data = [title, company, location, job_info]
    return job_data

# Export data to spreadsheet
def export_data(title, company, location, job_info):
    job_data = pd.DataFrame(
    {
        'title': title,
        'company': company,
        'location': location,
        'job_info': job_info,
    })

    print(job_data)

    #job_data.to_csv(r'/home/dan/Desktop/job_data.csv')


def main():
    job_dict = {}
    count = 1
    # Loop through each page of job adverts
    for search_page in PAGE_RESULTS_NUMBERS:
        # Create soup object for current main jobs listing page
        soup = main_page_setup(search_page)
        # Extract job links from page
        job_links = prepare_job_links(soup)


        # Loop through each link, extract all data from job listing into list and add to dict
        for job_link in job_links:
            # Create soup object for individual job listing page
            soup = single_page_setup(job_link)
            # Scrape individual job data from page
            job_data = scrape_page_data(soup)
            # Add job data to dict
            job_dict[count] = job_data
            # increment count
            count += 1

    print(job_dict)
    # # # export_data(title, company, location, job_info)



main()



