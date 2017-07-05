from DataSource import DataSource
import time
import urllib2

class LyricsWikiaSource(DataSource):
    def grabLyric(self, artist, title):
        title = title.replace(" ", "_")
        url = "http://lyrics.wikia.com/wiki/"+artist+":"+title
        self.crawler.get(url)
        lyrics = self.crawler.find_element_by_class_name("lyricbox").text
        return lyrics

    def grabAlbumCover(self, artist, album):

        artist = artist.replace(" ","_")
        url = "http://lyrics.wikia.com/wiki/"+artist
        self.crawler.get(url)
        headlines = self.crawler.find_elements_by_class_name("mw-headline")
        for h in headlines:
            for child in h.find_elements_by_css_selector("*"):  # gets all children
                if album in child.get_attribute("title"):
                    self.crawler.get(child.get_attribute("href"))
                    time.sleep(0.5)
                    div = self.crawler.find_element_by_class_name("plainlinks")
                    a = div.find_element_by_tag_name("a")
                    response = urllib2.urlopen(a.get_attribute("href"))
                    imagedata = response.read()
                    return imagedata
