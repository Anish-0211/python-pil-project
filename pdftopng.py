# The pdf2image library can be used
# pYou can install it simply using,

# pip install pdf2image
# Once installed you can use following code to get images.

from pdf2image import convert_from_path

pages = convert_from_path(
    "A:\Projects\Pdf\coursera.pdf",
    500,
    poppler_path=r"A:\Projects\Pdf\poppler-0.68.0\bin",
)

# Saving pages in jpeg format

for page in pages:
    page.save("out.jpg", "JPEG")
