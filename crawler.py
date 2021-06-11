import requests
import bs4 

def get_all_links(url):
 ret = []
 resp = requests.get(url)
 soup = bs4.BeautifulSoup(resp.content, "html.parser")
 links = soup.find_all("a", attrs = {"class" : "title"})
 for i in links:
   ret.append(i['href'])
 return ret
 
 
#get_all_links("https://www.metrolyrics.com/in-my-feelings-lyrics-drake.html")   
  
def get_song_lyrics(url):
 lyrics = []
 resp = requests.get(url)
 soup = bs4.BeautifulSoup(resp.content, "html.parser")
 lines = soup.find_all("p", attrs = {"class" : "verse"})
 for i in lines:
  lyrics.append(i.get_text())
 return "\n".join(lyrics)
 
  
  
  
  
#get_song_lyrics("https://www.metrolyrics.com/in-my-feelings-lyrics-drake.html")  
def file_name(url):  
  return url.split("/")[-1].replace(".html", ".txt")
  
  
  
def main():
 l = get_all_links("https://www.metrolyrics.com/in-my-feelings-lyrics-drake.html")
 for i in l:
  f = file_name(i)
  print(f"-> {f}")
  f1 = open(f, "w")
  song = get_song_lyrics(i)
  f1.write(song)
  f1.close()
  
  
if __name__ == "__main__":
  main()   
  
