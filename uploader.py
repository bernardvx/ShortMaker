import instagram_uploader
#import youtube_uploader
import time
import os


dir= '/home/mackintosh/Projects/Shop/Shorts/'
os.chdir(dir)

video_url='http://80.90.94.66/shorts_en_fashion/Blair_and_Chuck_Ill_always_love_you_Part_1.mp4'
caption = 'Blair_and_Chuck_Ill_always_love_you_Part_1  #girlss #love'.replace('_', " ")


instagram_account_id = instagram_uploader.instagram_account_id
access_token = instagram_uploader.access_token

response_ig = instagram_uploader.upload_video_to_insta(video_url=video_url, caption=caption)
time.sleep(25)
print(response_ig)
instagram_uploader.post_video_on_insta(creation_id=response_ig['id'], instagram_account_id=instagram_account_id ,access_token=access_token )
print('that was the instagram reel')