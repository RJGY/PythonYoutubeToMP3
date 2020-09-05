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
            print("Creation of path failed. Exiting prorgram.")
            exit()


def clearcache(dirpath, relative):
    if relative:
        dirpath = os.getcwd() + dirpath
    for file in os.listdir(dirpath):
        print(file)
        os.remove(dirpath + file)
