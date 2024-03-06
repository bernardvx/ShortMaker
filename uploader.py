import instagram_uploader
#import youtube_uploader
import time
import os
from publitio import PublitioAPI

publitio_api = PublitioAPI('AXsb12Qjld34v54mtXPu', 'wrmB9d7APJQHmcnMwje0gJ3JiH4QvWpg')
response = publitio_api.list_files()

dirc= '/home/mackintosh/Projects/Shop/Shorts/'
online_dir = 'https://media.publit.io/file/'
os.chdir(dirc)

vids = {}
    
for i in sorted(os.listdir()):
    if i.endswith('.mp4'):
        vids[f'{i}'] = f"{i.replace('_', ' ').replace('.mp4', '')}. \nCheck out the link in bio for a suprise #GossipGirlFan #PLLAddict #SceneStealer #Fashionista #TVObsessed #DiscountCode"

#video_url='http://80.90.94.66/shorts_en_fashion/Blair_and_Chuck_Ill_always_love_you_Part_1.mp4'
#caption = 'Blair_and_Chuck_Ill_always_love_you_Part_1  #girlss #love'.replace('_', " ")


instagram_account_id = instagram_uploader.instagram_account_id
access_token = instagram_uploader.access_token

uploaded = 0

for link, caption in vids.items(): 
    #upload 7 shorts with 2h increments 
    while uploaded < 7:


        response_ig = instagram_uploader.upload_video_to_insta(video_url=f"{online_dir}{link.replace('_', '-')}", caption=caption)
        print(link.replace('_', '-'), caption)
        while True:
            
            time.sleep(25)
            print(response_ig)
            try:
                post = instagram_uploader.post_video_on_insta(creation_id=response_ig['id'], instagram_account_id=instagram_account_id ,access_token=access_token )
                     
            except:
                time.sleep(10)
                if 'id' not in post.keys:
                    print('Trying again to post it')
                    continue
                else:

                    print(f"Instagram reel uploaded {post['id']}")
                    
                    break
                
            break
            
            
        os.rename(f"{dirc}{link}", f"{dirc.replace('Shorts', 'Ushorts')}{link}" ) # move the uploaded reel to the 'uploaded shorts' directory
        print('that was the instagram reel')
        uploaded += 1
        print('videos uploaded: ', uploaded)
        time.sleep(120)
        break
        



