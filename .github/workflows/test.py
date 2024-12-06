import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://realpython.github.io/fake-jobs/")
soup = bs(page.text, "html.parser")

#news = soup.find_all("div", {"class":"container__headline container_list-images-with-description__headline"})
#news_title = soup.find_all("span", {"class":"container__headline-text"})

#for index in enumerate(news, 1):
#    print("{} 번째 뉴스 : {}".format(index, news_title.text))

results = soup.find(id="ResultsContainer")

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_cards = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_card in python_job_cards:
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    link_url = job_card.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")
