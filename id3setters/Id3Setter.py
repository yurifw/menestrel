class Id3Setter(object):
    # file is a dictionary with the following template:
    # {
    #   path : "path to the mp3 file",
    #   artist : "artist name",
    #   title : "title of the song",
    #   album : "album where this song is",
    #   track_num : "number of this track",
    #   year : "the year this song was released (YYYY)
    #   genre : "this song genre"
    #   lyrics : "the lyrics for this song"
    #   cover : "the front cover of the album this song appears in"
    # }

    def setTags(self, file):
        raise NotImplementedError("Subclasses must override setTags method")