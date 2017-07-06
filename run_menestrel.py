from filelisters import FileLister
from id3setters.Eyed3Setter import Eyed3Setter

print "I am the Menestrel, and I'm here to help you"
print "if you find any bugs, go to the project page https://github.com/yurifw/menestrel and create an issue"
print "btw, you should do the same thing if you want to request a feature"
print "now let's get started"
print "---------------------"

lister = FileLister.FileLister()
files = lister.list()
setter = Eyed3Setter()
print "saving the new tags to the files"
for file in files:
    setter.setTags(file)
print "Seems like everything went ok, see you next time !"