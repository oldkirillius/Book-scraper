import requests

from pages.All_Books_Pages import AllBooksPage

page_content = requests.get('https://books.toscrape.com').content
page = AllBooksPage(page_content)

books = page.books

for book in books:
    print(book)