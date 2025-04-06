import os,datetime,sys,ffmpeg
from pytubefix import YouTube , Playlist

def menu_0():
	if len(sys.argv) == 4:
		if sys.argv[1].lower() == 'video' or sys.argv[1].lower() == '1':
			video_download(sys.argv[2], sys.argv[3])
		elif sys.argv[1].lower() == 'audio' or sys.argv[1].lower() == '2':
			audio_download(sys.argv[2], sys.argv[3])
		elif sys.argv[1].lower() == "playlist_video" or sys.argv[1].lower() == '3':
			playlist_video(sys.argv[2], sys.argv[3])
		elif sys.argv[1].lower() == "playlist_audio" or sys.argv[1].lower() == "4":
			playlist_audio(sys.argv[2], sys.argv[3])
		elif sys.argv[1].lower() == "itag" or sys.argv[1].lower() == '5':
			get_by_itag(sys.argv[2], sys.argv[3])
	else:
		print('Invalid option!')
		help()
		
def menu():
	print('1) Video \n2) Audio \n3) Playlist_vido \n4) Playlist_audio only \n5) itag')
	user_input = str(input("File Type: "))
	link = input('Link: ')
	if user_input == "itag" or user_input == '5':
		quality = input('itag: ')
	else:
		print('1) High \n2) Medium \n3) Low')
		quality = input('Quality: ')
	if user_input == 'Video' or user_input == '1':
		video_download(link, quality)
	elif user_input == 'Audio' or user_input == '2':
		audio_download(link, quality)
	elif user_input == "Playlist_video" or user_input == '3':
		playlist_video(link, quality)
	elif user_input == "Playlist_audio" or user_input == "4":
		playlist_audio(link, quality)
	elif user_input == "itag" or user_input == '5':
		get_by_itag(link, quality)
	else:
		print('Invalid option!')
		help()

def help():
	file_name = sys.argv[0]
	print("\n Usage: python3 " + file_name + " < video / audio / playlist_video / playlist_audio > [URL ..] <quality> \n")
	print('Example to download video - \n python3 ' + file_name + ' video https://www.youtube.com/watch?v=dQw4w9WgXcQ high\n')
	print('Example to download audio - \n python3 ' + file_name + ' audio https://www.youtube.com/watch?v=dQw4w9WgXcQ high\n')
	print('Example to download playlist - \n python3 ' + file_name + ' playlist_video https://www.youtube.com/watch?v=dQw4w9WgXcQ high \n python3 ' + file_name + ' playlist_audio https://www.youtube.com/watch?v=dQw4w9WgXcQ high \n')
	print("Example to download using itag - \n python3 " + file_name + ' itag N https://www.youtube.com/watch?v=dQw4w9WgXcQ \n where N is this Itag number , itag list file is already uploaded check that for your reference' )
    
def audio_download(link , quality):    
	yt = YouTube(link)
	title = yt.title
	try:
		if quality.lower() == ("high") or quality == '1':
			quality_select = yt.streams.get_by_itag(251)
		elif quality.lower() == ("low") or quality == '3':
			quality_select = yt.streams.get_by_itag(139)
		elif quality.lower() == ('medium') or quality == '2':
			quality_select = yt.streams.get_by_itag(140)
		print("Initiating audio download")
		out_file = quality_select.download()
		base, ext = os.path.splitext(out_file)
		ffmpeg.input(out_file).output(base + '.m4a', acodec='aac').run()
		print("Downloaded ", title, "\n")
	except:
		print("Failed , Try different quality audio")
		
def video_download(link, res):
	yt = YouTube(link)
	title = yt.title
	try:
		if res.lower() == ("high") or res == ("1"):
			reso_select = yt.streams.get_by_itag(22)
		elif res.lower() == ("low") or res == ("3"):
			reso_select = yt.streams.get_by_itag(17)
		elif res.lower() == ('medium') or res == ("2"):
			reso_select = yt.streams.get_by_itag(18)
		print("Initiating video download")
		reso_select.download()
		print("Downloaded ", title, "\n")
	except:
		print("Failed, try diffrent resolution.")

def playlist_video(link , res):
	try:
		if res.lower() == ("high") or res == '1':
			itag = 22
		elif res.lower() == ("low") or res == '3':
			itag = 17
		elif res.lower() == ('medium') or res == '2':
			itag = 18
		play = Playlist(link)
		print("Initiating audio download")
		for video in play.videos:
			video.streams.get_by_itag(itag).download()
		print('Downloaded! ')
	except:
		print("Failed, try diffrent resolution.")

def playlist_audio(link , res):
	try:
		if res.lower() == ("high") or res == '1':
			itag = 140
		elif res.lower() == ("low") or res == '3':
			itag = 139
		elif res.lower() == ('medium') or res == '2':
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
	try:
		print("Intiiating Download")
		yt.streams.get_by_itag(int(itag)).download()
		print("Downloaded ", yt.title, "\n")
	except:
		print('Failed , try with another itag !')
		
if len(sys.argv) == 1:
	menu()
else:
	menu_0()
