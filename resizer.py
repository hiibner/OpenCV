#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Huy Luong
# Created Date: 07.05.2019
# License: GNU GPL
# =============================================================================
# Imports
import cv2
import numpy as np
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# =============================================================================

#Copyright© resize vijay jha /https://stackoverflow.com/questions/44650888/resize-an-image-without-distortion-opencv/49208362#49208362
def resize(image,square_size):
    """
    Resizes a image so a SQUARE with given size(param:square_size)
    """
    height,width=image.shape
    if(height>width):
      differ=height
    else:
      differ=width
    differ+=4

    mask = np.zeros((differ,differ), dtype="uint8")
    mask = cv2.bitwise_not(mask)

    x_pos=int((differ-width)/2)
    y_pos=int((differ-height)/2)

    mask[y_pos:y_pos+height,x_pos:x_pos+width]=image[0:height,0:width]

    mask=cv2.resize(mask,(square_size,square_size),interpolation=cv2.INTER_AREA)

    return mask


# convert and rgb2qimage Copyright© Dr. rer. nat. Hans Meine URL: https://kogs-www.informatik.uni-hamburg.de/~meine/software/vigraqt/qimage2ndarray.py
def convert(gray):
    """Convert the 2D numpy array `gray` into a 8-bit QImage with a gray
    colormap.  The first dimension represents the vertical image axis."""
    if len(gray.shape) != 2:
        raise ValueError("gray2QImage can only convert 2D arrays")

    h, w = gray.shape
    bytesPerLine = 1 * w
    result = QImage(gray.data, w, h, bytesPerLine, QImage.Format_Grayscale8)
    result.ndarray = gray
    for i in range(256):
        result.setColor(i, QColor(i, i, i).rgb())
    return result

def rgb2qimage(rgb):
	"""Convert the 3D numpy array `rgb` into a 32-bit QImage.  `rgb` must
	have three dimensions with the vertical, horizontal and RGB image axes."""
	if len(rgb.shape) != 3:
		raise ValueError("rgb2QImage can expects the first (or last) dimension to contain exactly three (R,G,B) channels")
	if rgb.shape[2] != 3:
		raise ValueError("rgb2QImage can only convert 3D arrays")

	h, w, channels = rgb.shape

	# Qt expects 32bit BGRA data for color images:
	bgra = np.empty((h, w, 4), np.uint8, 'C')
	bgra[...,0] = rgb[...,2]
	bgra[...,1] = rgb[...,1]
	bgra[...,2] = rgb[...,0]
	bgra[...,3].fill(255)

	result = QImage(bgra.data, w, h, QImage.Format_RGB32)
	result.ndarray = bgra
	return result