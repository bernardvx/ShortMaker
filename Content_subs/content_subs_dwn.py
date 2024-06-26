import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter


link = 'https://www.youtube.com/watch?v='
id = '4Tn-gVpvMBU&t=13s'

urls = [f'{link}{id}']
dir = '/home/mackintosh/Projects/Shop/Content_subs'
title= ''

link_title = {
    # all that are commented out are done
    #'hMqtOFE8fxA': 'Everyone Finds Out Serena was in an Accident',
    #'XbBBV2PFM6w': 'Gossip Girl is Revealed',
   # '8BIEXLfT4YY': 'Dan & Serena | The Night We Met',
   # 'd9tng5p-PT8': 'Blair and Chuck Ill always love you',
   # 'k3xzHOlOwqo': 'Pretty Little Liars - 03x02 - The girls find out that Jenna can see',
   # '9GRry4EPHLs': 'Pretty Little Liars - 02x01 - The girls get confronted by their parents',
   # 'PPNMMR33yhc': 'Pretty Little Liars - Spencers Intervention',
   # 'XcCVD3cAnoI': 'Pretty Little Liars - "Miss Me x 100"',
   # '4QCnVbDaltU': 'Pretty Little Liars - Ezra is Shot - "A is for Answers"',
   'Jq0tg56DV7A': 'Gossip Girl - the wedding scene',
   'EYBeuTntK90': ' Blair dancing for Chuck at a burlesque club',
   '4sWTBMoyr4I': "CHUCK SAYS 'I LOVE YOU' TO BLAIR 'The Goodbye Gossip Gir'",
   'sQjDTHpMBzw': ' Blair storms off the photo shoot 📸 Gossip Girl',
   'FrGWGYAC4r4': 'Nate and Chuck season 1  logoless',
   '-IpygQbGG34': 'Chuck and Blair break up scene season 3',
   'wR9iPwX3JsE': ' Blair and Jenny Popularity War',
   'W9vwRXiXv14': 'Gossip Girl 4x10 Jenny & Blair',
   '3QjNuEtH-Yo': "End of Blair and Louie's Wedding Party",
   '7kk-vkp1PNI': "Blair tells Chuck she's pregnant Monkey comforts him",
   'upor6jqgDyQ': 'Serena and Blair in Paris',
   #lucifer
   'BVGX_5hVTf4': 'Chloe finds out who Lucifer really is ',
   'JNN3_Du-2Nk': 'Lucifer- S2E13 Ending Scene',
   'vAN41c_vGKA': "Amenadiel explains Chloe's gift",
   'I3DfQFU0Heg': 'You make me vulnerable',
   'dSz01YPapRI': 'God and Lucifer do therapy',
   'y2QtzGlGZMM': "God tells Lucifer that he's losing his powers",
   'ulZaXzhUDWs': 'Chloe Meets God',
   'k5StRockQrM': 'Lucifer and chloe first kiss',
   

}


"""
ydl_opts ={
    'format': 'best',
    #'outtmpl': f'{dir}/{title}.%(ext)s',
}

''' TODO: create a functions to set the files name'''
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ''' Get title of video for filename'''
    info = ydl.extract_info(urls[0], download=False)
    title = info.get('title', None)
"""    

for key, value in link_title.items():
        
    title = value.replace(' ', '_') #getstitle and  replaces the spaces with _


    ydl_opts_dwn ={
        'format': 'best',
        'outtmpl': f'{dir}/{title}.mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts_dwn) as ydl:
        error_code = ydl.download(f"{link}{key}")
    
    print(f'video with id: {key} and title {value} was downloaded')

    #subtitles = YouTubeTranscriptApi.get_transcript(id)
    subtitles = YouTubeTranscriptApi.get_transcript(key) #gets id of youtube link 
    print('got subs for id:', key)


    formatter = SRTFormatter()
    subtitles_formatted = formatter.format_transcript(subtitles)
    with open(f'{dir}/{title}_en.srt', 'w', encoding='utf-8') as subs_srt:
        subs_srt.write(subtitles_formatted)