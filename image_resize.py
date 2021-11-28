from PIL import Image
import os, sys
from os import listdir
from os.path import isfile, join


onlyfiles = [f for f in listdir("/Users/zheyu/Downloads/COMP 89/Presentation") if isfile(join("/Users/zheyu/Downloads/COMP 89/Presentation", f))]
path = "Presentation/"
def resize():
    for item in onlyfiles:
        if not item.startswith('.'):
            if os.path.isfile(path+item):
                im = Image.open(path+item)
                f, e = os.path.splitext(path+item)
                imResize = im.thumbnail([384,256], Image.ANTIALIAS)
                #imResize = im.resize((384,256), Image.ANTIALIAS)
                imResize.save(f + '.jpg', 'JPEG', quality=90)

resize()