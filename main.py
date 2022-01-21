import pytube
from pytube import Channel
from pytube import Playlist


def download_youtube_video(url_video):
    yt = pytube.YouTube(url_video)
    yt.streams.get_by_itag(22).download()


def download_playlist(url_playlist):
    p = Playlist(url_playlist)
    print(f'Downloading: {p.title}')
    for video in p.videos:
        video.streams.get_by_itag(22).download()
        # video.streams.get_by_itag(22).download(output_path="")


def download_youtube_channel(url_channel):
    c = Channel(url_channel)
    print(f'Downloading videos by: {c.channel_name}')
    for video in c.videos:
        video.streams.get_by_itag(22).download(output_path="")


def main():
    # download_youtube_video(url_video='')
    # download_playlist(url_playlist="")
    download_youtube_channel(url_channel="")


if __name__ == '__main__':
    main()
