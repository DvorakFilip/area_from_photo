from PIL import Image
import numpy as np

def save_processed_image(img, color, tolerance):

    final_data = []
    blackcolor = (0, 0, 0)
    if color == blackcolor:
        blackcolor = (100, 100, 100)

    for pixel in img.getdata():
        if (color[0]-tolerance <= pixel[0] <= color[0]+tolerance) and (color[1]-tolerance <= pixel[1] <= color[1]+tolerance) and (color[2]-tolerance <= pixel <= color[2]+tolerance):
            final_data.append(pixel)
        else:
            final_data.append(blackcolor)
    
    final_image = Image.new(img.mode, img.size)
    final_image.putdata(final_data)

    return final_image