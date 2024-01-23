import requests
from bs4 import BeautifulSoup as bs
import re

def parse(link):
    page = requests.get(link)
    soup = bs(page.text, "html.parser")
    #загружаем саммари
    summary = soup.find('span', class_='topic-body__title').text
    #загружаем все блоки с основным текстом из новости
    body = "\n".join([p.text for p in soup.find_all('p', class_='topic-body__content-text')])
    return summary + "\n" + body

def parselink(link):
    # парсим ИД из ссылки
    try:
        return re.search(r'/23/([^/]+)\/', link).group(1)
    except:
        return None

def main():
    link = 'https://lenta.ru/news/2024/01/22/joke/'
    print(parselink(link))
if __name__ == '__main__':
    main()