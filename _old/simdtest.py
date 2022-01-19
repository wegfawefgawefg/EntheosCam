from PIL import Image

impath = "/home/vega/Coding/EntheosCam/cat.png"
im = Image.open(impath)
im = im.rotate(45)
im.save("/home/vega/Coding/EntheosCam/cat_out.png")