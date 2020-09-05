from pydub import AudioSegment
import os
import pydub


def converttomp3(videofile, conversionfolder="\\MP3s\\", relative=True, extra=True):
    mp3name = os.path.splitext(os.path.basename(videofile))[0] + ".mp3"
    extension = os.path.splitext(os.path.basename(videofile))[1].replace(".", "")
    try:
        song = AudioSegment.from_file(videofile, format=extension)
    except pydub.exceptions.CouldntDecodeError:
        return False
    if relative:
        print(os.getcwd() + conversionfolder + mp3name)
        song.export(os.getcwd() + conversionfolder + mp3name, format="mp3")
    else:
        song.export(conversionfolder + mp3name, format="mp3")
    return True


def extratags(videooffile):
    print("Not yet implemented")