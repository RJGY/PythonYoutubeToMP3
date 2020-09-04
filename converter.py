from downloader import *
from pydub import AudioSegment
import pydub
import os


def convertm4atomp3(videofile, conversionFolder):
    logging.debug("Start of Conversion")
    mp3name = os.path.splitext(os.path.basename(videofile))[0] + ".mp3"
    song = AudioSegment.from_file(videofile, "webm")
    song.export(os.getcwd() + conversionFolder + mp3name, format="mp3")
    logging.debug("End of Conversion")


if __name__ == '__main__':
    # Test Now
    urlList = playlist(examplePlaylist)
    for video in urlList:
        # make a try catch whatever thingo
        try:
            convertm4atomp3(downloadvideoaudio(video))
        except pydub.exceptions.CouldntDecodeError:
            convertm4atomp3(downloadvideoaudio2(video))

    logging.debug("DONE")
