import downloader
import converter
import pathcheck
import youtube_dl

downloader.pafy.set_api_key("AIzaSyCQyk6dS1nomkmGlPuK-zJc9CjGg6ziWFA")


# Function which allows users to download a whole playlist.
def downloadandconvertplaylist(playlistURL, startingindex=None, endingindex=None, extra=True, downloadfolder="\\tempDownload\\", conversionfolder="\\MP3s\\", relative=True):
    # Check if path exists for parsed variables.
    pathcheck.pathexists(downloadfolder, relative)
    pathcheck.pathexists(conversionfolder, relative)
    videourls = downloader.playlist(playlistURL, startingindex, endingindex)
    count = 0
    # Iterate through video urls.
    for video in videourls:
        # If one of the downloaders are unable to download the song, use the other download method.
        if not converter.converttomp3(downloader.downloadvideoaudio(video, downloadfolder, relative, extra), conversionfolder,
                relative):
            print("First download method failed, attempting second method.")
            converter.converttomp3(downloader.downloadvideoaudio2(video, downloadfolder, relative, extra), conversionfolder,
                    relative)
        count += 1
        if count % 100 == 0:
            if pathcheck.checkcache(downloadfolder, relative):
                pathcheck.clearcache(downloadfolder, relative)
    pathcheck.clearcache(downloadfolder, relative)


def downloadandconvertsong(songurl, extra=True, downloadfolder="\\tempDownload\\", conversionfolder="\\MP3s\\", relative=True):
    pathcheck.pathexists(downloadfolder, relative)
    pathcheck.pathexists(conversionfolder, relative)
    # If one of the downloaders are unable to download the song, use the other download method.
    if not converter.converttomp3(downloader.downloadvideoaudio(songurl, downloadfolder, relative, extra), conversionfolder,
                                  relative):
        print("First download method failed, attempting second method.")
        converter.converttomp3(downloader.downloadvideoaudio2(songurl, downloadfolder, relative, extra), conversionfolder,
                               relative)
    # Clear the cache after downloading the song.
    pathcheck.clearcache(downloadfolder, relative)


# Function for UI.
def start():
    loop = True
    while loop:
        print("What would you like to do: ")
        print("Download a single song (simple):     1")
        print("Download a single song (advanced):   2")
        print("Download a playlist (simple):        3")
        print("Download a playlist (advanced):      4")
        print("Exit:                                5")
        user = input("Enter a number: ")
        try:
            user = int(user)
        except ValueError:
            print("Please enter a number.")
        except:
            print("Don't know what happened.")
            exit(1)
        if user == 1:
            videourl = input("Enter the YouTube video URL: ")
            downloadandconvertsong(videourl)
        elif user == 2:
            videourl = input("Enter the YouTube video URL: ")
            downloadandconvertsong(videourl, bool(input("Enter whether or not you want extra tags (eg. True/False): ")),
                    input("Enter the path to the temporary download folder (eg. /Downloads/PythonTemp/): "),
                    input("Enter the path to the folder which will store the MP3 files. Ensure this is a different"
                          " folder to the temporary download folder. (eg. /Downloads/PythonMP3s/): "),
                    bool(input("Enter whether or not you are referencing the paths relatively or their absolute paths "
                               "(eg. True/False): ")))
        elif user == 3:
            playlisturl = input("Enter the YouTube playlist URL: ")
            downloadandconvertplaylist(playlisturl)
        elif user == 4:
            playlisturl = input("Enter the YouTube playlist URL: ")
            downloadandconvertplaylist(playlisturl, int(input("Enter the index of where you wish to start downloading "
                                                              "from (eg. a number, 0, 1, 2, etc.): ")),
                    int(input("Enter the index of where you wish to stop downloading to (eg. a number, 10, 11, 12, etc.): ")),
                    bool(input("Enter whether or not you want extra tags (eg. True/False): ")),
                    input("Enter the path to the temporary download folder (eg. /Downloads/PythonTemp/): "),
                    input("Enter the path to the folder which will store the MP3 files. Ensure this is a different"
                          " folder to the temporary download folder. (eg. /Downloads/PythonMP3s/): "),
                    bool(input("Enter whether or not you are referencing the paths relatively or their absolute paths "
                               "(eg. True/False): ")))
        elif user == 5:
            exit(0)
        else:
            print("Functionality doesnt exist!")

# TODO - Make code run without python with py2exe or Cython. The exe will also need to install ffmpeg and set the path.
#  That's a lot of work...


start()
