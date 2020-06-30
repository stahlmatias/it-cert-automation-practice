import os, sys
from PIL import Image

for infile in sys.argv[1:]:
  f, e = os.path.splitext(infile)
  outfile = f + ".jpg"
  if infile != outfile:
    try:
      with Image.open(infile) as im:
        outfile = im.resize((128, 128))
        outfile = im.rotate(45) # degrees counter-clockwise
        im.save(outfile)
    except IOError:
      print("cannot convert", infile)


