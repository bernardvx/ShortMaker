import requests
import time
import json
from instapy_cli import client


# this access token expires  march 2024
access_token='EABkwyvThydABO6b4q3ldIKZAAnnBYCyFXhOqfYmr3cpGaE25mngcurBeM9SytDHs7nRHb59mwCUQ4SXKlO93df1KidrbFtwCgGoedBr5z0gzczrDEFtWUjVftHPybGCiBrvRKRrK8mLrJ42Ujt7y7Q0OI9jaH7VLb4aHmlpPQNbwbLAL4foULQOe4sBMM'
instagram_account_id='17841464231097531'
facebook_account_id ='244613845382488'


video_url='https://media.publit.io/file/Friends-Everybody-Hates-Chandler-ad-Part-1-T.mp4'
caption = 'Friends Chandler is hated at work \ncheckout the friends store in the bio for merch actualyy go to elmure . com'
#this below works , need to be carefull on the video specs as per reel requirements instagram graph api
#and access token that never expires did not work for the moment so generating a new one works.


graph_url = 'https://graph.facebook.com/v18.0/'
def upload_video_to_insta(video_url=video_url,
               caption=caption,
               instagram_account_id=instagram_account_id,
               access_token=access_token):
    
    url = graph_url + instagram_account_id + '/media'
    param = dict()
    param['access_token'] = access_token
    param['caption'] = caption
    param['video_url'] = video_url
    param['media_type'] = "REELS"
    param['thumb_offset'] = '10'
    response = requests.post(url, params=param)
    response = response.json()
    return response

# creation_id is container_id
def post_video_on_insta(creation_id ='',instagram_account_id='',access_token=''):
    url = graph_url + instagram_account_id + '/media_publish'
    param = dict()
    param['access_token'] = access_token
    param['creation_id'] = creation_id
    response = requests.post(url,params=param)
    response = response.json()
    print(f'instagram reel uploaded with id: {response}')

    return response


response_ig = upload_video_to_insta()
time.sleep(25)
print(response_ig)
post_video_on_insta(creation_id=response_ig['id'], instagram_account_id=instagram_account_id ,access_token=access_token )
print('that was the instagram reel')