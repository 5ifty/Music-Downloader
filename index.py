from __future__ import unicode_literals
import youtube_dl
import time

def main():
    
    yes_list = ['y']
    i = input("Please enter the url of the song/audio you would like to download: ")
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([i])
    print("File should be in the folder the CMD or the index.py file is located. Thanks for using our service!")
    time.sleep(5)
    z = input("If you would like to download another song type 'y' if not please type 'n'.")
    if z in yes_list:
        main()
    else:
        print("Thanks for using the Youtube to mp3 CMD, have a good day")
        time.sleep(5)
        exit()

main()
