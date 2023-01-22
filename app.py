import requests
import logging

from pages.All_Books_Pages import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('scraping')

print('Loading books list...')
logger.info('Loading books list.')

logger.info('Requesting http://books.toscrape.com')
page_content = requests.get('https://books.toscrape.com').content
page = AllBooksPage(page_content)


books = page.books

for page_num in range(1, page.page_count):
    url=f'https://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content = requests.get(url).content
    logger.debug('Creating AllBooksPage from page content.')
    page = AllBooksPage(page_content)
    books.extend(page.books)