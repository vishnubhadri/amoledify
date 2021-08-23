#!/usr/bin/python

import sys, getopt, re, time
from PIL import Image

VERSION="0.0.1"
inputfile = ""
outputfile = "output.jpg"
toleranceLevel = 32
colors = [(32, 32, 32)]
_tolerance = []
BLACK = (0, 0, 0)  # AMOLED OFF

######PROGRESS BAR ###########
from progressbar import *  # just a simple progress bar


def setupProcessBar(pixels):
    widgets = [
        "Converting: ",
        Percentage(),
        " ",
         AnimatedMarker(),
        " ",
        ETA(),
        " ",
        FileTransferSpeed(unit='Pixels')
    ]  # see docs for other options
    global pbar
    pbar = ProgressBar(widgets=widgets, maxval=pixels)
    pbar.start()


def main(argv):
    global inputfile
    global outputfile
    global toleranceLevel
    global colors
    global VERSION
    try:
        opts, args = getopt.getopt(argv, "vhi:o:t:c:", ["ifile=", "ofile=", "t", "c"])
    except getopt.GetoptError:
        print(
            "amoledify.py -i <path/to/inputfile> -o <path/to/outputfile> [-t <toleranceLevel> / -c <(00,00,00),(11,11,11),...> (in rgb 0-255)"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-v":
            print(VERSION)
            sys.exit()
        elif opt == "-h":
            print("amoledify.py -i <path/to/inputfile> -o <path/to/outputfile> [-t <toleranceLevel> / -c <(00,00,00),(11,11,11),...> (in rgb 0-255)")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-t", "--tolerance"):
            if toleranceLevel < 0 and toleranceLevel > 255:
                print("Tolerance should be between 0 to 255")
                sys.exit()
            else:
                toleranceLevel = int(arg)
        elif opt in ("-c", "--color"):
            colors.clear()
            for tup in re.findall(r"\([,\d]*\)", arg):
                r, g, b = 0, 0, 0
                r, g, b = tup[1:-1].split(",")
                colors.append(tuple([int(r), int(g), int(b)]))

    if inputfile == "":
        print("Please specify using -i <path/to/inputfile> ")
        sys.exit()


def reduceHexValue(color, value, condition):
    computedColor = int(color)
    if condition == "p":
        c = computedColor + value
        if c > 255:
            c = 255
    if condition == "n":
        c = computedColor - value
        if c < 0:
            c = 0
    return c


def computeTolerance(color):
    r, g, b = color
    for value in range(0, toleranceLevel):
        least = (
            reduceHexValue(r, value, "p"),
            reduceHexValue(g, value, "p"),
            reduceHexValue(b, value, "p"),
        )
        most = (
            reduceHexValue(r, value, "n"),
            reduceHexValue(g, value, "n"),
            reduceHexValue(b, value, "n"),
        )
        _tolerance.append(least)
        _tolerance.append(most)


def changeColor():
    picture = Image.open(inputfile).convert("RGB")
    width, height = picture.size
    setupProcessBar(width * height)
    # processbar Increment
    incr = 0
    # Process every pixel
    for x in range(0, width):
        for y in range(0, height):
            current_color = picture.getpixel((x, y))
            pbar.update(incr)
            incr = incr + 1
            if current_color in _tolerance:
                picture.putpixel((x, y), BLACK)
    picture.save(outputfile)
    pbar.finish()
    print("Picture Saved at ", outputfile)


if __name__ == "__main__":
    main(sys.argv[1:])
    for color in colors:
        computeTolerance(color)
    changeColor()
    print("Done.. Thank you for using amoledify.py")
