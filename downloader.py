import pafy
import os
from pytube import YouTube


# this uses pafy to download
def downloadvideoaudio(videoURL, downloadfolder="\\tempDownload\\"):
    audiostream = pafy.new(videoURL).getbestaudio()
    # Download
    audiostream.download(os.getcwd() + downloadfolder + audiostream.title.replace("/", "_").replace("'", "").replace("|", "") + "." + audiostream.extension, True)
    return os.getcwd() + downloadfolder + audiostream.title.replace("/", "_").replace("'", "").replace("|", "") + "." + audiostream.extension


# this uses pytube to download
def downloadvideoaudio2(videoURL, downloadfolder="\\tempDownload\\"):
    audiostream = YouTube(videoURL).streams.get_by_itag('251')
    # Download
    audiostream.download(os.getcwd() + downloadfolder)
    return os.getcwd() + downloadfolder + audiostream.title.replace(".", "").replace(",", "").replace("'", "") + ".webm"


def playlist(playlistURL, startingindex, endingindex):
    playlistURLs = []
    playlist = pafy.get_playlist2(playlistURL)
    if endingindex > len(playlist):
        endingindex = len(playlist)
    if startingindex < 0:
        startingindex = 0
    for i in range(startingindex, endingindex):
        playlistURLs.append("https://www.youtube.com/watch?v=" + playlist[i].videoid)
    return playlistURLs
