# Converting Image File Formats
Converting all files (.jpg to .png) with Python by Hoyeol Kim

### Converting a Single File
If you want to simply covert a single file (.jpg to .png), use the following code from [SingleFile.py](https://github.com/elibooklover/ConvertingPhotos/blob/master/SingleFile.py):

```python3
from PIL import Image

im = Image.open('photo.jpg')
im.save('photo.png')
```

### Converting Multiple Files
If you want to covert multiple files in a directory, use the following code from [MultipleFiles.py](https://github.com/elibooklover/ConvertingPhotos/blob/master/MultipleFiles.py):

```python3
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
