import os
import datetime
from pytube import YouTube
def video_download(link,res):
        yt = YouTube(link)
        title = yt.title
        try:
                if res.lower() == ("high"):
                        reso_select = yt.streams.get_by_itag(22)
                elif res.lower() == ("low"):
                        reso_select = yt.streams.get_by_itag(17)
                elif res.lower() == ('medium'):
                        reso_select = yt.streams.get_by_itag(18)
                reso_select.download()
                print("Downloaded " , title)
        except:
                print("Enter vaild input!")

def audio_download(link):
        yt = YouTube(link)
        title = yt.title
        try:
                try:
                        stream = yt.streams.get_by_itag(140)
                        stream.download()
                        print("Downloaded " , title)
                except:
                        stream = yt.streams.get_by_itag(139)
                        stream.download()
                        print("Downloaded " , title)
        except:
                print("Failed!")

def welcome():
    user_name = os.getlogin()
    time = datetime.datetime.now().hour
    if time <= 12 and time >= 5:
        print('Good morning,')
    elif time <= 17 and time >= 12:
        print('Good afternoon,')
    elif time <= 23 and time >= 17:
        print('Good evening,')
    print( user_name)

exit = False

welcome()

while exit == False:
    link = input('Paste your YouTube link here: ')
    if link.lower() == ('exit') or link.lower() == ('quit'):
        exit = True
        pass
    yt = YouTube(link)
    title = yt.title
    format = input("type v to download video and a to download audio: ")
    if format.lower() == ('exit') or format.lower() == ('quit'):
        exit = True
        pass
    if format.lower() == ('v'):
            res = input('Enter your resolution (low,high) #by default
its medium: ')
            print('Downloading ' ,title)
            video_download(link,res)
    if format.lower() == ('a'):
            print('Downloading ' , title)
            audio_download(link)
    else:
            print("Enter vaild input!")
