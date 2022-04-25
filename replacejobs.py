import pandas as pd
from bs4 import BeautifulSoup
import os
import re
import requests,openpyxl

text = pd.read_excel("C:/Users/hp/PycharmProjects/qweerty/Data Science Jobs.xlsx")
jobname=[]
company=[]
location=[]
joburl=[]

for i in range(24):
    jobname.append(text.iloc[i:i+1,:1])
    company.append(text.iloc[i:i+1,1:2])
    location.append(text.iloc[i:i+1,2:3])
    joburl.append(text.iloc[i:i+1,3:4])

print(jobname[0])

base = os.path.dirname(os.path.abspath(__file__))
html = open(os.path.join(base, 'datanuggets.html'))
soup=BeautifulSoup(html,'html.parser')

jobs=[]
for i in range(1,6):
    job = soup.find('div',class_='cardx'+str(i)).h3.get_text(strip=True)
    jobs.append(job)
# print(jobs)


for i in range(1,6):
    old_text = soup.find('div',class_='cardx'+str(i)).h3
    new_text=old_text.find(text=re.compile(str(jobs[i-1]))).replace_with(str(jobname[i-1]))


with open("datanuggets1.html", "wb") as f_output:
    f_output.write(soup.prettify("utf-8"))

