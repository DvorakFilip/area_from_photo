from PIL import Image
import numpy as np
from imagedemonstration import save_processed_image

from functions import prettyprint

# ask for path to image, searched color and tolerance
image_path, color, tolerance = "", "", ""

while image_path == "":
    image_path = input("Enter image path: ")
if image_path == "quit":
    quit()

while color == "":
    color = input("Enter RGB value for color (format: '255 255 255'): ")
color = tuple([int(i) for i in color.split(" ")])

while tolerance == "":
    tolerance = input("Enter tolerance value for chosen color (0 - 255): ")
tolerance = int(tolerance)


#temporary
image_path = "testinput/black02.png"
color = (0, 0, 0)



# Convert the image to list of RGB values
img = Image.open(image_path)

img_rgb = img.convert("RGB")
width, height = img_rgb.size

all_rgb_values = list(img_rgb.getdata())


# converting list of RGB values to 2d matrix
rgb_values = []
for i in range(height):
    rgb_values.append(all_rgb_values[width*i:width*(i+1)])



# breadth first search to find all pixels coresponding to one area
def bfs(x, y):
    global rgb_values
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = [(x, y)]
    result = []
    queue = [(x, y)]

    while queue:

        x, y = queue.pop(0)

        rgb_value = rgb_values[y][x]

        #if rgb_values[y][x] == color:
        if (color[0]-tolerance <= rgb_value[0] <= color[0]+tolerance) and (color[1]-tolerance <= rgb_value[1] <= color[1]+tolerance) and (color[2]-tolerance <= rgb_value[2] <= color[2]+tolerance):
            result.append((x, y))



            for direction in directions:
                new_x, new_y = x+direction[0], y+direction[1]
                if ((new_x, new_y) not in visited) and ((new_x >= 0) and (new_x < width)) and ((new_y >= 0) and (new_y < height)):
                    queue.append((new_x, new_y))
                    visited.append((new_x, new_y))

    return result





# iterates through the image to find areas of chosen color
result = []
visited = []
for y, row in enumerate(rgb_values):
    for x, value in enumerate(row):

        if (value == color) and ((x, y) not in visited):
            new_pixels = bfs(x, y)
            visited += new_pixels
            #print(new_pixels)
            result.append(new_pixels)



#prettyprint(rgb_values)
print()


print("Number of areas: ", len(result))

surface_areas = []
rs = []

for i, r in enumerate(result):
    print("Area number: ", i)
    print(len(r), " pixels:")
    print(r)

    # since len(r) is number of pixels of color area, it coresponds to area of a circle
    r = np.sqrt((len(r)/np.pi))
    rs.append(r)
    surface_areas.append(4*np.pi*(r**2))

print("FINAL OUTPUT: ")
print("Average diameter: ", (sum(rs)/len(rs)))
print("Total surface area: ", (sum(surface_areas)))

#bonus - visualize selection
print((f"{image_path.split(".")[0]}_processed.png"))
save_processed_image(img, color, tolerance).save((f"{image_path.split(".")[0]}_processed.png"))

