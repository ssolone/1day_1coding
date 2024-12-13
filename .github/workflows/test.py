import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://news.naver.com/?viewType=pc")
soup = bs(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

news_title = soup.find_all("h4", {"class":"cn_title"})
media_com = soup.find_all("div", {"class":"cn_name"})
news_link = soup.find_all("a", {"class":"cjs_nf_a _item _cds_link _newsflash_link"})

data = []

for i in range(len(news_title)):
  num = i+1
  title = news_title[i].text
  media = media_com[i].text
  link = "https://news.naver.com" + news_link[i].get("href")
  data.append([num, title, media, link])

print(data)

with open('news.csv', 'w', newline='', encoding='utf-8-sig') as file:
  writer = csv.writer(file)
  writer.writerow(['No', 'Title', 'Media', 'Link'])
  writer.writerows(data)
