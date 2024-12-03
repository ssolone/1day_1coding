import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=AI")
soup = bs(page.text, "html.parser")

elements = soup.select('div.news_contents a > title')

for index, element in enumerate(elements, 1):
    print("{} 번째 뉴스 제목 : {}".format(index, element.text))
