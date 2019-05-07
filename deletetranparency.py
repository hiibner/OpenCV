from __future__ import print_function
import fnmatch
import os
from wand.api import library
import wand.color
import wand.image
from wand.image import Image
from PIL import Image
from imgreader import find_files

# files = find_files("mono")
#
# file_modified = files[0].split('.')[0]
#
#
# for i in files:
#     file_modified = i.split('.')[0]
#
#     Image.open("mono/"+i).save('monoconverted/'+file_modified+'.png', 'PNG')

# GIF to PNG
#######
#DELETE TRANSPARENCY
from PIL import Image



files = find_files("SVGtoPNG")

file_modified = files[0].split('.')[0]


for i in files:
    file_modified = i.split('.')[0]
    image = Image.open('SVGtoPNG/'+i).convert("RGBA")
    new_image = Image.new("RGBA", image.size, "WHITE") # Create a white rgba background
    new_image.paste(image, (0, 0), image)              # Paste the image on the background. Go to the links given below for details.
    new_image.convert('RGB').save('SVGtoPNGtoRGB/'+file_modified+'.png', "PNG")

###################

#Convert SVG to PNG

# matches = []
# for root, dirnames, filenames in os.walk('Datenbank_Monogramme'):
#     for filename in fnmatch.filter(filenames, '*.svg'):
#         matches.append(os.path.join(root, filename))
#
# for x in matches:
#     head,tail = os.path.split(x)
#     filename, ext =  os.path.splitext(tail)
#     outputname = filename + ".png"
#     with open(x) as f:
#         image_binary = f.read()
#
#     svg_blob = image_binary.encode('utf-8')
#
#
#     with wand.image.Image() as image:
#         with wand.color.Color('transparent') as background_color:
#             library.MagickSetBackgroundColor(image.wand,
#                                              background_color.resource)
#         image.read(blob=svg_blob)
#         png_image = image.make_blob("png32")
#
#     with open("SVGtoPNG"+"\\"+outputname, "wb") as out:
#         out.write(png_image)