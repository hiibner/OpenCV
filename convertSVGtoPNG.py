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

#Copyright©: https://stackoverflow.com/questions/6589358/convert-svg-to-png-in-python/19718153\#19718153
#Convert SVG to PNG

#Inputordner und Zielordner auswählen
root = Tk()
root.withdraw()

current_directory = filedialog.askdirectory(title="SVG Ordner")

destination = filedialog.askdirectory(title="Zielordner")

matches = []
for root, dirnames, filenames in os.walk(current_directory):
    for filename in fnmatch.filter(filenames, '*.svg'):
        matches.append(os.path.join(root, filename))

for x in matches:
    head,tail = os.path.split(x)
    filename, ext =  os.path.splitext(tail)
    outputname = filename + ".png"
    with open(x) as f:
        image_binary = f.read()

    svg_blob = image_binary.encode('utf-8')


    with wand.image.Image() as image:
        with wand.color.Color('transparent') as background_color:
            library.MagickSetBackgroundColor(image.wand,
                                             background_color.resource)
        image.read(blob=svg_blob)
        png_image = image.make_blob("png32")

    with open(destination+"\\"+outputname, "wb") as out:
        out.write(png_image)