import pafy
import logging
import os
from pytube import YouTube

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s -  %(levelname)s -  %(message)s")
logging.debug("Start of Program.")

downloadfolder = '\\webms\\'
exampleVideo = r"https://www.youtube.com/watch?v=HS2idHXAKUU"
examplePlaylist = r"https://www.youtube.com/playlist?list=PLUDyUa7vgsQlEST5MYSqTmc03U0Mr_Ihc"
startingIndex = 564
pafy.set_api_key("AIzaSyCQyk6dS1nomkmGlPuK-zJc9CjGg6ziWFA")


# this uses pafy to download
def downloadvideoaudio(videoURL):
    logging.debug("Start of downloadvideo")
    audiostream = pafy.new(videoURL).getbestaudio() # YouTube(videoURL).streams.get_by_itag('251')
    # Download
    audiostream.download(os.getcwd() + downloadfolder + audiostream.title.replace("/", "_").replace("'", "").replace("|", "") + "." + audiostream.extension, True)
    logging.debug(audiostream.title)
    logging.debug("End of downloadvideo")
    return os.getcwd() + downloadfolder + audiostream.title.replace("/", "_").replace("'", "").replace("|", "") + "." + audiostream.extension


# this uses pytube to download
def downloadvideoaudio2(videoURL):
    logging.debug("Start of downloadvideo2")
    audiostream = YouTube(videoURL).streams.get_by_itag('251')
    # Download
    audiostream.download(os.getcwd() + downloadfolder)
    logging.debug("End of downloadvideo2")
    return os.getcwd() + downloadfolder + audiostream.title.replace(".", "").replace(",", "").replace("'", "") + ".webm"


def playlist(playlistURL):
    playlistURLs = []
    logging.debug("Start of playlist")
    playlist = pafy.get_playlist2(examplePlaylist)
    for i in range(len(playlist)):
        logging.debug("we are at index " + str(i))
        playlistURLs.append("https://www.youtube.com/watch?v=" + playlist[i].videoid)
    logging.debug("End of playlist")
    return playlistURLs


if __name__ == '__main__':
    # logging.debug(downloadvideoaudio(exampleVideo))
    logging.debug(YouTube(exampleVideo).streams)
    #playlist(examplePlaylist)


logging.debug("End of Program.")

