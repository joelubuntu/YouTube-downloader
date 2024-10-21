import os
from pytube import YouTube, Playlist
import datetime

def video_download(link, res):
    try:
        yt = YouTube(link)
        title = yt.title
        
        # Find the best matching video stream based on resolution
        if res.lower() == "high":
            stream = yt.streams.filter(progressive=True, res="720p").first()  # 720p (high)
        elif res.lower() == "medium":
            stream = yt.streams.filter(progressive=True, res="480p").first()  # 480p (medium)
        elif res.lower() == "low":
            stream = yt.streams.filter(progressive=True, res="144p").first()  # 144p (low)
        else:
            print("Invalid resolution. Please use 'high', 'medium', or 'low'.")
            return

        if stream:
            print(f"Downloading {title} in {res} quality...")
            stream.download()
            print(f"Downloaded {title} successfully!\n")
        else:
            print(f"No available stream for {res} resolution.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def audio_download(link, quality):
    try:
        yt = YouTube(link)
        title = yt.title
        
        # Find the best matching audio stream based on bitrate
        if quality.lower() == "high":
            stream = yt.streams.filter(only_audio=True, abr="160kbps").first()  # 160kbps (high quality)
        elif quality.lower() == "medium":
            stream = yt.streams.filter(only_audio=True, abr="128kbps").first()  # 128kbps (medium quality)
        elif quality.lower() == "low":
            stream = yt.streams.filter(only_audio=True, abr="48kbps").first()  # 48kbps (low quality)
        else:
            print("Invalid quality. Please use 'high', 'medium', or 'low'.")
            return

        if stream:
            print(f"Downloading {title} audio in {quality} quality...")
            out_file = stream.download()
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(f"Downloaded {title} audio successfully!\n")
        else:
            print(f"No available stream for {quality} quality.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def playlist_download(link, res):
    try:
        playlist = Playlist(link)
        print(f"Downloading playlist with {len(playlist.video_urls)} videos...")

        # Download each video in the playlist
        for video in playlist.videos:
            video_download(video.watch_url, res)

        print("Playlist downloaded successfully!\n")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def welcome():
    user_name = os.getlogin()
    time = datetime.datetime.now().hour
    greeting = "Good morning" if 5 <= time < 12 else "Good afternoon" if 12 <= time < 17 else "Good evening"
    print(f"\n{greeting}, {user_name}!")

def menu():
    print("\nWhat would you like to download?")
    print("1. Video")
    print("2. Audio")
    print("3. Playlist")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        link = input("Enter the YouTube video URL: ")
        res = input("Choose quality (high/medium/low): ")
        video_download(link, res)
    elif choice == "2":
        link = input("Enter the YouTube audio URL: ")
        quality = input("Choose audio quality (high/medium/low): ")
        audio_download(link, quality)
    elif choice == "3":
        link = input("Enter the YouTube playlist URL: ")
        res = input("Choose quality (high/medium/low): ")
        playlist_download(link, res)
    else:
        print("Invalid choice. Please restart the program.")
        return

welcome()
menu()
