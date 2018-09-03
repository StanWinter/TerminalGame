import sys
import time
import random
import math
import os

columns,rows = os.get_terminal_size(1)

# if 0 then all the brackets will appear around the edges
# if 1 then all the brackets will appear 1 space off the edges
BracketDisplacement = 3


def slowprint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

    print('')

def FakeLoading(text, text2 = ""):
    sys.stdout.write(text)
    amount = random.randint(5,12)
    for x in range(amount):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(random.uniform(0.15, 0.15))

    print('')
    print(text2)
    print('')

def FakeLoading(text):
    sys.stdout.write(text[0])
    amount = random.randint(5,12)
    for x in range(amount):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(random.uniform(0.15, 0.15))

    print('')
    print(text[1])
    print('')

def SlowPrintArray(array, extraText = ""):
    lines = len(array)
    for x in range(lines):
        for character in array[x]:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        print('')


    print('')
    slowprint(extraText)

def FullScreenMessage(array):
    columns,rows = get_terminal_size()
    os.system('cls||clear')
    # get all the positions for the start screen
    middlePoint = math.ceil((rows / 2))
    textstart = math.ceil((columns/2) - (len(array[0])/2))
    textstart2 = math.ceil((columns/2) - (len(array[1])/2))
    # Populate screen
    for x in range(rows-1):
        for number in range(columns):
            if x == (0 + BracketDisplacement) and number > BracketDisplacement and number < (columns-1 -BracketDisplacement) or x == (rows - 2  -BracketDisplacement) and number > BracketDisplacement and number <(columns-1 -BracketDisplacement):
                sys.stdout.write("#")
                sys.stdout.flush()
            else:
                if number == (0 + BracketDisplacement) and x > BracketDisplacement-1 and x < (rows-1-BracketDisplacement) or number == (columns-1 -BracketDisplacement) and x > BracketDisplacement-1 and x <(rows-1 -BracketDisplacement):
                    sys.stdout.write("#")
                    sys.stdout.flush()
                elif x == middlePoint and number >= textstart and number <= (textstart + (len(array[0])-1)):
                        textcount = 0
                        for character in array[0]:
                            if textcount == (number - (textstart)):
                                sys.stdout.write(character)
                                sys.stdout.flush()
                                continue
                            textcount +1
                elif x == middlePoint+1 and number >= textstart2 and number <= (textstart2 + (len(array[1])-1)): #ugly fix for now
                        textcount = 0
                        for character in array[1]:
                            if textcount == (number - (textstart2)):
                                sys.stdout.write(character)
                                sys.stdout.flush()
                                continue
                            textcount +1
                else:
                    sys.stdout.write(" ")
                    sys.stdout.flush()

    print('')

