import instagram_uploader
#import youtube_uploader
import time
import os
from publitio import PublitioAPI

publitio_api = PublitioAPI('AXsb12Qjld34v54mtXPu', 'wrmB9d7APJQHmcnMwje0gJ3JiH4QvWpg')
response = publitio_api.list_files()

dir= '/home/mackintosh/Projects/Shop/Shorts/'
online_dir = 'https://media.publit.io/file/'
os.chdir(dir)

vids = {}
    
for i in sorted(os.listdir()):
    if i.endswith('.mp4'):
        vids[f'{i}'] = f"{i.replace('_', ' ').replace('.mp4', '')}. \nCheck out the link in bio for a suprise #GossipGirlFan #PLLAddict #SceneStealer #Fashionista #TVObsessed #DiscountCode" 



#video_url='http://80.90.94.66/shorts_en_fashion/Blair_and_Chuck_Ill_always_love_you_Part_1.mp4'
#caption = 'Blair_and_Chuck_Ill_always_love_you_Part_1  #girlss #love'.replace('_', " ")


instagram_account_id = instagram_uploader.instagram_account_id
access_token = instagram_uploader.access_token

uploaded = 1

for link, caption in vids.items():
    while uploaded < 7:

        response_ig = instagram_uploader.upload_video_to_insta(video_url=f"{online_dir}{link.replace('_', '-')}", caption=caption)
        print(link.replace('_', '-'), caption)
        while True:
            
            time.sleep(25)
            print(response_ig)
            try:
                instagram_uploader.post_video_on_insta(creation_id=response_ig['id'], instagram_account_id=instagram_account_id ,access_token=access_token )
            except:

                continue
        
        print('that was the instagram reel')
        break    
        time.sleep(300)
    else:
        break



