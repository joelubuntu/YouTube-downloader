import os
import datetime
import sys
from pytube import YouTube
from pytube import Playlist


def video_download(link, res):
    yt = YouTube(link)
    title = yt.title
    streams = yt.streams.filter(file_extension='mp4')
    try:
        if res.lower() == ("high"):
            reso_select = streams.get_by_itag(22)
        elif res.lower() == ("low"):
            reso_select = streams.get_by_itag(17)
        elif res.lower() == ('medium'):
            reso_select = streams.get_by_itag(18)
        print("Initiating video download")
        reso_select.download()
        print("Downloaded ", title, "\n")
    except:
        print("Failed, try diffrent resolution.")


def audio_download(link, quality):
    yt = YouTube(link)
    title = yt.title
    streams = yt.streams.filter(file_extension='mp3')
    try:
        if quality.lower() == ("high"):
            quality_select = streams.get_by_itag(251)
        elif quality.lower() == ("low"):
            quality_select = streams.get_by_itag(249)
        elif quality.lower() == ('medium'):
            quality_select = streams.get_by_itag(50)
        print("Initiating audio download")
        quality_select.download()
        print("Downloaded ", title, "\n")
    except:
        print("Failed , Try different quality audio")


def playlist(link, res):
    try:
        if res.lower() == ("high"):
            itag = 22
        elif res.lower() == ("low"):
            itag = 17
        elif res.lower() == ('medium'):
            itag = 18
        play = Playlist(link)
        print("Initiating playlist download")
        for video in play.videos:
            video.streams.filter(
                file_extension="mp4").get_by_itag(itag).download()
        print('Downloaded! ')
    except:
        print("Failed, try diffrent resolution.")


def welcome():
    user_name = os.getlogin()
    time = datetime.datetime.now().hour
    if time <= 12 and time >= 5:
        print('Good morning,', end=" ")
    elif time <= 17 and time >= 12:
        print('Good afternoon,', end=" ")
    elif time <= 23 and time >= 17:
        print('Good evening,', end=" ")
    print(str(user_name))


def help():
    print("\nUsage: python3 " +
          sys.argv[0] + " <video/audio> [URL ..] <resolution/quality>\n")
    print('Example to download video - \n    python3 ',
          sys.argv[0], ' video https://www.youtube.com/watch?v=dQw4w9WgXcQ high\n')
    print('Example to download audio - \n    python3 ',
          sys.argv[0], ' audio https://www.youtube.com/watch?v=dQw4w9WgXcQ medium\n')
    print('Example to download playlist - \n    python3 ',
          sys.argv[0], ' playlist https://www.youtube.com/watch?v=dQw4w9WgXcQ high\n')


def menu():
    if len(sys.argv) > 4 or len(sys.argv) < 4:
        help()
    elif sys.argv[1] == 'video':
        video_download(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'audio':
        audio_download(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "playlist":
        playlist(sys.argv[2], sys.argv[3])


welcome()
menu()
