
from filelisters import ArtistAlbumLister


def chooseLister():
    while True:
        print "How are you MP3's organized?"
        print "1 - /path_to_my_music_folder/{artist}/{album}-{year}/{track number}-{track title}.mp3"
        print "0 - Quit"
        print "to request another method, go to the project page at https://github.com/yurifw/menestrel and create an issue"
        option = raw_input()
        if option == "1":
            return FileLister(ArtistAlbumLister.ArtistAlbumLister())
        if option == "0":
            quit()

class FileLister(object):

    def __init__(self, lister):
        self.lister = lister

    # All methods starting with list should return a list of instances of Mp3File
    def listFiles(self):
        return self.lister.listFiles()





