from selenium import webdriver
from selenium.common import exceptions
import LyricsWikiaSource

def getInstance(source):
    instance = None
    if source == 1:
        instance = LyricsWikiaSource.LyricsWikiaSource()
    return instance

class DataSource(object):

    def __init__(self):
        self.crawler = webdriver.PhantomJS(executable_path='/var/www/html/neatcomics-scrapper/selenium-driver/phantomjs')

    def grabLyric(self, artist, title):
        raise NotImplementedError("Subclasses must override grabLyric method")

    # returns an url to the album cover
    def grabAlbumCover(self, artist, album):
        raise NotImplementedError("Subclasses must override grabAlbumCover method")

    def quit(self):
        self.crawler.quit()