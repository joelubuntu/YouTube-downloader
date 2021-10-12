from pytube import YouTube , Playlist
import datetime
import os
import sys

def menu():
	if len(sys.argv) == 4:
		if sys.argv[1].lower() == 'video':
			video_download(sys.argv[2], sys.argv[3])
		elif sys.argv[1].lower() == 'audio':
			audio_download(sys.argv[2], sys.argv[3])
		elif sys.argv[1].lower() == "playlist_video":
			playlist_video(sys.argv[2], sys.argv[3])
		elif sys.argv[1].lower() == "playlist_audio":
			playlist_audio(sys.argv[2], sys.argv[3])
		elif sys.argv[1].lower() == "itag":
			get_by_itag(sys.argv[2], sys.argv[3])
	else:
		print('Invalid option!')
		help()

def help():
	file_name = sys.argv[0]
	print("\n Usage: python3 " + file_name + "< video / audio / playlist_video / playlist_audio > [URL ..] <quality> \n")
	print('Example to download video - \n python3 ' + file_name + 'ytdown.py video https://www.youtube.com/watch?v=dQw4w9WgXcQ high\n')
	print('Example to download audio - \n python3 ' + file_name + 'audio https://www.youtube.com/watch?v=dQw4w9WgXcQ high\n')
	print('Example to download playlist - \n python3 ' + file_name + 'playlist_video https://www.youtube.com/watch?v=dQw4w9WgXcQ high \n python3 ' + file_name + ' playlist_audio https://www.youtube.com/watch?v=dQw4w9WgXcQ high')
	print("Example to download using itag - \n python3 " + file_name + 'itag N https://www.youtube.com/watch?v=dQw4w9WgXcQ \n where N is this Itag number , itag list file is already uploaded check that for your reference' )
	
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
    
    
def audio_download(link , quality):    
	yt = YouTube(link)
	title = yt.title
	try:
		if quality.lower() == ("high"):
			quality_select = yt.streams.get_by_itag(140)
		elif quality.lower() == ("low"):
			quality_select = yt.streams.get_by_itag(139)
		elif quality.lower() == ('medium'):
			quality_select = yt.streams.get_by_itag(139)
		print("Initiating audio download")
		out_file = quality_select.download()
		base, ext = os.path.splitext(out_file)
		new_file = base + '.mp3'
		os.rename(out_file, new_file)
		print("Downloaded ", title, "\n")
	except:
		print("Failed , Try different quality audio")
		
def video_download(link, res):
	yt = YouTube(link)
	title = yt.title
	try:
		if res.lower() == ("high"):
			reso_select = yt.streams.get_by_itag(22)
		elif res.lower() == ("low"):
			reso_select = yt.streams.get_by_itag(17)
		elif res.lower() == ('medium'):
			reso_select = yt.streams.get_by_itag(18)
		print("Initiating video download")
		reso_select.download()
		print("Downloaded ", title, "\n")
	except:
		print("Failed, try diffrent resolution.")

def playlist_video(link , res):
	try:
		if res.lower() == ("high"):
			itag = 22
		elif res.lower() == ("low"):
			itag = 17
		elif res.lower() == ('medium'):
			itag = 18
		play = Playlist(link)
		print("Initiating audio download")
		for video in play.videos:
			video.streams.get_by_itag(itag).download()
		print('Downloaded! ')
	except:
		print("Failed, try diffrent resolution.")

def playlist_audio(link , quality):
	try:
		if res.lower() == ("high"):
			itag = 140
		elif res.lower() == ("low"):
			itag = 139
		elif res.lower() == ('medium'):
			itag = 139
		play = Playlist(link)
		print("Initiating audio download")
		for video in play.videos:
			out_file = video.streams.get_by_itag(itag).download()
			base, ext = os.path.splitext(out_file)
			new_file = base + '.mp3'
			os.rename(out_file, new_file)
		print('Downloaded! ')
	except:
		print("Failed, try diffrent quality.")

def get_by_itag(itag , link):
	yt = YouTube(link)
	title = yt.title
	try:
		print("Intiiating Download")
		yt.streams.get_by_itag(int(itag)).download()
	except:
		print('Failed , try with another itag !')
		
welcome()
menu()

#last updated on 12th OCT 2021
