from PIL import Image
import glob, os

size = 128, 128

for infile in glob.glob("images/*.thumbnail"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(file + "_thumbnail.jpg", "JPEG")
