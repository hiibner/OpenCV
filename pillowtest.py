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

# GIF to JPG

from PIL import Image



files = find_files("monoconverted")

file_modified = files[0].split('.')[0]


for i in files:
    file_modified = i.split('.')[0]
    image = Image.open('monoconverted/'+i).convert("RGBA")
    new_image = Image.new("RGBA", image.size, "WHITE") # Create a white rgba background
    new_image.paste(image, (0, 0), image)              # Paste the image on the background. Go to the links given below for details.
    new_image.convert('RGB').save('monoconverted2/'+file_modified+'.jpg', "JPEG")