import sys
import time
import random
import math
import os

columns, rows = os.get_terminal_size(1)

# if 0 then all the brackets will appear around the edges
# if 1 then all the brackets will appear 1 space off the edges
BracketDisplacement = 3
color = ["\033[0;37;40m", #option 0 = white
         "\033[1;31;40m",  #option 1 = red
         "\033[1;32;40m",  #option 2 = green
         "\033[1;36;40m"]  #option 3 = cyan


def slowprint(text, option = 2):
    c1 = option
    if option is not 2:
        if option == 0:
            c1 = 0
        elif option == 1:
            c1 = 1
        elif option == 2:
            c1 = 2
        elif option == 3:
            c1 = 3

    for character in text:
        sys.stdout.write(color[c1]+ character +'\033[0m')
        sys.stdout.flush()
        time.sleep(0.01)

    print('')

def FakeLoading(text, text2 = "", option = 2):
    c1 = option
    if option is not 2:
        if option == 0:
            c1 = 0
        elif option == 1:
            c1 = 1
        elif option == 2:
            c1 = 2
        elif option == 3:
            c1 = 3

    sys.stdout.write(color[2]+ text +'\033[0m')
    amount = random.randint(5,12)
    for x in range(amount):
        sys.stdout.write(color[2]+ "." +'\033[0m')
        sys.stdout.flush()
        time.sleep(random.uniform(0.15, 0.15))

    print('')
    print(color[c1]+text2+'\033[0m')
    print('')

def FakeLoading(text, option = 2):
    c1 = option
    if option is not 2:
        if option == 0:
            c1 = 0
        elif option == 1:
            c1 = 1
        elif option == 2:
            c1 = 2
        elif option == 3:
            c1 = 3

    sys.stdout.write(color[2]+ text[0] +'\033[0m')
    amount = random.randint(5,12)
    for x in range(amount):
        sys.stdout.write(color[2]+ "." +'\033[0m')
        sys.stdout.flush()
        time.sleep(random.uniform(0.15, 0.15))

    print('')
    print(color[c1]+text[1]+'\033[0m')
    print('')

def SlowPrintArray(array, extraText = ""):
    lines = len(array)
    for x in range(lines):
        for character in array[x]:
            sys.stdout.write(color[2]+character+'\033[0m')
            sys.stdout.flush()
            time.sleep(0.01)
        print('')


    print('')
    slowprint(extraText, 2)

def FullScreenMessage(array, option = 2):
    c1 = option
    if option is not 2:
        if option == 0:
            c1 = 0
        elif option == 1:
            c1 = 1
        elif option == 2:
            c1 = 2
        elif option == 3:
            c1 = 3

    os.system('cls||clear')
    # get all the positions for the start screen
    middlePoint = math.ceil((rows / 2))
    textstart = math.ceil((columns/2) - (len(array[0])/2))
    textstart2 = math.ceil((columns/2) - (len(array[1])/2))
    # Populate screen
    for x in range(rows-1):
        for number in range(columns):
            if x == (0 + BracketDisplacement) and number > BracketDisplacement and number < (columns-1 -BracketDisplacement) or x == (rows - 2  -BracketDisplacement) and number > BracketDisplacement and number <(columns-1 -BracketDisplacement):
                sys.stdout.write(color[c1]+"#"+'\033[0m')
                sys.stdout.flush()
            else:
                if number == (0 + BracketDisplacement) and x > BracketDisplacement-1 and x < (rows-1-BracketDisplacement) or number == (columns-1 -BracketDisplacement) and x > BracketDisplacement-1 and x <(rows-1 -BracketDisplacement):
                    sys.stdout.write(color[c1]+"#"+'\033[0m')
                    sys.stdout.flush()
                elif x == middlePoint and number >= textstart and number <= (textstart + (len(array[0])-1)):
                        textcount = 0
                        for character in array[0]:
                            if textcount == (number - (textstart)):
                                sys.stdout.write(color[c1]+character+'\033[0m')
                                sys.stdout.flush()
                                continue
                            textcount +1
                elif x == middlePoint+1 and number >= textstart2 and number <= (textstart2 + (len(array[1])-1)): #ugly fix for now
                        textcount = 0
                        for character in array[1]:
                            if textcount == (number - (textstart2)):
                                sys.stdout.write(color[c1]+character+'\033[0m')
                                sys.stdout.flush()
                                continue
                            textcount +1
                else:
                    sys.stdout.write(color[c1]+" "+'\033[0m')
                    sys.stdout.flush()

    print('')
