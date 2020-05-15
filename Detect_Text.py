from moviepy.editor import *
from moviepy.video import *
import cv2
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

def fdur(clip,frno):
    Fps=clip.fps
    dur = frno/Fps
    return dur

clip = VideoFileClip("ESample.mp4")                                 #the video file to be opened here should already contain the code
crp = fx.all.crop(clip, x1=230, y1=20, x2=260, y2=40)               #Crop the part where the code is present

crp.save_frame("code.jpg",fdur(clip,71))                            #Save the cropped image as "code.jpg"

img = Image.open("code.jpg")
ni = img.resize((250,150))                                          #Enlarge the cropped image
ni.save("rs.jpg")                                                   #Save the enlarged image as "rs.jpg"
txt = pytesseract.image_to_string(ni)                               #Detect the text in the image
print("Hash code =",txt)                                            #Print the text
