from PIL import Image
import numpy as np


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
#image_path = "image_path_to_override_user_choice.png"
#color = (0, 0, 255)
#tolerance = 135



# Convert the image to list of RGB values
img = Image.open(image_path)

img_rgb = img.convert("RGB")
width, height = img_rgb.size

all_rgb_values = list(img_rgb.getdata())
pixels_processed = img.load()

# converting list of RGB values to 2d matrix
rgb_values = []
for i in range(height):
    rgb_values.append(all_rgb_values[width*i:width*(i+1)])



# breadth first search to find all pixels coresponding to one area
def bfs(x, y):
    global rgb_values
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = set()
    visited.add((x, y))
    result = [(x, y)]
    queue = [(x, y)]


    while queue:

        x, y = queue.pop(0)

        for direction in directions:

            new_x, new_y = x+direction[0], y+direction[1]

            if ((new_x, new_y) not in visited) and ((new_x >= 0) and (new_x < width)) and ((new_y >= 0) and (new_y < height)):

                visited.add((new_x, new_y))
                rgb_value = rgb_values[new_y][new_x]

                if (abs(color[0]-rgb_value[0]) <= tolerance) and (abs(color[1]-rgb_value[1]) <= tolerance) and (abs(color[2]-rgb_value[2]) <= tolerance):
                    queue.append((new_x, new_y))
                    result.append((new_x, new_y))
    

    return result





# iterates through the image to find areas of chosen color
result = []
visited = set()
for y, row in enumerate(rgb_values):

    print(f"{(y/height)*100:.2f} %")

    for x, value in enumerate(row):

        if ((x, y) not in visited):

            if (abs(color[0]-value[0]) <= tolerance) and (abs(color[1]-value[1]) <= tolerance) and (abs(color[2]-value[2]) <= tolerance):
                new_pixels = bfs(x, y)
                visited.update(new_pixels)
                result.append(new_pixels)

            else:
                pixels_processed[x,y] = (100, 100, 100)






# FINAL OUTPUT AND COMPUTING THE AREA
print("Number of areas: ", len(result))

surface_areas = []
rs = []

for i, r in enumerate(result):
    print("Area number: ", i)
    print(len(r), " pixels")

    # since len(r) is number of pixels of color area, it coresponds to area of a circle
    r = np.sqrt((len(r)/np.pi))
    rs.append(r)
    surface_areas.append(4*np.pi*(r**2))

print("FINAL OUTPUT: ")
if len(rs) == 0:
    print("Did not find anything")
    quit()
print("Average diameter: ", (sum(rs)/len(rs)))
print("Total surface area: ", (sum(surface_areas)))

#Creates image mask for chosen color
output = f"{image_path.split(".")[0]}_processed2.png" 
print((output))
img.save(output)

