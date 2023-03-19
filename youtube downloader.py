from youtubesearchpython import VideosSearch
from pytube import YouTube

def downlad():
  prompt = input("Search for the video: ")
  search = VideosSearch(prompt, limit=1) 
  videolink = search.result()["result"][0]["link"]#search for the video link zero is the first 

  yt_video =YouTube(videolink)
  videos = yt_video.streams.get_by_itag(18)# OR  vieos= vid.streams.get_highest_resolution() 18 will getit 360 rslution to unite the otion 
  videos.download()
  
  videoname = search.result()["result"][0]["title"] 
  print(f'{videoname} is downloaded successfully')
  try:
    with open ('Downloaded', 'a') as f:#file write whats downloaded at the end of the same file so append 
      f.write(videoname + "\n")
  except FileNotFoundError:
    f = open ('Downloaded', 'w') #write in a new file if not found
    f.write(videoname + "\n")

def List_downladed ():
  try:
    with open ("Downloaded", "r") as videos: #list the vieo names 
      print("The video Downloaded is:\n")
      for name in videos:
        print(name, end=" ")
  except FileNotFoundError:
    print("\nThere is no videos downladed!")

def main ():
  while True:
    print ("\nChoose the option you want\n")
    print("< 1 > Download video")
    print("< 2 > View downloaded")
    print("< 3 > Exit")
    try:  
      op = int (input ())
      if op == 1:
        downlad()
      elif op == 2:
        List_downladed()
      elif op == 3:
        exit()
      else:
        print("Invalid input!")
    except ValueError:
      print ("Ivalid input!")
main()
