#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Huy Luong
# Created Date: 07.05.2019
# License: GNU GPL
# =============================================================================
# Imports
from __future__ import print_function
import fnmatch
import os
from wand.api import library
import wand.color
import wand.image
from wand.image import Image
from PIL import Image
from imgreader import find_files
from tkinter import filedialog
from tkinter import *
from PIL import Image
# =============================================================================
#DELETE TRANSPARENCY and CONVERT to PNG
#Copyright: https://stackoverflow.com/a/50898375/11448315

root = Tk()
root.withdraw()

current_directory = filedialog.askdirectory(title="Inputordner")
destination = filedialog.askdirectory(title="Zielordner")

files = find_files(current_directory)
file_modified = files[0].split('.')[0]


for i in files:
    file_modified = i.split('.')[0]
    image = Image.open(current_directory+'/'+i).convert("RGBA")
    new_image = Image.new("RGBA", image.size, "WHITE") # Create a white rgba background
    new_image.paste(image, (0, 0), image)              # Paste the image on the background. Go to the links given below for details.
    new_image.convert('RGB').save(destination+'/'+file_modified+'.png', "PNG")

