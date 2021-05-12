from PIL import Image, ImageFilter
import os

Image1 = Image.open(os.getcwd() + "\\input.jpg")
Image1.convert(mode="L").save(os.getcwd() + "\\output.jpg")
