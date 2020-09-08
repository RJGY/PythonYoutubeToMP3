import os


def pathexists(dirpath, relative):
    if relative:
        dirpath = os.getcwd() + dirpath
    if os.path.isdir(dirpath):
        return
    else:
        try:
            os.mkdir(dirpath)
        except OSError:
            print("Creation of path failed. Exiting program.")
            exit()


def clearcache(dirpath, relative):
    if relative:
        dirpath = os.getcwd() + dirpath
    for file in os.listdir(dirpath):
        if os.path.isfile(dirpath + file):
            os.remove(dirpath + file)


def checkcache(dirpath, relative):
    if relative:
        dirpath = os.getcwd() + dirpath
    size = 0
    for folderpath, foldernames, filenames in os.walk(dirpath):
        for file in filenames:
            path = folderpath + file
            size += os.path.getsize(path)
    if size > 1000000000:
        return True
    return False


if __name__ == '__main__':
    print(checkcache("\\MP3s\\", True))