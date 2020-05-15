from moviepy.editor import *

def fdur(clip,frno):
    Fps=clip.fps
    dur = frno/Fps
    return dur

video = VideoFileClip("sample.mp4")
txt = TextClip("Mov",fontsize=15,color='black')
txt = txt.set_position((230,20)).set_duration(0.04)
vid = CompositeVideoClip([video , txt.set_start(fdur(video,71))])
vid.write_videofile("ESample.mp4")
