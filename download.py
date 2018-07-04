import pafy
import time

def clearScreen():
    print(25 * "\n")


def getVideos():
    urlVideo = input("Ingresa el url del video de Youtube: ")
    video = pafy.new(urlVideo)
    bestVideo = video.getbest()

    # print("Titulo del Video\n{}\nResolución\n{}\nTamaño del archivo\n{}".format(), video.title)
    print("\n\nDatos del Video:\n{}\n{} {}\n{:0,} bytes".format(video.title, bestVideo.resolution, bestVideo.extension, bestVideo.get_filesize()))
    # print("Resolución\n", bestVideo.resolution, " Extension: ", bestVideo.extension)
    # print("Tamaño del archivo: ", bestVideo.get_filesize())
    print("")

    ask = input("Desea descargar el video? (y/n): ")
    if (ask == "y"):
        # bestVideo = video.getbest(preftype="mp4")
        bestVideo.download()


def getPlaylists():
    urlPlaylist = input("Ingresa la url de la Playlist: ")
    playlist = pafy.get_playlist(urlPlaylist)

    print("Titulo de la Playlist: ", playlist["title"])
    print("Playlist con ", len(playlist["items"]), " videos")
    print("1. Ver la lista de videos")
    print("2, Descargar todos los videos")
    askAction = input("Que opción que desea? ")
    contador = 1
    if askAction == "1":
        for i in playlist["items"]:
            bestVideo = i["pafy"].getbest()
            print("Titulo del Video # ", contador, ": ", i["pafy"].title)
            print("Resolución: ", bestVideo.resolution, " Extension: ", bestVideo.extension)
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
    askProcess = input("Desea procesar una URL (y/n): ")
    if (askProcess == "y"):
        askTypeUrl = input("Video o Playlist? (v/p)")
        clearScreen()
        if (askTypeUrl == "v"):
            getVideos()
        elif (askTypeUrl == "p"):
            getPlaylists()
        else:
            print("Opción erronea!!!")
            time.sleep(5)
    else:
        clearScreen()
        print("0k, chao...!")
        ciclo = False
