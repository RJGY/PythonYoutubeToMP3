import downloader
import converter
import pathcheck

downloader.pafy.set_api_key("AIzaSyCQyk6dS1nomkmGlPuK-zJc9CjGg6ziWFA")


def downloadandconvertplaylist(playlistURL, startingindex=None, endingindex=None, extra=True, downloadfolder="\\tempDownload\\", conversionfolder="\\MP3s\\", relative=True):
    pathcheck.pathexists(downloadfolder, relative)
    pathcheck.pathexists(conversionfolder, relative)
    videourls = downloader.playlist(playlistURL, startingindex, endingindex)
    for video in videourls:
        if not converter.converttomp3(downloader.downloadvideoaudio(video, downloadfolder, relative), conversionfolder,
                relative):
            print("First download method failed, attempting second method.")
            converter.converttomp3(downloader.downloadvideoaudio2(video, downloadfolder, relative), conversionfolder,
                    relative)
        pathcheck.clearcache(downloadfolder, relative)


if __name__ == '__main__':
    downloadandconvertplaylist("https://www.youtube.com/playlist?list=PLUDyUa7vgsQlEST5MYSqTmc03U0Mr_Ihc", 0, 10)
    print("DONE")