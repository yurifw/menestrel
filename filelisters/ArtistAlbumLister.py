from datasources import DataSource
import os
import Mp3File
import selenium
import sys

class ArtistAlbumLister(object):

    def listFiles(self):
        albumPath = raw_input("enter the absolute path to your album folder:\n")
        files = []
        dataSources = DataSource.getInstances()
        for file in os.listdir(albumPath):
            if not file.endswith("mp3"):
                continue
            path = albumPath + "/" + file

            mp3 = Mp3File.Mp3File()
            mp3.path = path
            data = self.getDataFromFileName(path)
            mp3.artist = data['artist']
            mp3.title = data['title']
            mp3.album = data['album']
            mp3.track_num = data['track_num']
            mp3.year = data['year']
            mp3.genre = "Rock"

            for i, ds in enumerate(dataSources):
                try:
                    mp3.lyrics = ds.grabLyric(mp3.artist, mp3.title)
                    break
                except selenium.common.exceptions.NoSuchElementException:
                    if i == len(dataSources)-1:
                        print "did not find lyrics for this song, please request a new datasource"
                        sys.exit()
                    print "did not find lyric in data source, trying in the next one"

            mp3.cover = ds.grabAlbumCover(mp3.artist, mp3.album)

            files.append(mp3)
        for ds in dataSources:
            ds.quit()
        return files

    # filename = full path of the file.
    # (/path/to/your/music/folder/artist/album/file.mp3)
    def getDataFromFileName(self, fullpath):
        filepath = fullpath.split("/")[-1]
        albumpath = fullpath.split("/")[-2]

        track_num = filepath.partition("-")[0].strip()
        title = filepath.partition("-")[2].replace(".mp3", "").strip()
        artist = fullpath.split("/")[-3].strip()
        year = albumpath.partition("-")[2].strip()
        album = albumpath.partition("-")[0].strip()
        data = {"track_num": track_num,
            "title": title,
            "artist": artist,
            "year": year,
            "album": album
        }
        return data
