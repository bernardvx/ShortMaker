"""
This script takes in a directory of  youtube videos and their 
generated subs(or any translated subtitle) and creates 30sec parts of that video

"""

from  moviepy.editor import VideoFileClip, clips_array, TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip, file_to_subtitles
import os


#init
b = 0 #beginning of clip (s)
e = 30 #end of clip(s)
dir = '/home/mackintosh/Projects/Shop/Content_subs/'
edited_dir = '/home/mackintosh/Projects/Shop/Edited_vids/'

file = ""
ad = "/home/mackintosh/Projects/Shop/full_ad.mp4"
os.chdir(dir)
videos = []


for i in os.listdir():
    if i.endswith('.mp4'):
        videos.append(i)


for video in videos:
    file = f"{dir}{video}"

    
    content = VideoFileClip(f'{file}')
    ad = VideoFileClip(ad)
    subs = f'{file}_en.srt'.replace('.mp4', '')
    generator = lambda txt: TextClip(txt.upper(), font='Helvetica-Bold', fontsize=65, color='white', method='caption', 
                                        stroke_color='black', stroke_width=1.5, align="center", size=(810, 1440))
    srt_file = file_to_subtitles(subs)
    subtitles = SubtitlesClip(srt_file, generator)
    subtitles = subtitles.subclip(0, content.duration)

    content, ad= content.subclip(0, content.duration), ad.subclip(0, content.duration)
    content = content.crop(x1=350, x2=1570) #remove 360px form each side of the width of the video
 

    content = content.resize((1080, 1000))
    ad = ad.resize((1080, 970))

    def number_of_videos(content):
        return content.duration//30 - 1

    i = 1
    vid_array = clips_array([[content],[ad]])

    while True:
        title = content.filename.replace('.mp4', '')# its lol just for testing
        
        #edit clips with parts
        while i<number_of_videos(content):
            final_short = CompositeVideoClip((vid_array, subtitles.set_position("center")), size=((1080, 1920))).subclip(b, e)
            final_short.resize(width=1080, height=1920).write_videofile(f'{title}_Part_{i}.mp4', fps=24)     
            os.rename(f'{title}_Part_{i}.mp4', f'{title}_Part_{i}.mp4'.replace('Content_subs', 'Shorts'))

            b += 30
            e += 30
            i += 1
        else:
            final_short = CompositeVideoClip((vid_array, subtitles.set_position("center")), size=((1080, 1920))).subclip(e, content.duration)
            final_short.resize(width=1080, height=1920).write_videofile(f'{title}_Part_{i}.mp4', fps=24)   
            os.rename(f'{title}_Part_{i}.mp4', f'{title}_Part_{i}.mp4'.replace('Content_subs', 'Shorts'))

            i, b, e =0, 0, 30
            os.rename(f'{dir}{video}', f'{edited_dir}{video}')

            break
 
        


    print('done')
