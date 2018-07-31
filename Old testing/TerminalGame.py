import cmd
import textwrap
import sys
import os
import time
import random
import math
from TerminalGameTools import slowprint, FakeLoading

StartMenuText = ["start","help","quit"]
BootScreenText = ["SYSTEM LOCKED","PLEASE INSERT USB KEY"]
HelpScreenText = ["Connect [IP]            connects to a other pc, enter IP at [IP]",
                  "Login   [TYPE] [CODE]   login on a other pc, enter type at [TYPE] and code at [CODE]"]
HelpScreenText2 =["Change  [TYPE] [AMOUNT] Changes the amount of the object, enter type at [TYPE] and amount at [AMOUNT]",
                  "Exit                    Saves the final changes and exit the program"]

Commands = ["connect","login","change","exit"]
ip = "127.0.0.1"
LoginCodes = ["p_transport", "r45ghh"]
transportMinAmount = 6
columns, rows = os.get_terminal_size(1)
FirstStart = 1

# PLAYER DATA
class player:
    def __init__(self):
        self.CableConnected = False
        self.ConnectionOnline = False
        self.LogedIn = False
        self.UsbConnected = False
        self.GameStarted = False
        self.GameWon = False
myPlayer = player()

# Screen the player will see on startup
def TitleScreen():

    os.system('cls||clear')
    # get all the positions for the start screen
    middlePoint = math.ceil((rows / 2))
    textstart = math.ceil((columns/2) - (len(BootScreenText[0])/2))
    textstart2 = math.ceil((columns/2) - (len(BootScreenText[1])/2))
    # Populate screen
    for x in range(rows-1):
        for number in range(columns):
            if x == 0 or x == rows-2:
                sys.stdout.write("#")
                sys.stdout.flush()
            else:
                if number == 0 or number == columns-1:
                    sys.stdout.write("#")
                    sys.stdout.flush()
                elif x == middlePoint and number >= textstart and number <= (textstart + (len(BootScreenText[0])-1)):
                        textcount = 0
                        for character in BootScreenText[0]:
                            if textcount == (number - (textstart)):
                                sys.stdout.write(character)
                                sys.stdout.flush()
                                continue
                            textcount +1
                elif x == middlePoint+1 and number >= textstart2 and number <= (textstart2 + (len(BootScreenText[1])-1)): #ugly fix for now
                        textcount = 0
                        for character in BootScreenText[1]:
                            if textcount == (number - (textstart2)):
                                sys.stdout.write(character)
                                sys.stdout.flush()
                                continue
                            textcount +1
                else:
                    sys.stdout.write(" ")
                    sys.stdout.flush()

    print('')
    TitleScreen_Selections()

#--------------------------------------------------------------------
# selection menu (for dev purposes)
def TitleScreen_Selections():
    while True:
        option = TextInput()
        if option == StartMenuText[0]:
            myPlayer.GameStarted = True
            os.system('cls||clear')
            StartGame()
            break
        # elif option == StartMenuText[1]:
        #     HelpMenu()
        #     break
        elif option == StartMenuText[2]:
            sys.exit()
        else:
            slowprint("DEV START SCREEN ENTER START")
#--------------------------------------------------------------------

def StartGame():
    global FirstStart
    if FirstStart == 1:
        slowprint("PLEASE ENTER A COMMAND, FOR INSTRUCTIONS ENTER HELP")
        FirstStart = 0

    while True:
        option = TextInput()
        if Commands[0] in option:
            if str(ip) in option:
                ConnectMenu(True)
                break
            else:
                ConnectMenu(False)
                break
        elif Commands[1] in option:
            if LoginCodes[0] in option and LoginCodes[1] in option:
                LoginMenu(True, 0)
                break
            elif LoginCodes[0] in option:
                LoginMenu(False, 1)
                break
            elif LoginCodes[1] in option:
                LoginMenu(False, 2)
                break
            else:
                LoginMenu(False, 3)
                break
        elif option == StartMenuText[1]:
            HelpMenu()
            break
        elif myPlayer.LogedIn == True and Command[2] in option:
            ChangeAmountMenu()
            break
        elif myPlayer.LogedIn == True and option is Command[3]:
            ExitMenu()
            break
        else:
            slowprint("PLEASE ENTER A VALID COMMAND, FOR INSTRUCTIONS ENTER HELP")
#--------------------------------------------------------------------
def HelpMenu():
    if myPlayer.GameStarted == False:
        os.system('cls||clear')

    index = 0
    for x in HelpScreenText:
        slowprint(HelpScreenText[index])
        index= index + 1
    if myPlayer.LogedIn == True:
        index = 0
        for x in HelpScreenText2:
            slowprint(HelpScreenText2[index])
            index= index + 1

    if myPlayer.GameStarted == False:
        TitleScreen_Selections()
    else:
        StartGame()
#--------------------------------------------------------------------
def ConnectMenu(RightCode):
    if RightCode == True and myPlayer.CableConnected == True:
        os.system('cls||clear')
        myPlayer.ConnectionOnline = True
        FakeLoading("CONNECTING","CONNECTION ESTABLISHED")
        StartGame()
    elif myPlayer.CableConnected == False:
        slowprint("ERROR: NOT CONNECTED TO THE INTERNET")
        StartGame()
    else:
        slowprint("ERROR: CANT CONNECT TO IP")
        StartGame()
#--------------------------------------------------------------------
def LoginMenu(RightData, ErrorCode):
    if RightData == True:
        myPlayer.LogedIn = True
        FakeLoading("CONNECTING","LOGIN SUCCESFULL, NEW ENTRYS HAVE BEEN ADDED TO THE HELP LIST")
    elif ErrorCode == 2:
        slowprint("ERROR: TYPE IS NOT RECOGNISED")
        StartGame()
    elif ErrorCode == 1:
        slowprint("ERROR: AMOUNT IS NOT VALID")
        StartGame()
    elif ErrorCode == 3:
        slowprint("ERROR: TYPE AND AMOUNT NOT SPECIFED")
        StartGame()

#--------------------------------------------------------------------
def ChangeAmountMenu():
        print("hier gebleven")

#--------------------------------------------------------------------
def ExitMenu():
        print("hier gebleven")

#--------------------------------------------------------------------

# here we can catch text before its used
def TextInput():
    text = input().lower()
    if text == "cable":
        myPlayer.CableConnected = True
        print("Cable active")
    elif text == "quit":
        sys.exit()

    return text
#--------------------------------------------------------------------

TitleScreen()
