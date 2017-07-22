from selenium import webdriver
from selenium.common import exceptions
import re
from datasources import LyricsWikiaSource

class LetrasMusSource():

    def __init__(self):
        self.crawler = webdriver.PhantomJS(executable_path='/var/www/html/neatcomics-scrapper/selenium-driver/phantomjs')
        self.cache = []

    def grabLyric(self, artist, title):
        print "scraping Letras.Mus.Br for \"{}\" lyrics".format(title)
        regex = re.compile('[^a-zA-Z0-9\-]')
        title = title.replace(" ", "-")
        title = regex.sub('', title).lower()
        artist = artist.replace(" ", "-")
        artist = regex.sub('', artist).lower()
        url = "https://www.letras.mus.br/" + artist + "/" + title
        self.crawler.get(url)
        div = self.crawler.find_element_by_xpath("id('js-lyric-cnt')/div[3]/div[2]/article")
        lyrics = div.text
        return lyrics

    def grabAlbumCover(self, artist, album):
        for cached in self.cache:
            if artist + album in cached.keys():
                print "found artwork in cache"
                return cached[artist + album]

        print "Letras.Mus.Br does not have an album artwork, so we are fetching from LyricsWikia"
        dataSource = LyricsWikiaSource.LyricsWikiaSource()
        artwork = dataSource.grabAlbumCover(artist, album)
        self.cache.append({artist + album: artwork})
        return artwork

    def quit(self):
        self.crawler.quit()