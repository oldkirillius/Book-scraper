from bs4 import BeautifulSoup
from locators.all_books_page import AllBooksPageLocators
from parser.book_parser import BookParser

class AllBooksPage:
    def __init__(self, page_content) -> None:
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]