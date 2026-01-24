# Парсер author.today с применением библиотеки beautifulsoup
import requests
from bs4 import BeautifulSoup
import json
def read_data_json(name):
    with open(f'{name}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data
def create_json(dictionary, name):
    with open(f'{name}.json', 'w', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=4)
def create_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup
def parse_soup(soup):
    big_body_div = soup.find_all('div', class_='bookcard')
    books = {}
    for link in big_body_div:
        book = link.find('div', class_='bookcard-title')
        if book and link.find('img', class_='lazyload'):
            title = book.text.strip("\n")
            href = f'{url}{link.find('a').get('href')}'
            author = link.find('div', class_='bookcard-authors')
            img_href = f'{link.find('img', class_='lazyload').get('data-src')}'
            if author:
                author = author.text.strip("\n")
            books[author] = title, href, img_href
    books_out = {}
    num = 1
    for author, title_href_img_href in books.items():
        book = {}
        response = requests.get(title_href_img_href[1])
        soup_a = BeautifulSoup(response.text, 'html.parser')
        content = soup_a.find('div', class_='rich-content')
        content_book = content.text.strip("\n")
        content_book = content_book.strip("'\r\n'")
        book['Название книги'] = title_href_img_href[0]
        book['Автор'] = author
        book['Краткое содержание'] = content_book
        book['Ссылка на книгу'] = title_href_img_href[1]
        book['Ссылка на обложку'] = title_href_img_href[2]
        books_out[num] = book
        num += 1
    return books_out
url ='https://author.today'
if __name__ == '__main__':
    url = 'https://author.today'
    soup = create_soup(url)
    books_out = parse_soup(soup)
    create_json(books_out, 'books')
