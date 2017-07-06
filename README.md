# Menestrel
A simple and extensible script to fetch your ID3 tags from the internet, to use it just run the file run_menestrel.py.
This scripts takes information from your directory structure and puts that info in MP3 tags, the information that can't be found in your folders, it scrapes the internet, so this script automatically sets all ID3 tags for you :)


#### What is an ID3 tag? And why should I care?
> "MP3 ID3 tagMP3 files usually contain track data embedded within the file in addition to the audio data. This additional data is contained in ID3 tags and typically include the track’s title, artist and album details. However, these tags are much more versatile and can also contain a lot of extra information about the file in question." [- Richard Farrar](http://www.richardfarrar.com/what-are-id3-tags-in-mp3-files/)

Don't know why **you** should care, **I** care because I like when my musics are organized and all the album art appears, also I like to read the lyrics sometimes, having them already set on the MP3 file is an extremely convenient way to do that, so I don't need an extra app or even internet connection to read them.


#### I used this script to set the tags, but I still can't read the lyrics / other tags !
If you didn't get any error messages, and your tags still don't appear, maybe your player don't support them, I *strongly* recommend [Rocket Player](https://play.google.com/store/apps/details?id=com.jrtstudio.AnotherMusicPlayer) for Android

The following ID3 tags are supported:
* Artist/Band Name
* Album Name
* Track Number
* Year (release year)
* Genre
* Lyrics
* Album Picture

The script currently supports scraping from the following websites:
* http://lyrics.wikia.com/wiki/Lyrics_Wiki

The Following directory structures are supported:
* /path_to_my_music_folder/{artist}/{album}-{year}/{track number}-{track title}.mp3

If your directories are in a different way, create an issue and I might adapt the script for you, also if none of the supported websites have the lyrics you are searching for create an issue and I'll probably add support from a new website. You should also create an issue if this script gets any info wrong :)


Here are a few print screens of how files looks like with and without the ID3 tags:
![With tags](https://i.imgur.com/QmOJwR0.jpg)

![Without tags](https://i.imgur.com/xgfyGIo.png)
