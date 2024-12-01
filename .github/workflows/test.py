import requests
from bs4 import BeautifulSoup

URL = "https://www.linkedin.com/search/results/people/?currentCompany=%5B20708%5D"
req = requests.get(URL)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

jobs_title = soup.find_all("div",{"class":"entity-result__primary-subtitle.t-14.t-black"})
print(jobs_title)
