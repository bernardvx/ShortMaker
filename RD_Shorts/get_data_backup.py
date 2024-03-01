from googleapiclient.discovery import build
from pprint import PrettyPrinter  

pp = PrettyPrinter()

# Set up the YouTube Data API client
api_key = 'AIzaSyDREipXOyNWHy5tSiWFv08ibJvRaeXZl9w'
youtube = build('youtube', 'v3', developerKey=api_key)

channel_id = 'UCUtS0weWmRsAgC06E7u65og' 


#Get the video_ids from a channel 
request = youtube.search().list(part='snippet', 
                                type='video', 
                                channelId=channel_id, 
                                maxResults=50).execute()
for i in request['items']:
    #pp.pprint(i) 
    links =list(i['id'].values())
    #print(f'https://www.youtube.com/shorts/{links[1:][0]}')
    vid_ids= links[1:][0]

    video_dur = youtube.videos().list(part='contentDetails',
                                        id=f'{vid_ids}'
                                        
        
    ).execute()

    pp.pprint(video_dur['items'][0]['contentDetails']['duration'])