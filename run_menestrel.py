from datasources import LyricsWikiaSource
from filelisters import FileLister
from id3setters.Eyed3Setter import Eyed3Setter


lister = FileLister.FileLister()
files = lister.list()
setter = Eyed3Setter()
for file in files:
    setter.setTags(file)




# mp3 = {"path":"/var/www/html/tagger/Deep Purple/Shades Of Deep Purple - 1968/02 - Hush.mp3", "artist":"Deep Purple", "title":"Hush", "album":"Shades of Grey", "track_num":"02",
#                "year":"1968","genre":"Rock", "lyrics":"Lyrics of Hush", "cover":"isso vai bugar"}
# setter.setTags(mp3)