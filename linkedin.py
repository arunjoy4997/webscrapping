from bs4 import BeautifulSoup
import requests,openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Data science Jobs'
sheet.append(['job title','company','location','job url'])

source = requests.get('https://www.linkedin.com/jobs/search/?keywords=data%20scientist')
soup = BeautifulSoup(source.text,'html.parser')

jobs = soup.find('ul',class_='jobs-search__results-list').find_all('li')
# print(jobs)
for job in jobs:
     job_name = job.find('div','base-card base-card--link base-search-card base-search-card--link job-search-card').span.get_text(strip=True)
     company_name = job.find('div','base-card base-card--link base-search-card base-search-card--link job-search-card').h4.get_text(strip=True)
     location_ = job.find('span','job-search-card__location').get_text(strip=True)
     link = job.find('a','base-card__full-link')['href']

     # print(job_name)
     # print(company_name)
     # print(location_)
     # print(links)

     sheet.append([job_name,company_name,location_,link])
excel.save('Data Science Jobs.xlsx')

