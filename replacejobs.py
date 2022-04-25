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
    jobname.append(text.iloc[:,:1])
    company.append(text.iloc[:,1:2])
    location.append(text.iloc[:,2:3])
    joburl.append(text.iloc[:,3:4])



base = os.path.dirname(os.path.abspath(__file__))
html = open(os.path.join(base, 'datanuggets.html'))
soup=BeautifulSoup(html,'html.parser')

old_text = soup.find('div',class_='cardx')
new_text=old_text.find(text=re.compile('Sr Data Scientist')).replace_with('hello world')
# new_text=old_text.find(text=re.compile('Principal Data Scientist')).replace_with('hello mahhhn')

# for i in soup.find('div',class_='cardx'):
#     i.find(text=re.compile('Sr Data Scientist')).replace_with('hello world')

with open("datanuggets1.html", "wb") as f_output:
    f_output.write(soup.prettify("utf-8"))

