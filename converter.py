import os
import pydub


# This function converts any media file to an mp3.
# This function uses pydub.
def converttomp3(dictionary, conversionfolder="\\MP3s\\", relative=True):
    # Error checking in case downloader runs into an error.
    if not isinstance(dictionary, dict):
        return False

    # Error checking in case the path doesnt exist inside the dictionary
    if "path" not in dictionary:
        return False

    videofile = dictionary["path"]
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
    if "thumb" not in dictionary:
        song.export(path, format="mp3")
    else:
        song.export(path, format="mp3", cover=dictionary["thumb"], tags={"artist": dictionary["artist"], "title":
                    dictionary["title"], "album": dictionary["album"]})
    return True
