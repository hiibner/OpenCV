import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from tkinter import *


class resultwindow:
    def __init__(self, window, window_title, images):
        self.window = window
        self.window.title(window_title)
        self.images = images
        # Load an image using OpenCV

    def showWindow(self):
        image = self.images.pop()
        self.cv_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
        self.height, self.width, no_channels = self.cv_img.shape

        # Create a canvas that can fit the above image

        self.canvas = tkinter.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.pack()

        # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))

        # Add a PhotoImage to the Canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

        self.next_button = tkinter.Button(self.window, text="Next", command=self.nextimage)
        self.next_button.pack(anchor=S, expand=True)

        self.close_button = tkinter.Button(self.window, text="Close", command=self.close)
        self.close_button.pack(anchor=S, expand=True)

        self.zoom_button = tkinter.Button(self.window, text="Zoom", command=self.zoom)
        self.zoom_button.pack(anchor=S, expand=True)

        self.window.mainloop()

    def nextimage(self):
        if  len(self.images)!= 0 :

            self.canvas.delete(ALL)

            image = self.images.pop()
            self.cv_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            self.height, self.width, no_channels = self.cv_img.shape
            # Create a canvas that can fit the above image
            self.canvas = tkinter.Canvas(self.window, width=self.width, height=self.height)
            self.canvas.pack()
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

            self.zoom_button.destroy()
            self.close_button.destroy()
            self.next_button.destroy()

            self.next_button = tkinter.Button(self.window, text="Next", command=self.nextimage)
            self.next_button.pack(anchor=S, expand=True)
            self.close_button = tkinter.Button(self.window, text="Close", command=self.close)
            self.close_button.pack(anchor=S, expand=True)
            self.zoom_button = tkinter.Button(self.window, text="Zoom", command=self.zoom)
            self.zoom_button.pack(anchor=S, expand=True)
            self.window.geometry("300x300")

        else:
            self.window.destroy()

    def close(self):
        self.window.destroy()

    def zoom(self):
        im =  self.cv_img

        self.cv_img = cv2.resize(self.cv_img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
        self.height, self.width, no_channels = self.cv_img.shape
        # Create a canvas that can fit the above image
        self.canvas = tkinter.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.pack()
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

        self.zoom_button.destroy()
        self.close_button.destroy()
        self.next_button.destroy()

        self.next_button = tkinter.Button(self.window, text="Next", command=self.nextimage)
        self.next_button.pack(anchor=S, expand=True)
        self.close_button = tkinter.Button(self.window, text="Close", command=self.close)
        self.close_button.pack(anchor=S, expand=True)
        self.zoom_button = tkinter.Button(self.window, text="Zoom", command=self.zoom)
        self.zoom_button.pack(anchor=S, expand=True)
