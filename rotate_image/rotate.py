from PIL import Image

Image1 = Image.open("input.jpg")

Image1.rotate(90).save("output.jpg")

Image1.show("output.jpg")
