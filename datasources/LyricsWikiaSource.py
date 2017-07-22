from selenium import webdriver
from selenium.common import exceptions
import time
import urllib2

class LyricsWikiaSource():

    def __init__(self):
        self.crawler = webdriver.PhantomJS(executable_path='/var/www/html/neatcomics-scrapper/selenium-driver/phantomjs')
        self.cache = []

    def grabLyric(self, artist, title):
        print "scraping Lyrics Wikia for \"{}\" lyrics".format(title)
        title = title.replace(" ", "_")
        url = "http://lyrics.wikia.com/wiki/"+artist+":"+title
        self.crawler.get(url)
        lyrics = self.crawler.find_element_by_class_name("lyricbox").text
        return lyrics

    def grabAlbumCover(self, artist, album):
        print "scraping Lyrics Wikia for \"{}\" artwork".format(album)
        artist = artist.replace(" ","_")

        for cached in self.cache:
            if artist+album in cached.keys():
                print "found artwork in cache"
                return cached[artist+album]

        url = "http://lyrics.wikia.com/wiki/"+artist
        self.crawler.get(url)
        headlines = self.crawler.find_elements_by_class_name("mw-headline")
        imagedata = None
        for h in headlines:
            for child in h.find_elements_by_css_selector("*"):  # gets all children
                if album in child.get_attribute("title"):
                    self.crawler.get(child.get_attribute("href"))
                    time.sleep(0.5)
                    div = self.crawler.find_element_by_class_name("plainlinks")
                    a = div.find_element_by_tag_name("a")
                    response = urllib2.urlopen(a.get_attribute("href"))
                    imagedata = response.read()
                else:
                    print "sorry, I could not scrape LyricsWikia for the artwork"
                    link = raw_input("enter the url for the image:\n")
                    response = urllib2.urlopen(link)
                    imagedata = response.read()
                self.cache.append({artist+album:imagedata})
                return imagedata

    def quit(self):
        self.crawler.quit()
