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
  link = news_link[i].get("href")
  data.append([num, title, media, link])

print(data)

with open('news.csv', 'w') as file:
  file.write('No,Title,Media,Link\n')
  for i in data:
      file.write('{0},{1},{2},{3}\n'.format(i[0], i[1], i[2], i[3]))
