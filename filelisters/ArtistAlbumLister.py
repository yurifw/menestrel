from datasources import DataSource
import os
import Mp3File


class ArtistAlbumLister(object):

    def listFiles(self):
        albumPath = raw_input("enter the absolute path to your album folder:\n")
        files = []
        dataSource = DataSource.getInstance(2)
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
            mp3.lyrics = dataSource.grabLyric(mp3.artist, mp3.title)
            mp3.cover = dataSource.grabAlbumCover(mp3.artist, mp3.album)

            files.append(mp3)
        dataSource.quit()
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
