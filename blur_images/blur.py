from PIL import Image, ImageFilter

import os


Image1 = Image.open(os.getcwd() + "\\input.jpg")

Image1.filter(ImageFilter.GaussianBlur(15)).save(os.getcwd() + "\\output.jpg")
