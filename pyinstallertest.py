import os
from wand.api import library
import wand.color
import wand.image

path = "Datenbank_Monogramme"

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.svg' in file:
            files.append(os.path.join(r, file))



image_binary = None

for f in files  :
    outfile = "SVGtoPNG/" + f.split("\\")[-1].split(".")[0] + ".png"

    with open(f) as f:
        image_binary = f.read()

    svg_blob = image_binary.encode('utf-8')

    with wand.image.Image() as image:
        with wand.color.Color('transparent') as background_color:
            library.MagickSetBackgroundColor(image.wand,
                                             background_color.resource)
        image.read(blob=svg_blob)
        png_image = image.make_blob("png32")

    with open(outfile, "wb") as out:
        out.write(png_image)