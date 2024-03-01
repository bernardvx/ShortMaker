from pytube import YouTube
import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


'''
chrome_options = Options()
chrome_options.add_argument("--headless") 

utube_basic_link = 'https://www.youtube.com/shorts/'
utube_channel_link = 'https://www.youtube.com/channel/'
'''




with open('ids_unique.txt', 'r') as f:
    ids = f.read().splitlines()
a, b = 0, 25562


conn = psycopg2.connect(
    host='localhost',
    database='youtube_shorts',
    user = 'postgres',
    password='mackintosh'
)
cur = conn.cursor()

select_one = """
SELECT id, length, views, published, title 
FROM data where length<61 and views > 1000000 and views <10000000 order by views asc;
"""
cur.execute(select_one)
rows = cur.fetchall()
c = 0
characters, lengths ,views_tot, time_differences = [], [], [], []

try:
    for row in rows:
        print(row)
        timestamp = '2023-09-05 00:00:00'
        published = row[3]
        views = row[2]/1000
        length = row[1]
        c+=1
        characters.append(row[4].count('#'))
        public_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S') - datetime.strptime(published, '%Y-%m-%d %H:%M:%S')
        time_difference = str(public_time).split(" ")[0]
        time_differences.append(time_difference)   
        views_tot.append(views)
        lengths.append(length)
except Exception as err:
    print(err)

plt.plot(views_tot, characters, marker='o', linestyle='-', color='b', label='Data Points')
plt.xlabel('views')
plt.ylabel('hashtags number ')
plt.show()
cur.close()
conn.close()


'''
cur.execute("""CREATE TABLE IF NOT EXISTS data (
id bigserial PRIMARY KEY,
link varchar,
title varchar,
views int8,
length int8,
published varchar,
channel_views varchar,  
channel_videos int8,
channel_created varchar,
subscribers varchar);
""")

conn.commit()



def get_channel_info(url):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    element = driver.find_element(By.ID, "right-column")
    texts = element.text.split("\n")
    channel_created = texts[1].split("Joined ")[1]
    channel_views = texts[2].split(" ")[0]
    element_id = "videos-count"
    channel_videos = driver.find_element(By.ID, element_id).text.split(" ")[0]
    subscriber_element_id = "subscriber-count"
    subscribers = driver.find_element(By.ID, subscriber_element_id).text.strip()
    driver.quit() 
    return channel_created, channel_views, channel_videos, subscribers

links = [f'{utube_basic_link}{i}' for i in ids]
links_copy = links
lastprc = -1
for i in links_copy[25562:]:
    b += 1
    try: 
        video = YouTube(i)
        url = f"{utube_channel_link}{video.channel_id}/about"
        channel_created, channel_views, channel_videos, subscribers = get_channel_info(url)
        insert = ("INSERT INTO data (link, title, views, length, published, channel_videos, channel_created, subscribers, channel_views) VALUES (%s, %s,%s, %s, %s,%s, %s,%s,%s );")  
        values = (f'{i}', f'{video.title}', video.views, video.length, f'{video.publish_date}', channel_videos, f'{channel_created}', f'{subscribers}', channel_views) 
        cur.execute(insert, values)
        conn.commit()

        #print(f"""{video.channel_id}-->{video.title}----------{video.views}views     {video.length}sekonda {video.publish_date} koha 
        #    subscribers:{subscribers} {channel_videos}videot e kanalit {channel_created}  """) 
    except Exception as e:
        print(str(e)) 
    percentage = int(b/137646*100)
    if(lastprc != percentage):
        lastprc=percentage
        print(percentage,"%")


cur.close()
conn.close()

'''




