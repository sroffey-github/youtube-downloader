from youtube_dl import YoutubeDL
from pytube import Playlist
from pytube import YouTube
import urllib.request
import platform
import pytube
import re
import os

original_path = os.getcwd()

first = 'https://www.youtube.com/results?search_query='
second = 'https://www.youtube.com/watch?v='

def clear():
    if 'windows' in platform.system():
        os.system('cls')
    else:
        os.system('clear')

def search(key):
    count = 0
    top = []
    url = first + key
    html = urllib.request.urlopen(url)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    for i in video_ids:
        if count == 3:
            continue
        else:
            top.append(second + i)
            count += 1
    return top

def download(mode, url, path):
    if mode == 3 or mode == 4:
        pass
    else:
        print('\n[+] Downloading Top Result...')
    if mode == 1:
        opts = {
            'format':'bestaudio/best',
            'postprocessors':[{
                'key':'FFmpegExtractAudio',
                'preferredcodec':'mp3',
                'preferredquality':'192'
            }]
        }
        ydl = YoutubeDL(opts)
        os.chdir(path)
        ydl.download([url])
        os.chdir(original_path)
        return True
    elif mode == 2:
        opts = {}
        ydl = YoutubeDL(opts)
        os.chdir(path)
        ydl.download([url])
        os.chdir(original_path)
        return True
    elif mode == 3:
        opts = {
            'format':'bestaudio/best',
            'postprocessors':[{
                'key':'FFmpegExtractAudio',
                'preferredcodec':'mp3',
                'preferredquality':'192'
            }]
        }
        ydl = YoutubeDL(opts)
        os.chdir(path)
        playlist = Playlist(url)
        print('[-] Downloading {} Videos...'.format(len(playlist.video_urls)))
        for url in playlist:
            print('[-] Downloading {}...'.format(url))
            ydl.download([url])
        os.chdir(original_path)
        return True
    elif mode == 4:
        opts = {}
        ydl = YoutubeDL(opts)
        playlist = Playlist(url)
        os.chdir(path)
        print('[-] Downloading {} Videos...'.format(len(playlist.video_urls)))
        for url in playlist:
            print('[-] Downloading {}...'.format(url))
            ydl.download([url])
        os.chdir(original_path)
        return True
    else:
        return False