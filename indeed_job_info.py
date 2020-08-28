from bs4 import BeautifulSoup
import requests

test_link1 = 'https://de.indeed.com/rc/clk?jk=edd4176699c2f1d7&fccid=d79d00cbbf5795e0&vjs=3'
test_link2 = 'https://de.indeed.com/rc/clk?jk=fd4ff7f1657d391f&fccid=263d04306603c815&vjs=3'
test_link3 = 'https://de.indeed.com/company/Die-Datenschmiede/jobs/Machine-Learning-Scientist-a98985a165f75ab9?fccid=8e1751206f578cc3&vjs=3'
test_link4 = 'https://de.indeed.com/rc/clk?jk=c9c6f27387a9438e&fccid=d2aae6d9e2355253&vjs=3'
test_link5 = 'https://de.indeed.com/rc/clk?jk=8658efe7f9d8c654&fccid=5cd2518607580830&vjs=3'
test_link6 = 'https://de.indeed.com/rc/clk?jk=60e747ffc47dbb8b&fccid=1992e9a12e091329&vjs=3'
test_link7 = 'https://de.indeed.com/rc/clk?jk=e95fbd038c600750&fccid=da1e2e1c7bbb46be&vjs=3'
test_link8 = 'https://de.indeed.com/rc/clk?jk=d3715187cc2fc0d1&fccid=1992e9a12e091329&vjs=3'
test_link9 = 'https://de.indeed.com/rc/clk?jk=9db5d66ab5734fdc&fccid=a54066e6670be1ce&vjs=3'
test_link10 = 'https://de.indeed.com/rc/clk?jk=c87f256b6c7f42c5&fccid=66cb79b1fb76b1d5&vjs=3'
test_link11= 'https://de.indeed.com/rc/clk?jk=fe3fb1dcff9d0158&fccid=150614b16553c72a&vjs=3'
test_link12 = 'https://de.indeed.com/rc/clk?jk=bd97c23a6b43826d&fccid=b9561145e1e02981&vjs=3'
test_link13 = 'https://de.indeed.com/rc/clk?jk=1c451034b3c0a889&fccid=af31e16a17ddafd1&vjs=3'
test_link14 = 'https://de.indeed.com/rc/clk?jk=f3bd3ff0f4a4dec9&fccid=a54066e6670be1ce&vjs=3'
test_link15 = 'https://de.indeed.com/rc/clk?jk=7a9ca6f1ea2fb6b2&fccid=941c4fb004be80b8&vjs=3'


# TESTING
def test_single_page_setup(test_link):
    single_page_url = test_link
    job_information = requests.get(single_page_url).text
    soup = BeautifulSoup(job_information, 'lxml')

    # Scrape all relevant information
    title = soup.find('h1').text
    company = soup.find('div', class_="icl-u-lg-mr--sm icl-u-xs-mr--xs").text
    location = soup.find('div', class_="icl-u-xs-mt--xs icl-u-textColor--secondary jobsearch-JobInfoHeader-subtitle jobsearch-DesktopStickyContainer-subtitle").find_all('div')[-1].text
    job_info = soup.find('div', id="jobDescriptionText").text

    data_list = [title, company, location, job_info]
    print(data_list)

# # Set up links for scraping
# def single_page_setup(test_link):
#     single_page_url = test_link
#     job_information = requests.get(single_page_url).text
#     soup = BeautifulSoup(job_information, 'lxml')

#     # Scrape all relevant information
    title = soup.find('h1').text
    company = soup.find('div', class_="icl-u-lg-mr--sm icl-u-xs-mr--xs").text
    location = soup.find('div', class_="icl-u-xs-mt--xs icl-u-textColor--secondary jobsearch-JobInfoHeader-subtitle jobsearch-DesktopStickyContainer-subtitle").find_all('div')[-1].text
    job_info = soup.find('div', id="jobDescriptionText").text

#     data_list = [title, company, location, job_info]
#     print(data_list)


test_single_page_setup(test_link15)

links_that_dont_work = [7, 15]
