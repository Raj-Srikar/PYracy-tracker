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

clip = VideoFileClip("ESample.mp4")
crp = fx.all.crop(clip, x1=230, y1=20, x2=260, y2=40)

crp.save_frame("code.jpg",fdur(clip,71))

img = Image.open("code.jpg")
ni = img.resize((250,150))
ni.save("rs.jpg")
txt = pytesseract.image_to_string(ni)
print("Hash code =",txt)
