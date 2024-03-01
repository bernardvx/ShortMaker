from tiktok_uploader.upload import upload_videos
from tiktok_uploader.auth import AuthBackend
import os

cookies='/home/mackintosh/Projects/Shop/cookies.txt'
path = '/home/mackintosh/Projects/Shop/Ucontent_subs/'
os.chdir(path)

def video_dir(video):
    vid = {'video': f'{video}', 'description': 'Merch ready at https://friends.com'}
    videos = [vid for vid in video]
    return videos

videos = []
for video in os.listdir():
    if video.startswith("Friends_Everybody_Hates_Chandler_Part"):
        vid = {'video': f'{video}', 'description': f"{video.replace('_', ' ')}   !!!!Merch ready at https://friends.com!!!!"}
        videos.append(vid)



print(videos)
'''
videos = [
    {
        'video' : 'short.mp4',
        'description' : 'Merch ready at https://friends.com'
    },
    {
        'video' : 'youtube_final_short.mp4',
        'description' : 'Merch ready at https://eminem.com'

    }
]'''

auth = AuthBackend(cookies='/home/mackintosh/Projects/Shop/cookies.txt')
upload_videos(videos=videos, auth=auth, browser='firefox')
