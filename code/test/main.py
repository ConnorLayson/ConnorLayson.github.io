from pytube import YouTube
from pytube import Playlist

print("hello")

def video():
    link = Element('link-input').element.value
    try:
        yt = YouTube(link)

        output = f'Title: {yt.title}/nViews: {yt.views}/nLength: {yt.length}'
        Element('output').write(output)
    except:
        output = "There was an error with your link"
        Element('output').write(output)
