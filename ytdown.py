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
                print("Downloaded " , title,"\n")
        except:
                print("Enter vaild input!",'\n')

def audio_download(link):
        yt = YouTube(link)
        title = yt.title
        try:
                try:
                        stream = yt.streams.get_by_itag(140)
                        stream.download()
                        print("Downloaded " , title ,'\n')
                except:
                        stream = yt.streams.get_by_itag(139)
                        stream.download()
                        print("Downloaded " , title ,'\n' )
        except:
                print("Failed!", '\n')

def welcome():
    user_name = os.getlogin()
    time = datetime.datetime.now().hour
    if time <= 12 and time >= 5:
        print('Good morning,')
    elif time <= 17 and time >= 12:
        print('Good afternoon,')
    elif time <= 23 and time >= 17:
        print('Good evening,')
    print(str(user_name))

exit = False

def help():
        help_file = open('help.txt','r')
        print(help_file.read())

def menu():
        exit = False
        while exit == False:
                user_cmd = input('Enter your command: ').split(' ')
                if user_cmd[0].lower() == ("video"):
                        res = input('Enter resolution: ')
                        video_download(user_cmd[1],res)
                elif user_cmd[0].lower() == ("audio"):
                        audio_download(user_cmd[1])
                elif user_cmd[0].lower() == ('help'):
                        help()
                elif user_cmd[0].lower() == ('exit') or user_cmd[0].lower() == ('quit'):
                        exit = True
                else:
                        print("Invaild input! ")

welcome()
menu()
