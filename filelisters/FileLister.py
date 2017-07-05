import os

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
            print path
            artist = path.split("/")[-3]
            title = file.split(".")[-2].split("-")[-1].lstrip()
            album = path.split("/")[-2].split("-")[-2].rstrip()
            track_num = file.split(".")[-2].split("-")[-2].rstrip()
            year = path.split("/")[-2].split("-")[-1].lstrip()
            genre = "Rock"
            lyrics = dataSource.grabLyric(artist, title)
            cover = dataSource.grabAlbumCover(artist, album)

            mp3 = {"path":path, "artist":artist, "title":title, "album":album, "track_num":track_num,
               "year":year,"genre":genre, "lyrics":lyrics, "cover":cover}
            files.append(mp3)
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
