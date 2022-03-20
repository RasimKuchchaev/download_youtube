import pytube
from pytube import Channel
from pytube import Playlist


def download_youtube_video(url_video):
    yt = pytube.YouTube(url_video)
    yt.streams.get_by_itag(22).download()


def download_playlist(url_playlist):
    p = Playlist(url_playlist)
    print(f'Downloading: {p.title}')
    count = 1
    for video in p.videos:
        print(f'INFO {count}/{p.length} : {video.title}')
        # video.streams.get_by_itag(22).download()
        video.streams.get_by_itag(22).download(output_path=f"D:\\Video Lesson\\{video.author}\\{p.title}")
        count += 1

        # with open("error.txt", "a") as file:
        #     file.write(f"{count_err}    {video.title} \n")


def download_youtube_channel(url_channel):
    c = Channel(url_channel)
    print(f'Downloading videos by: {c.channel_name}')
    count = 1
    for video in c.videos:
        print(f'INFO {count}/{c.length} : {video.title}')
        video.streams.get_by_itag(22).download(output_path=f"D:\\Video Lesson\\{c.channel_name}")
        count += 1


def main():
    # download_youtube_video(url_video='')
    download_playlist(url_playlist="https://www.youtube.com/watch?v=evjpa3v22-U&list=PLQAt0m1f9OHsMP67JNONOMh13dw_UHf52")
    # download_youtube_channel(url_channel="https://www.youtube.com/c/PythonToday/videos")


if __name__ == '__main__':
    main()
