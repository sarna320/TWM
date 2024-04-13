import requests
from bs4 import BeautifulSoup
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

urls_to_scrape = []
with open("url_to_scrape.txt", "r") as file:
    for line in file:
        urls_to_scrape.append(line)
#print(urls_to_scrape)

#url_of_img_to_scrape=[]
for url_to_scrape in urls_to_scrape:
    response = requests.get(url_to_scrape, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    articles=soup.find_all("article") # article is class of every post    
    for article in articles:
        try:
            url=article.find("img").get("src")
            if url.startswith("https://") and url.endswith("320x240"):
                #url_of_img_to_scrape.append(url)
                with open("urls_of_img_to_scrape.txt", "a") as file:
                    file.write(url + "\n")  # Dodaj link na końcu pliku txt
        except:
            continue
    time.sleep(0.3)
    if url_to_scrape!="https://www.otomoto.pl/osobowe\n":
        proc=int(url_to_scrape.split('=')[-1].replace('\n', ''))/len(urls_to_scrape)*100
        print(f"{proc}%")
    