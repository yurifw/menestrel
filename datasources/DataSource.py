from datasources import LyricsWikiaSource, AZLyricsSource

def getInstance(source):
    instance = None
    if source == 1:
        instance = DataSource(LyricsWikiaSource.LyricsWikiaSource())
    if source == 2:
        instance = DataSource(AZLyricsSource.AZLyricsSource())
    return instance

class DataSource(object):

    def __init__(self, source):
        self.source = source

    def grabLyric(self, artist, title):
        return self.source.grabLyric(artist, title)

    def grabAlbumCover(self, artist, album):
        return self.source.grabAlbumCover(artist, album)

    def quit(self):
        self.source.quit()