from pytube import Playlist
from pytube import YouTube

pl_url = "https://www.youtube.com/playlist?list=PLtTSER1U4AE5ZhxWfvfLeQ9bhOD2vg-HQ"

pl = Playlist(pl_url)

for url in pl.video_urls:
    print("download url: " + url)
    yt = YouTube(url, use_oauth=True)
    #yt.streams.filter(only_audio=True).first().download()
    yt.streams.get_audio_only("mp4").download()
