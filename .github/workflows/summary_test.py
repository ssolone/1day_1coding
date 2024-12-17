import feedparser
from newspaper import Article
from summa.summarizer import summarize

rss_url = "http://feeds.feedburner.com/inven"

print(len(rss_feed.entries))

for p in rss_feed.entries:

    url = p.link

article = Article(url, language = 'ko')
article.download()
article.parse()

NewsFeed = article.text
NewsSum = summarize(NewsFeed)

print(article.title + '\n' + NewsFeed + '\n' + NewsSum)
