import pafy
import time

from color import *


def clearScreen():
    print(25 * "\n")


def getVideos(pUrl):
    video = pafy.new(pUrl)
    bestVideo = video.getbest()

    print(colorize(40, 1, 37, "\n\nDatos del Video:\n{}\n{} {}\n{:0,} bytes.\n\n".format(video.title, bestVideo.resolution, bestVideo.extension, bestVideo.get_filesize())))

    ask = input("Desea descargar el video? (s/n): ")
    if (ask == "s"):
        # bestVideo = video.getbest(preftype="mp4")
        bestVideo.download()


def getPlaylists(pUrl):
    playlist = pafy.get_playlist(pUrl)

    print("Titulo de la Playlist: ", playlist["title"])
    print("Playlist con ", len(playlist["items"]), " videos")
    print("1. Ver la lista de videos")
    print("2, Descargar todos los videos")
    askAction = input("Que opción que desea? ")
    contador = 1
    if askAction == "1":
        for i in playlist["items"]:
            # bestVideo = i["pafy"].getbest()
            print("Video ", contador, ": \n", i["pafy"].title)
            # print("Resolución: ", bestVideo.resolution, " Extension: ", bestVideo.extension)
            contador += 1

        time.sleep(5)
    elif askAction == "2":
        for i in playlist["items"]:
            bestVideo = i["pafy"].getbest()
            print("Titulo del Video # ", contador, ": ", i["pafy"].title)
            print("Resolución: ", bestVideo.resolution, " Extension: ", bestVideo.extension)
            print("Tamaño del archivo: ", bestVideo.get_filesize())
            print("")
            bestVideo.download()
            contador += 1


ciclo = True
while ciclo:
    clearScreen()
    urlVideo = input("Ingresa el url del video de Youtube: ")
    if urlVideo == "":
        askProcess = input("La url esta vacia, quiere abandonar el aplicativo? (s/n) ")
        if askProcess == "s":
            clearScreen()
            print(colorize(40, 0, 37, "0k, chao pues...!"))
            ciclo = False
    else:
        if "/playlist?list=" in urlVideo:
            getPlaylists(urlVideo)
        else:
            getVideos(urlVideo)
