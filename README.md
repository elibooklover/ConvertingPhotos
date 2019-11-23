# ConvertingPhotos
Converting all files (.jpg to png) in Python

If you want to simply covert a single file (.jpg to .png), use the following code:

```
import Image

im = Image.open('photo.jpg')
im.save('photo.png')
```

If you want to covert multiple files in a directory, use [the following code from coverter.py](https://github.com/elibooklover/ConvertingPhotos/blob/master/converter.py):

```
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
```
