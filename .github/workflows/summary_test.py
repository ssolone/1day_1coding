import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

def fetch_news(query, num_results=10):
    url = f"https://search.naver.com/search.naver?where=news&query={query}"
    news_data = []

    for start in range(1, num_results + 1, 10):  # Pagination을 고려하여 10개씩 요청
        response = requests.get(f"{url}&start={start}")
        soup = BeautifulSoup(response.text, 'html.parser')
        
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
        time.sleep(random.uniform(1, 3)) 
    except Exception as e:
            print(f"Error fetching page {start}: {e}")
            continue

    return news_data

def extract_and_summarize(link):
    try:
        page = requests.get(link, timeout=5)
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
news_data = fetch_news(query, num_results=30)
save_to_csv(news_data)
