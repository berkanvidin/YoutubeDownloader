import pytube

url = input("enter video url: ")
path = "D:\Müzikler"
pytube.YouTube(url).streams.get_audio_only().download(path)
