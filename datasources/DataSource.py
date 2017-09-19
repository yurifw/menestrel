from datasources import LyricsWikiaSource, AZLyricsSource, LetrasMusSource

def getInstance(source):
    instance = None
    if source == 1:
        instance = DataSource(LyricsWikiaSource.LyricsWikiaSource())
    if source == 2:
        instance = DataSource(AZLyricsSource.AZLyricsSource())
    if source == 3:
        instance = DataSource(LetrasMusSource.LetrasMusSource())
    return instance

def getInstances():
    instances = []
    instances.append(DataSource(LyricsWikiaSource.LyricsWikiaSource()))
    instances.append(DataSource(AZLyricsSource.AZLyricsSource()))
    instances.append(DataSource(LetrasMusSource.LetrasMusSource()))
    return instances

class DataSource(object):

    def __init__(self, source):
        self.source = source

    def grabLyric(self, artist, title):
        return self.source.grabLyric(artist, title)

    def grabAlbumCover(self, artist, album):
        return self.source.grabAlbumCover(artist, album)

    def quit(self):
        self.source.quit()