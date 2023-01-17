from bs4 import BeautifulSoup

from locators.book_locators import BookLocators


class BookParser:
    def __init__(self,parent) -> None:
        self.parent = parent


    @property
    def name(self):
        locator = BookLocators.NAME_LOCATOR
        item_link = BookLocators.self.parent.select_one(locator)
        item_name = item_link.link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = BookLocators.LINK_LOCATOR
        item_link = BookLocators.self.parent.select_one(locator)
        return item_link

    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).attrs['href']

    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        return rating_classes[0]
    