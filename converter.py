from pydub import AudioSegment
import os


def converttomp3(videofile, conversionfolder=None, relative=True):
    mp3name = os.path.splitext(os.path.basename(videofile))[0] + ".mp3"
    song = AudioSegment.from_file(videofile, "webm")
    if relative:
        song.export(os.getcwd() + conversionfolder + mp3name, format="mp3")
    else:
        song.export(conversionfolder + mp3name, format="mp3")
