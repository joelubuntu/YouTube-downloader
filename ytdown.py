import os
import datetime
import sys
from pytube import YouTube
from pytube import Playlist
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
		print("Failed, try diffrent resolution.")

def audio_download(link,quality):
	yt = YouTube(link)
	title = yt.title
	try:
		if quality.lower() == ("high"):
			quality_select = yt.streams.get_by_itag(251)
		elif quality.lower() == ("low"):
			quality_select = yt.streams.get_by_itag(249)
		elif quality.lower() == ('medium'):
			quality_select = yt.streams.get_by_itag(50)
		quality_select.download()
		print("Download " , title , "\n")
	except:
		print("Failed , Try different quality audio")

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

def help():
	print("Usage: python3 " + sys.argv[0] + " <video/audio> [URL ..] <resolution/quality>")
	print('Example to download video - \n python3 ' , sys.argv[0] , ' video https://www.youtube.com/watch?v=dQw4w9WgXcQ high')
	print('Example to download audio - \n python3 ' , sys.argv[0] , ' audio https://www.youtube.com/watch?v=dQw4w9WgXcQ high')
	print('Example to download playlist - \n python3 ' , sys.argv[0] , ' playlist https://www.youtube.com/watch?v=dQw4w9WgXcQ high')

def playlist(link,res):
	try:
		if res.lower() == ("high"):
			itag = 22
		elif res.lower() == ("low"):
			itag = 17
		elif res.lower() == ('medium'):
			itag = 18
		play = Playlist(link)
		for video in play.videos:
			video.streams.get_by_itag(itag).download()
		print('Downloaded! ')
	except:
		print("Failed, try diffrent resolution.")

def menu():
	if len(sys.argv) > 4 or len(sys.argv) < 4:
		help()
	if sys.argv[1] == 'video':
		video_download(sys.argv[2],sys.argv[3])
	elif sys.argv[1] == 'audio':
		audio_download(sys.argv[2],sys.argv[3])
	elif sys.argv[1] == "playlist":
		playlist(sys.argv[2],sys.argv[3])

welcome()
menu()
