import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://news.naver.com/?viewType=pc")
soup = bs(page.content, "html.parser")

#news = soup.find_all("div", {"class":"container__headline container_list-images-with-description__headline"})
#news_title = soup.find_all("span", {"class":"container__headline-text"})

#for index in enumerate(news, 1):
#    print("{} 번째 뉴스 : {}".format(index, news_title.text))

results = soup.find(id="ResultsContainer")

news_title = soup.find_all("h4", {"class":"cn_title"})
media_com = soup.find_all("div", {"class":"cn_name"})

for i in range(len(news_title)):
  print(i+1,".", news_title[i].text,"[",media_com[i].text,"]")