import pafy
import os
import requests
from pytube import YouTube


# this uses pafy to download
def downloadvideoaudio(videoURL, downloadfolder="\\tempDownload\\", relative=True, extra=True):
    dict = {}
    video = pafy.new(videoURL)
    audiostream = video.getbestaudio()
    # Download
    if relative:
        audiostream.download(os.getcwd() + downloadfolder + audiostream.title.replace("/", "_").replace("'", "")
            .replace("|", "") + "." + audiostream.extension, True)
        dict["path"] = os.getcwd() + downloadfolder + audiostream.title.replace("/", "_").replace("'", "")\
            .replace("|", "") + "." + audiostream.extension
    else:
        audiostream.download(
            downloadfolder + audiostream.title.replace("/", "_").replace("'",
            "").replace("|", "") + "." + audiostream.extension,
            True)
        dict["path"] = downloadfolder + audiostream.title.replace("/", "_").replace("'",
            "").replace("|", "") + "." + audiostream.extension
    if extra:
        dict["artist"] = video.title.split("-", 1)[0]
        dict["thumb"] = downloadcover(video.bigthumbhd, video.title, downloadfolder, relative)
        dict["title"] = video.title.split("-", 1)[1]
        dict["album"] = video.author
    return dict


# this uses pytube to download
def downloadvideoaudio2(videoURL, downloadfolder="\\tempDownload\\", relative=True, extra=True):
    dict = {}
    video = YouTube(videoURL)
    audiostream = video.streams.get_by_itag(251)
    # Download
    if relative:
        dict["path"] = os.getcwd() + downloadfolder + audiostream.title.replace(".", "").replace(",", "").replace("'",
            "").replace("|", "") + ".webm"
        audiostream.download(os.getcwd() + downloadfolder)
    else:
        dict["path"] = downloadfolder + audiostream.title.replace(".", "").replace(",", "").replace("'",
            "").replace("|", "") + ".webm"
        audiostream.download(downloadfolder)
    if extra:
        dict["artist"] = video.title.split("-", 1)[0]
        dict["thumb"] = downloadcover(video.thumbnail_url, video.title, downloadfolder, relative)
        dict["title"] = video.title.split("-", 1)[1]
        dict["album"] = video.author
    return dict


def playlist(playlistURL, startingindex=None, endingindex=None):
    print("Downloading URLS")
    playlistURLs = []
    playlistVideos = pafy.get_playlist2(playlistURL)
    if endingindex is None:
        endingindex = len(playlistVideos)
    if not isinstance(endingindex, int):
        print("something went wrong with ending index")
        return
    if endingindex > len(playlistVideos):
        endingindex = len(playlistVideos)
    if startingindex is None:
        startingindex = 0
    if not isinstance(startingindex, int):
        print("something went wrong with startingindex")
        return
    if startingindex < 0:
        startingindex = 0
    print("Starting Download")
    for i in range(startingindex, endingindex):
        playlistURLs.append("https://www.youtube.com/watch?v=" + playlistVideos[i].videoid)
        print(str(i))
    return playlistURLs


def downloadcover(thumb, covername, downloadfolder, relative):
    if relative:
        downloadfolder = os.getcwd() + downloadfolder
    img_data = requests.get(thumb).content
    with open(downloadfolder + covername + ".jpeg", 'wb') as handler:
        handler.write(img_data)
    return downloadfolder + covername + ".jpeg"
