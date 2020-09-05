from pydub import AudioSegment
import os
import pydub

def converttomp3(videofile, conversionfolder="\\MP3s\\", relative=True):
    mp3name = os.path.splitext(os.path.basename(videofile))[0] + ".mp3"
    extension = os.path.splitext(os.path.basename(videofile))[1].replace(".", "")
    # pydub.exceptions.CouldntDecodeError
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

# TODO - # add album art, add channel name as artist

def addextras():
    print("LOL")
