import os

import Mp3File
from datasources import DataSource, LyricsWikiaSource, AZLyricsSource



def getInstance(source):
    instance = None
    if source == 1:
        instance = DataSource.DataSource(LyricsWikiaSource.LyricsWikiaSource())
    if source == 2:
        instance = DataSource.DataSource(AZLyricsSource.AZLyricsSource())
    return instance

class FileLister(object):

    # All methods starting with list should return a list of instances of Mp3File
    def listArtistAlbumSong(self):

        albumPath = raw_input("enter the absolute path to your album folder:\n")
        files=[]
        dataSource = getInstance(2)
        for file in os.listdir(albumPath):
            if not file.endswith("mp3"):
                continue
            path = albumPath+"/"+file

            mp3 = Mp3File.Mp3File()
            mp3.path = path
            mp3.artist = path.split("/")[-3]
            mp3.title = path.split(".")[-2].split("-")[-1].lstrip()
            mp3.album = path.split("/")[-2].split("-")[-2].rstrip()
            mp3.track_num = file.split(".")[-2].split("-")[-2].rstrip()
            mp3.year = path.split("/")[-2].split("-")[-1].lstrip()
            mp3.genre = "Rock"
            mp3.lyrics = dataSource.grabLyric(mp3.artist, mp3.title)
            mp3.cover = dataSource.grabAlbumCover(mp3.artist, mp3.album)

            files.append(mp3)
        dataSource.quit()
        return files

    def list(self):
        while True:
            print "How are you MP3's organized?"
            print "1 - /path_to_my_music_folder/{artist}/{album}-{year}/{track number}-{track title}.mp3"
            print "0 - Quit"
            print "to request another method, go to the project page at https://github.com/yurifw/menestrel and create an issue"
            option = raw_input()
            if option == "1":
                return self.listArtistAlbumSong()
            if option == "0":
                quit()
