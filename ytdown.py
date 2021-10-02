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

def playlist_audio(link, res):
    try:
        if res.lower() == ("high"):
            itag = 251
        elif res.lower() == ("low"):
            itag = 249
        elif res.lower() == ('medium'):
            itag = 50
        play = Playlist(link)
        print("Initiating playlist download")
        for video in play.videos:
            video.streams.filter(
                file_extension="mp3").get_by_itag(itag).download()
        print('Downloaded! ')
    except:
        print("Failed, try diffrent resolution.")


def playlist_video(link, res):
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
    print(f'''Usage: python3 {sys.argv[0]} + " <video/audio> [URL ..] <resolution/quality> [mp3/mp4]\n")
Examples:
To download video -
python3 {sys.argv[0]} video https://www.youtube.com/watch?v=dQw4w9WgXcQ high\n
To download audio -
python3 {sys.argv[0]} audio https://www.youtube.com/watch?v=dQw4w9WgXcQ medium\n
To download playlist as video-
python3 {sys.argv[0]} playlist video https://www.youtube.com/playlist?list=PL6rBC_87VKs76V9Vc0s44Gg_Q6qObZrFY high''')


def menu():
    if not 4 <= len(sys.argv) <= 5:
        help()
    elif sys.argv[1].lower() == 'video':
        video_download(sys.argv[2], sys.argv[3])
    elif sys.argv[1].lower() == 'audio':
        audio_download(sys.argv[2], sys.argv[3])
    elif sys.argv[1].lower() == "playlist":
        if sys.argv[2].lower() == 'video':
            playlist_video(sys.argv[3], sys.argv[4])
        if sys.argv[2].lower() == 'audio':
            playlist_audio(sys.argv[3], sys.argv[4])
    else:
        print('Invalid option!')
        exit()

welcome()
menu()
