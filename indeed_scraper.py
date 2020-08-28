from bs4 import BeautifulSoup
import requests

URL_PREFIX = 'https://de.indeed.com'
NUMBER_OF_SEARCH_PAGES = 10
PAGE_RESULTS_NUMBERS = list(range(0, NUMBER_OF_SEARCH_PAGES*11, 10))

# Loop through number of search pages
for search_page in PAGE_RESULTS_NUMBERS:
    # Set up links for scraping
    url = f'https://de.indeed.com/Jobs?l=Berlin&sort=date&lang=en&start={search_page}'
    main_jobs_page = requests.get(url).text
    soup = BeautifulSoup(main_jobs_page, 'lxml')

    # Find all elements on page
    job_links = []
    results = soup.find_all('div', {"data-tn-component":"organicJob"})
    for i in range(len(results)):
        job_link = results[i].h2.a['href']
        job_links.append(job_link)

# print(len(job_links))
# for link in job_links:
#     print(f'{URL_PREFIX}{link}')

# Loop through elements and open


# Scrape page
# On indeed_job_info

# Write to file

# Continue for next page of results

