import re
import logging

from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')

class BookParser:
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    
    
    def __init__(self, parent):
        logger.debug(f'New book parser created from `{parent}`')
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name} {self.price}, {self.rating} stars>'

    @property
    def name(self):
        logger.debug('Finding book name...')
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        logger.info(f'Found book name, `{item_name}`.')
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        logger.debug('Finding book page link...')
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']
        logger.info(f'Found book page link, `{item_link}`.')
        return item_link

    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string
        logger.debug(f'Item price element found, `{item_price}`')

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        
        price = float(matcher.group(1))
        logger.info(f'Found book price, `{price}`.')
        return price

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        return rating_number
    