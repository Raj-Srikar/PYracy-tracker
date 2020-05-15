from moviepy.editor import *

def fdur(clip,frno):                #Function takes the video and the frame number as arguments
    Fps=clip.fps                          #This function returns the duration at which,
    dur = frno/Fps                              #the frame given is present
    return dur

video = VideoFileClip("sample.mp4")
txt = TextClip("Mov",fontsize=15,color='black')                                 #Creating a text video file saying "Mov"
txt = txt.set_position((230,20)).set_duration(0.04)
vid = CompositeVideoClip([video , txt.set_start(fdur(video,71))])               #Overlay the text clip onto the video
vid.write_videofile("ESample.mp4")                                              #Create the video file, "ESaample.mp4"
