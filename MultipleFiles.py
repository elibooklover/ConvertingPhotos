from PIL import Image
import os
directory = r'your directory'
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        prefix = filename.split(".jpg")[0]
        im = Image.open(filename)
        im.save(prefix+'.png')
    else:
        continue
