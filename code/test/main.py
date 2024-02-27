from pytube import YouTube
from pytube import Playlist

print("hello")

def video():
    link =  document.querySelector("#link-input")
    try:
        yt = YouTube(link)

        output = f'Title: {yt.title}/nViews: {yt.views}/nLength: {yt.length}'
        Element('output').write(output)
    except:
        output = "There was an error with your link"
        Element('output').write(output)
