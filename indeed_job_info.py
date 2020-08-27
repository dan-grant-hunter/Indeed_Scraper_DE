from bs4 import BeautifulSoup
import requests


# Set up links for scraping
def single_page_setup(single_page_url):
    single_page_url = 'https://de.indeed.com/rc/clk?jk=022928a345e8d3ea&fccid=ec43e957e65d7c21&vjs=3'
    job_information = requests.get(singe_page_url).text
    soup = BeautifulSoup(job_information, 'lxml')

    # Scrape all relevant information
    title = soup.find('h1').text
    company = soup.find('div', class_=" jobsearch-CompanyInfoWithoutHeaderImage").find_all('div')[3].text
    location = soup.find('div', class_=" jobsearch-CompanyInfoWithoutHeaderImage").find_all('div')[5].text
    job_info = soup.find('div', id="jobDescriptionText").text

# Write to CSV
