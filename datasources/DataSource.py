

class DataSource(object):

    def __init__(self, source):
        self.source = source

    def grabLyric(self, artist, title):
        return self.source.grabLyric(artist, title)

    def grabAlbumCover(self, artist, album):
        return self.source.grabAlbumCover(artist, album)

    def quit(self):
        self.source.quit()