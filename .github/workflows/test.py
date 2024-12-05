import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://edition.cnn.com/search?q=AI&from=0&size=10&page=1&sort=newest&types=all&section=")
soup = bs(page.text, "html.parser")

news = soup.find_all("div", {"class":"container__headline container_list-images-with-description__headline"})
news_title = soup.find_all("span", {"class":"container__headline-text"})

for index, news in enumerate(news, 1):
    print("{} 번째 뉴스 : {}".format(index, news_title.text))
