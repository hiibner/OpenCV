# Created By  : Huy Luong
# Created Date: 07.05.2019
# Inspired by Copyright© https://drive.google.com/file/d/0B8Qjj40Go4-UOGJrUmNwV0NoeTA/view
# License: GNU GPL
# =============================================================================
# Imports
from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import *
import os
# =============================================================================

width = 500
height = 500
center = height//2
white = (255, 255, 255)
green = (0,128,0)

def save():
    filename = "my_drawing.png"
    if os.path.exists(filename):
        os.remove(filename)
    image1.save(filename)
    root.destroy()
def clear():
    cv.delete("all")
    draw.rectangle((0, 0, 500, 500), fill=(255, 255, 255, 1))

def close():
    root.destroy()

def paint(event):
    # python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval(x1, y1, x2, y2, fill="black",width=5)
    draw.line([x1, y1, x2, y2],fill="black",width=5)

root = Tk()
# Tkinter create a canvas to draw on
cv = Canvas(root, width=width, height=height, bg='white')

cv.pack()
# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = PIL.Image.new("RGB", (width, height), white)

# do the Tkinter canvas drawings (visible)
# cv.create_line([0, center, width, center], fill='green')

draw = ImageDraw.Draw(image1)
cv.pack(expand=YES, fill=BOTH)

# do the PIL image/draw (in memory) drawings
#draw.line([0, center, width, center], green)

cv.bind("<B1-Motion>", paint)
# PIL image can be saved as .png .jpg .gif or .bmp file (among others)


button=Button(text="save",command=save)
button.pack()
button2=Button(text="clear",command=clear)
button2.pack(side = "left")
button3=Button(text="close", command=close)
button3.pack(side = "right")
root.mainloop()