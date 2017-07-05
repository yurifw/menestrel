from DataSource import LyricsSource
from selenium import webdriver
from selenium.common import exceptions

class DarkLyricsSource(LyricsSource):
    def grabLyric(self, artist, title):
        url = "http://www.darklyrics.com/"
        return "Letra"