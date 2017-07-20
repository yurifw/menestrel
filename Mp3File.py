class Mp3File:
    def __init__(self):
        self.path = ""
        self.artist = ""
        self.title = ""
        self.album = ""
        self.track_num = 0
        self.year = ""
        self.genre = ""
        self.lyrics = ""
        self.images = None

    def __str__(self):
        string = "path: " + self.path + "\n"
        string += "artist: " + self.artist + "\n"
        string += "title: " + self.title + "\n"
        string += "album: " + self.album + "\n"
        string += "track_num: " + self.track_num + "\n"
        string += "year: " + self.year + "\n"
        string += "genre: " + self.genre + "\n"
        string += "lyrics: " + self.lyrics[0:20] + "\n"
        return string

