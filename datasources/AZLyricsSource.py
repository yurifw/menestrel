from selenium import webdriver
from selenium.common import exceptions
import re

from datasources import LyricsWikiaSource


class AZLyricsSource():
    def __init__(self):
        self.crawler = webdriver.PhantomJS(executable_path='/var/www/html/neatcomics-scrapper/selenium-driver/phantomjs')
        self.cache = []

    def grabLyric(self, artist, title):
        print "scraping AZLyrics for \"{}\" lyrics".format(title)
        regex = re.compile('[^a-zA-Z0-9]')
        title = regex.sub('',title).lower()
        artist = regex.sub('',artist).lower()
        url = "http://www.azlyrics.com/lyrics/"+artist+"/"+title+".html"
        self.crawler.get(url)
        div = self.crawler.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[5]")
        lyrics = div.text
        return lyrics

    def grabAlbumCover(self, artist, album):
        for cached in self.cache:
            if artist+album in cached.keys():
                print "found artwork in cache"
                return cached[artist+album]

        print "AZLyrics does not have an album artwork, so we are fetching from LyricsWikia"
        dataSource = LyricsWikiaSource.LyricsWikiaSource()
        artwork = dataSource.grabAlbumCover(artist,album)
        self.cache.append({artist + album: artwork})
        return artwork

    def quit(self):
        self.crawler.quit()