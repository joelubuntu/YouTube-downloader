import os , platform , datetime , sys
try:
	from pytube import YouTube , Playlist
except:
	if platform.system() == 'Windows':
		os.system("pip intall pytube")
	if platform.system() == 'Linux':
		os.system("pip3 intall pytube")
from tkinter import *

def video_download(link,quality):
	video_root = Tk()
	if quality == "144p":
		itag = 17
	elif quality == "240p":
		itag = 133
	elif quality == "360p":
		itag = 18
	elif quality == "480p":
		itag = 135
	elif quality == "720p":
		itag = 22
	elif quality == '1080p':
		itag = 137
	elif quality == "1440p":
		itag = 400
	try:
		yt = YouTube(link)
		title = yt.title
		reso_select = yt.streams.get_by_itag(itag)
		downloading_label = Label(video_root,text="Initiating video download").pack()
		reso_select.download()
		text1 = "Downloaded ", title, "\n"
		donwloaded = Label(video_root,text=text1).pack()
	except:
		error_label = Label(video_root,text="Failed, try diffrent resolution.").pack()
	video_root.mainloop()

def audio_download(link,quality):
	audio_root = Tk()
	if quality == "Low":
		itag = 139
	elif quality == "Medium":
		itag = 140
	elif quality == "High":
		itag = 251
	yt = YouTube(link)
	title = yt.title
	try:
		quality_select = yt.streams.get_by_itag(itag)
		downloading = Label(audio_root,text="Initiating audio download").pack()
		out_file = quality_select.download()
		"""base, ext = os.path.splitext(out_file)
		new_file = base + '.mp3'
		os.rename(out_file, new_file)"""
		text1 = "Downloaded ", title, "\n"
		downloaded = Label(audio_root,text=text1).pack()
	except:
		print("Failed , Try different quality audio")
	audio_root.mainloop()

root = Tk()
root.iconbitmap("C:/Users/avguser1.DESKTOP-N4DIB48/Downloads/youtube.ico")
root.title("Youtube Downloader.")


time = datetime.datetime.now().hour
if time <= 12 and time >= 5:
	time1 = ('Good Morning')
elif time <= 17 and time >=12:
	time1 = ("Good Afternoon")
elif time <= 23 and time >= 17:
	time1 = ("Good Evening")
greet_text = str(time1 + ' , ' + os.getlogin())
home_screen = LabelFrame(root,text=greet_text,padx=10,pady=10)
home_screen.pack(padx=10,pady=10)

video_entry = Entry(home_screen,width=40,borderwidth=3)
video_entry.grid(row=1,column=1)
audio_entry = Entry(home_screen,width=40,borderwidth=3)
audio_entry.grid(row=2,column=1)

video_label = Label(home_screen,text='Download video by pasting link here: ',padx=10).grid(row=1,column=0)
audio_label = Label(home_screen,text='Download audio by pasting link here: ',padx=10).grid(row=2,column=0)

video_default = StringVar()
video_default.set("480p")
audio_default = StringVar()
audio_default.set("Medium")
video_drop = OptionMenu(home_screen , video_default , "144p",'240p','360p',"480p",'720p',"1080","1440p").grid(row=1,column=2)
audio_drop = OptionMenu(home_screen,audio_default,"Low","Medium","High").grid(row=2,column=2)

video_download_button = Button(home_screen,text="Download",padx=30,command=lambda: video_download(video_entry.get(),video_default.get())).grid(row=1,column=3)
audio_download_button = Button(home_screen,text="Download",padx=30,command=lambda: audio_download(audio_entry.get(),audio_default.get())).grid(row=2,column=3)



exit_button = Button(home_screen,text="Exit",command=root.destroy,padx=20,pady=2).grid(row=3,column=1)


root.mainloop()

#30-11-2022
