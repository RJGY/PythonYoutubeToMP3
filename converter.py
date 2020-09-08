import os
import pydub


def converttomp3(dict, conversionfolder="\\MP3s\\", relative=True):
    if "path" not in dict:
        return
    videofile = dict["path"]
    mp3name = os.path.splitext(os.path.basename(videofile))[0] + ".mp3"
    extension = os.path.splitext(os.path.basename(videofile))[1].replace(".", "")
    try:
        song = pydub.AudioSegment.from_file(videofile, format=extension)
    except pydub.exceptions.CouldntDecodeError:
        return False
    if relative:
        path = os.getcwd() + conversionfolder + mp3name
    else:
        path = conversionfolder + mp3name
    if "thumb" not in dict:
        song.export(path, format="mp3")
    else:
        song.export(path, format="mp3", cover=dict["thumb"], tags={"artist": dict["artist"], "title": dict["title"],
                                                                   "album": dict["album"]})
    return True
