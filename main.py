from PIL import Image

from functions import prettyprint

image_path = input("Enter image path: ")
important_color = input("Enter RGB value for color: ")
print()
image_path = "testinput/black03.png"

if image_path == "quit":
    quit()



with Image.open(image_path) as img:

    img = img.convert("RGB")
    width, height = img.size

    rgb_values = list(img.getdata())

#print(width, height)
#prettyprint(rgb_values, width)
