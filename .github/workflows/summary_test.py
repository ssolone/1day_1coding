import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def fetch_news(query):
    url = f"https://search.naver.com/search.naver?where=news&query={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_data = []

    for item in soup.select('.news_wrap'):
        title_tag = item.select_one('.news_tit')
        title = title_tag.get_text() if title_tag else 'No Title'
        link = title_tag['href'] if title_tag else 'No Link'
        
        media_tag = item.select_one('.info_group .press')
        media = media_tag.get_text() if media_tag else 'No Media'

        date_tag = item.select_one('.info_group .info')
        date = date_tag.get_text() if date_tag else 'No Date'
        
        summary = extract_and_summarize(link)

        news_data.append({
            'Title': title,
            'Date': date,
            'Media': media,
            'Link': link,
            'Summary': summary
        })

    return news_data

def extract_and_summarize(link):
    try:
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')

        paragraphs = soup.find_all('p')
        text = ' '.join([para.get_text() for para in paragraphs])

        # 문장 분리
        sentences = text.split('. ')
        # 가장 긴 문장 3개 선택
        sentences = sorted(sentences, key=len, reverse=True)[:3]
        summary = '. '.join(sentences)

        return summary
    except Exception as e:
        return f"Error: {e}"

def save_to_csv(news_data, filename='naver_news.csv'):
    df = pd.DataFrame(news_data)
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"Data saved to {filename}")

query = 'AI'
news_data = fetch_news(query)
save_to_csv(news_data)
