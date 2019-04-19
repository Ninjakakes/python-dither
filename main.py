from math import floor
from PIL import Image
import tkinter
import tkinter.filedialog

import os, sys

def setup():
    global image
    root = tkinter.Tk()
    root.withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = tkinter.filedialog.askopenfilename(filetypes = (("image files","*.jpg *.png *.gif"),("all files","*.*"))) # show an "Open" dialog box and return the path to the selected file
    try:
        image = Image.open(filename)
        image = image.convert('L')
        image = image.convert('RGB')
    except:
        sys.exit()
    root.destroy()
    # image.show()

def main():
    width, height = image.size
    pixel = image.load()

    for y in range(1, height):
        for x in range(1, width):
            oldR, oldG, oldB = pixel[x, y]

            newR = apply_thershold(oldR, 4)
            newB = apply_thershold(oldB, 4)
            newG = apply_thershold(oldG, 4)

            pixel[x, y] = newR, newG, newB

            errR = oldR - newR
            errG = oldG - newG
            errB = oldB - newB

            if x < width - 1:
                red = pixel[x+1, y][0] + round(errR * 7/16)
                green = pixel[x+1, y][1] + round(errG * 7/16)
                blue = pixel[x+1, y][2] + round(errB * 7/16)

                pixel[x+1, y] = (red, green, blue)

            if x > 1 and y < height - 1:
                red = pixel[x-1, y+1][0] + round(errR * 3/16)
                green = pixel[x-1, y+1][1] + round(errG * 3/16)
                blue = pixel[x-1, y+1][2] + round(errB * 3/16)

                pixel[x-1, y+1] = (red, green, blue)

            if y < height - 1:
                red = pixel[x, y+1][0] + round(errR * 5/16)
                green = pixel[x, y+1][1] + round(errG * 5/16)
                blue = pixel[x, y+1][2] + round(errB * 5/16)

                pixel[x, y+1] = (red, green, blue)

            if x < width - 1 and y < height - 1:
                red = pixel[x+1, y+1][0] + round(errR * 1/16)
                green = pixel[x+1, y+1][1] + round(errG * 1/16)
                blue = pixel[x+1, y+1][2] + round(errB * 1/16)

                pixel[x+1, y+1] = (red, green, blue)

            # pixel[x, y] = (newR, newG, newB)


    image.show()
            

def apply_thershold(value, color_amount=2):
    if color_amount == 1:
        b = 1
    else:
        b = color_amount - 1
    new_value = int(round(b * value / 255) * (255/b))
    return new_value

if __name__ == '__main__':
    setup()
    main()