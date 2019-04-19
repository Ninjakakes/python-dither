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
        # image = image.convert('L')
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