from pytube import YouTube

def downlaod(link):
    youtubeObject = YouTube(link)
    youtubeObject =youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()

    except:
        print("An error has occurred!,\n please try again")
    print("Download completed suscessfully")


link = input("Enter URL for youtube video: ")
downlaod(link)
