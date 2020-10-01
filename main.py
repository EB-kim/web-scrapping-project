import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=50&l=Los+Angeles%2C+CA&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch")
indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")## Make soup of it to see how many pages. Soup allow to extract data

pagination = indeed_soup.find("div", {"class": "pagination"})## find html that only include div with class called pagination
print(pagination)


pages = pagination.find_all('a') ## is a soup and page
print(pages)
spans =[]
for page in pages:
   print(page.find("span"))
   
    
  

