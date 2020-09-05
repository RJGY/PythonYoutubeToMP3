import pafy
import os
from pytube import YouTube


# this uses pafy to download
def downloadvideoaudio(videoURL, downloadfolder="\\tempDownload\\", relative=True):
    dict = {}
    audiostream = pafy.new(videoURL).getbestaudio()
    # Download
    if relative:
        audiostream.download(os.getcwd() + downloadfolder + audiostream.title.replace("/", "_").replace("'", "")
            .replace("|", "") + "." + audiostream.extension, True)
        dict["path"] = os.getcwd() + downloadfolder + audiostream.title.replace(".", "").replace(",", "").replace("'",
            "").replace("|", "") + audiostream.extension
    else:
        audiostream.download(
            downloadfolder + audiostream.title.replace("/", "_").replace("'",
            "").replace("|", "") + "." + audiostream.extension,
            True)
        dict["path"] = downloadfolder + audiostream.title.replace("/", "_").replace("'",
            "").replace("|", "") + "." + audiostream.extension
    return dict


# this uses pytube to download
def downloadvideoaudio2(videoURL, downloadfolder="\\tempDownload\\", relative=True):
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
    dict["artist"] = video.title.split("-", 1)[0]
    dict["thumb"] = video.thumbnail_url
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
        print("https://www.youtube.com/watch?v=" + playlistVideos[i].videoid + " " + str(i))
    return playlistURLs


