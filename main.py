from PIL import Image

from functions import prettyprint

# ask for path to image and searched color
image_path = input("Enter image path: ")
if image_path == "quit":
    quit()
color = input("Enter RGB value for color (format: '255 255 255'): ")
color = tuple([int(i) for i in color.split(" ")])
print(color)
print()

#temporary
image_path = "testinput/black03.png"



# Convert the image to list of RGB values
with Image.open(image_path) as img:

    img = img.convert("RGB")
    width, height = img.size

    all_rgb_values = list(img.getdata())


# converting list of RGB values to 2d matrix
rgb_values = []
for i in range(height):
    rgb_values.append(all_rgb_values[width*i:width*(i+1)])



def bfs(x, y):
    global rgb_values
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = []
    queue = [(x, y)]

    while queue:

        x, y = queue.pop(0)

        if rgb_values[y][x] != color:
            continue

        visited.append((x, y))

        for direction in directions:
            new_x, new_y = x+direction[0], y+direction[1]
            if ((new_x, new_y) not in visited) and ((new_x >= 0) and (new_x < width)) and ((new_y >= 0) and (new_y < height)):
                queue.append((new_x, new_y))

    return visited






result = []
visited = []
for y, row in enumerate(rgb_values):
    for x, value in enumerate(row):

        if (value == color) and ((x, y) not in visited):
            new_pixels = bfs(x, y)
            visited += new_pixels
            #print(new_pixels)
            result.append(new_pixels)




prettyprint(rgb_values)
#print()
print(len(result), result)

