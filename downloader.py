import pafy
import os
import requests
import pytube


# This function uses pafy to download Youtube videos from the best audio it can get. This is
# normally in the form of webms.
def downloadvideoaudio(videoURL, downloadfolder="\\tempDownload\\", relative=True, extra=True):
    dict = {}
    try:
        video = pafy.new(videoURL)
    except ValueError:
        print("Invalid Youtube URL. Exiting.")
        return None
    except OSError:
        print("Unable to extract video data from Youtube. Exiting.")
        return None
    audiostream = video.getbestaudio()
    # Download video.
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

    # Add extra information to dictionary.
    if extra:
        if "-" in video.title:
            dict["artist"] = video.title.split("-", 1)[0]
            dict["title"] = video.title.split("-", 1)[1]
        thumburl = pytube.YouTube(videoURL).thumbnail_url
        dict["thumb"] = downloadcover(thumburl, video.title, downloadfolder, relative)
        dict["album"] = video.author
    return dict


# this uses pytube to download
def downloadvideoaudio2(videoURL, downloadfolder="\\tempDownload\\", relative=True, extra=True):
    dict = {}
    try:
        video = pytube.YouTube(videoURL)
    except pytube.exceptions.RegexMatchError:
        print("Invalid URL. Exiting.")
        return None
    audiostream = video.streams.get_by_itag(251)
    # Download video.
    if relative:
        dict["path"] = os.getcwd() + downloadfolder + audiostream.title.replace(".", "").replace(",", "").replace("'",
            "").replace("|", "") + ".webm"
        audiostream.download(os.getcwd() + downloadfolder)
    else:
        dict["path"] = downloadfolder + audiostream.title.replace(".", "").replace(",", "").replace("'",
            "").replace("|", "") + ".webm"
        audiostream.download(downloadfolder)

    # Add extra information to dictionary.
    if extra:
        if "-" in video.title:
            dict["artist"] = video.title.split("-", 1)[0].strip()
            dict["title"] = video.title.split("-", 1)[1].strip()
        dict["thumb"] = downloadcover(video.thumbnail_url, video.title, downloadfolder, relative)
        dict["album"] = video.author
    return dict


def playlist(playlistURL, startingindex=None, endingindex=None):
    print("Downloading URLS")
    playlistURLs = []
    playlistVideos = pafy.get_playlist2(playlistURL)

    # Error checking for indexes.
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

    # Creates a list of YouTube URLS from the playlist.
    print("Starting Download")
    for i in range(startingindex, endingindex):
        playlistURLs.append("https://www.youtube.com/watch?v=" + playlistVideos[i].videoid)
        print(str(i))
    return playlistURLs


def downloadcover(thumb, covername, downloadfolder, relative):
    # Changes folder path if relative or not.
    if relative:
        downloadfolder = os.getcwd() + downloadfolder
    # Use requests to download the image.
    img_data = requests.get(thumb).content
    # Download it to a specific folder with a specific name.
    with open((downloadfolder + covername + ".jpeg").replace("|", ""), 'wb') as handler:
        handler.write(img_data)
    # Return download location.
    return (downloadfolder + covername + ".jpeg").replace("|", "")
