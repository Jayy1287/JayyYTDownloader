from pytube import YouTube
#Documentation: https://pytube.io/en/latest/


def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
    youtubeObject.download()
  except:
    print("Error in downloading")
  print("Download Completed, Suiiiiii!")


link = input("Feed me the link! URL: ")
Download(link)
