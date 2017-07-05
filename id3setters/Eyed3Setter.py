from Id3Setter import Id3Setter
import eyed3

class Eyed3Setter(Id3Setter):

    def setTags(self, file):
        track = eyed3.load(file.path)
        track.tag.artist = unicode(file.artist)
        track.tag.title = unicode(file.title)
        track.tag.album = unicode(file.album)
        track.tag.track_num = int(file.track_num)
        track.tag.year = unicode(file.year)
        track.tag.genre = unicode(file.genre)
        track.tag.lyrics.set(unicode(file.lyrics))
        track.tag.images.set(3,file.cover,"image/jpeg")
        track.tag.save()

        #read lyrics:
        # print  u"".join([i.text for i in track.tag.lyrics])
