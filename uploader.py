import instagram_uploader
import youtube_uploader
import time
import os
from googleapiclient.errors import HttpError


CLIENT_SECRETS_FILE = "/home/mackintosh/Projects/Shop/client_secrets.json"
youtube = youtube_uploader.get_authenticated_service()
dirc= '/home/mackintosh/Projects/Shop/Shorts/'
online_dir = 'https://elmure.com/api/shorts/dl?filePath=shorts$$EN_fashionablemysteries$$'#change to the actuall link
os.chdir(dirc)

vids = {}
    
for i in sorted(os.listdir()):
    if i.endswith('.mp4'):
        vids[f'{i}'] = f"{i.replace('_', ' ').replace('.mp4', '')}.#GossipGirlFan #SceneStealer #TVObsessed  \nCheck out the link in bio for a suprise #DiscountCode"

instagram_account_id = instagram_uploader.instagram_account_id
access_token = instagram_uploader.access_token

uploaded = 0


for link, caption in vids.items(): 
    #upload 5 shorts with .5h increments 
    while uploaded < 5:
        print(f'{dirc}{link}, {caption[:95]}')
        #upload video on youtube, make a better description and put emojis on the tittles
        try:
            youtube_uploader.initialize_upload(youtube, file=f'{dirc}{link}', title=caption[:95] , description=f'{caption} #Shopping', tags=None, category='22', privacyStatus='public')
        except HttpError as e:
            print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
        
        #posts video on IG
        response_ig = instagram_uploader.upload_video_to_insta(video_url=f"{online_dir}{link}", caption=caption)
        print(f'{online_dir}{link}', caption)
        while True:
            
            time.sleep(65)
            print(response_ig)
            try:
                post = instagram_uploader.post_video_on_insta(creation_id=response_ig['id'], instagram_account_id=instagram_account_id ,access_token=access_token )
                     
            except:
                time.sleep(35)
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
        time.sleep(1800)
        break
        



