from pytube import YouTube
from pytube import Playlist
from pyscript import document

def video():
    link =  document.querySelector("#link-input")
    output = 'Found video'
    Element('#output').write(output)