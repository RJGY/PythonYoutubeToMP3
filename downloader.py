import pafy
import os
import requests
import pytube


# this uses pytube to download
def downloadvideoaudio(videoURL, downloadfolder="\\tempDownload\\", relative=True, extra=True):
    dict = {}
    try:
        video = pytube.YouTube(videoURL)
    except pytube.exceptions.RegexMatchError:
        print("Invalid URL. Exiting.")
        return None
    # 251 is the iTag for the highest quality audio.
    audiostream = video.streams.get_by_itag(251)

    # Download video.
    if relative:
        dict["path"] = os.getcwd() + downloadfolder + audiostream.title.replace(".", "").replace(",", "").replace("'",
            "").replace("|", "").replace("/", "") + ".webm"
        audiostream.download(os.getcwd() + downloadfolder)
    else:
        dict["path"] = downloadfolder + audiostream.title.replace(".", "").replace(",", "").replace("'",
            "").replace("|", "").replace("/", "") + ".webm"
        audiostream.download(downloadfolder)

    # Add extra information to dictionary to be assigned by converter.
    if extra:
        if "-" in video.title:
            dict["artist"] = video.title.split("-", 1)[0]
            dict["title"] = video.title.split("-", 1)[1]
        else:
            dict["artist"] = video.title
            dict["title"] = video.title
        try:
            dict["thumb"] = downloadcover(video.thumbnail_url, video.title, downloadfolder, relative)
        except pytube.exceptions.RegexMatchError or KeyError["assets"]:
            print("Unable to download thumbnail. Skipping.")
            dict["thumb"] = None
        dict["album"] = video.author
    return dict


def playlist(playlistURL, startingindex=None, endingindex=None):
    print("Downloading URLS")
    # Variables
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
        print("Starting index is not of type int. Exiting playlist function.")
        return
    if startingindex < 0:
        startingindex = 0

    # Creates a list of YouTube URLS from the playlist.
    print("Starting Download")
    for i in range(startingindex, endingindex):
        playlistURLs.append("https://www.youtube.com/watch?v=" + playlistVideos[i].videoid)
        # Debug statement.
        print(str(i))
    return playlistURLs


def downloadcover(thumb, covername, downloadfolder, relative):
    # Changes folder path if relative or not.
    if relative:
        downloadfolder = os.getcwd() + downloadfolder
    # Use requests to download the image.
    img_data = requests.get(thumb).content
    # Download it to a specific folder with a specific name.
    with open((downloadfolder + covername + ".jpeg").replace("|", "").replace("\"", "").replace("/", "_"), 'wb') as handler:
        handler.write(img_data)
    # Return download location.
    return (downloadfolder + covername + ".jpeg").replace("|", "").replace("\"", "").replace("/", "_")
