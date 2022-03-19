import os.path
from subprocess import CREATE_NEW_CONSOLE
from youtube_transcript_api import YouTubeTranscriptApi
from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

vid = input("Enter youtube url:")


# URl to web scrap from.
page_url = vid

vid = vid.replace("https://www.youtube.com/watch?v=", "")

# >>><<< # TEST: https://www.youtube.com/watch?v=Irc7cPKOkkM # >>><<< #

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

video_name = page_soup.div.meta["content"]
video_name = video_name.replace("/","-").replace("|","_").replace('"','')
#max substring length
video_name = video_name[:100]


# If a video's ID starts with a hypen you'll have to mask the hyphen using \ to prevent the CLI from mistaking it for an argument name.
# e.g. YouTubeTranscriptApi.get_transcript("\-abc123")

outls = []

tx = YouTubeTranscriptApi.get_transcript(vid)


save_path = "D:\Documents\Programming is fun\Python is fun\\transcripts\\"

file_path = os.path.join(save_path, video_name + "_transcript.txt")


# if tx.count()<300:

for i in tx[0:250]: # ►►► how to get slices of dictionary? https://stackoverflow.com/questions/29216889/slicing-a-dictionary
# for i in tx:
	outtxt = (i['text'])
	outls.append(outtxt)

	# with open(video_name + "_transcript.txt", "a") as opf:
	with open(file_path, "a") as opf:
		opf.write(outtxt + " ")
opf.close()
print("Saved successfully")

# elif tx.count()>300:
	# print("Transcript too long")
