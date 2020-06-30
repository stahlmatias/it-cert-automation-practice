#!/usr/bin/env python3

from PIL import Image
import os

path = '/home/student-02-248546686053/images'

for r, d, f in os.walk(path):
  for name in f:
    outfile = "/opt/icons/" + name + ".jpg"
    print(outfile)
    try:
      with Image.open(path+'/'+name) as img:
        img = img.convert("RGB")
        img = img.resize((128, 128))
        img = img.rotate(-90)
        img.save(outfile)
    except IOError:
      print("cannot convert", path+'/'+name)
                                                        
