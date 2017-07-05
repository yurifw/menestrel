import os

import Mp3File
from datasources import DataSource


class FileLister(object):

    # All methods starting with list should return a list of dictionaries with the following template:
    # {
    #   path : "path to the mp3 file",
    #   artist : "artist name",
    #   title : "title of the song",
    #   album : "album where this song is",
    #   track_num : (int) number of this track,
    #   year : "the year this song was released (YYYY)
    #   genre : "this song genre"
    #   lyrics : "the lyrics for this song"
    #   cover : "the front cover of the album this song appears in"
    # }
    def listArtistAlbumSong(self):

        albumPath = raw_input("enter the absolute path to your album folder:\n")
        files=[]
        dataSource = DataSource.getInstance(1)
        for file in os.listdir(albumPath):
            if not file.endswith("mp3"):
                continue
            path = albumPath+"/"+file

            file = Mp3File.Mp3File()
            file.path =  path
            file.artist = path.split("/")[-3]
            file.title = file.split(".")[-2].split("-")[-1].lstrip()
            file.album = path.split("/")[-2].split("-")[-2].rstrip()
            file.track_num = file.split(".")[-2].split("-")[-2].rstrip()
            file.year = path.split("/")[-2].split("-")[-1].lstrip()
            file.genre = "Rock"
            file.lyrics = dataSource.grabLyric(file.artist, file.title)
            file.cover = dataSource.grabAlbumCover(file.artist, file.album)

            files.append(file)
        dataSource.quit()
        return files

    def list(self):
        while True:
            print "How are you MP3's organized?"
            print "1 - /path_to_my_music_folder/{artist}/{album}-{year}/{track number}-{track title}.mp3"
            print "2 - Quit"
            print "to request another method, go to the project page at and create an issue"
            option = raw_input()
            if option == "1":
                return self.listArtistAlbumSong()
            if option == "2":
                quit()
