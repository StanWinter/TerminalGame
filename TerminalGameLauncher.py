import cmd
import textwrap
import sys
import os
import time
import random
import math
from TerminalGameTools import slowprint, FakeLoading, SlowPrintArray, FullScreenMessage

StartMenuText = ["start","help","quit"]
BootScreenText = ["SYSTEM LOCKED","PLEASE INSERT USB KEY"]
EndScreenText = ["CHANGES SAVED","PLEASE TRANSPORT THE PRISONERS"]
EndScreenExitGameText = ["SYSTEM UNLOCKED","PLEASE ENTER 1 TO START"]

Commands = ["1","2","3","4"]
CommandsText = ["1 = CONNECT TO COMPUTER","2 = LOGIN TO COMPUTER",
                "3 = EDIT PRISONER TRANSPORT MANIFEST","4 = SAVE CHANGES AND EXIT"]
TransportMenuText = ["1 = CANCEL TRANSPORT","2 = CHANGE PRISONER AMOUNT FOR TRANSPORT",
                     "3 = DELAY TRANSPORT","4 = RETURN TO LAST MENU"]
ExitMenuText = ["1 = YES", "2 = NO"]

ip = "127.0.0.1"
LoginCode = "12345"
TransportNumber = "101"
TransportMinAmount = "6"
columns, rows = os.get_terminal_size(1)
FirstLoad = True

# PLAYER DATA
class player:
    def __init__(self):
        self.CableConnected = False
        self.ConnectionOnline = False
        self.LogedIn = False
        self.UsbConnected = False
        self.GameStarted = False
        self.TransportManifestCompleted = False
        self.GameWon = False
myPlayer = player()

# Screen the player will see on startup
def TitleScreen():
    FullScreenMessage(BootScreenText)
    TitleScreen_Selections()

#--------------------------------------------------------------------
# selection menu (for dev purposes)
def TitleScreen_Selections():
    while True:
        option = TextInput()
        if option == StartMenuText[0]:
            myPlayer.GameStarted = True
            os.system('cls||clear')
            FakeLoading("INSTALLING KEYCRACKER.PY", "INSTALL COMPLETED")
            slowprint("ACCES GRANTED")
            time.sleep(2.00)
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
    global FirstLoad
    if FirstLoad == False:
        time.sleep(1.00)
    else:
        FirstLoad = False

    os.system('cls||clear')
    SlowPrintArray(CommandsText, "PLEASE ENTER A COMMAND")

    while True:
        option = TextInput()
        if Commands[0] == option: #1 = CONNECT TO COMPUTER
            ConnectMenu()
            break
        elif Commands[1] == option: #2 = LOGIN TO COMPUTER
            LoginMenu()
            break
        elif Commands[2] == option: #3 = EDIT PRISONER TRANSPORT MANIFEST
            ChangeAmountMenu()
            break
        elif Commands[3] == option: #4 = SAVE CAHNGES AND EXIT
            ExitMenu()
            break
        else:
            slowprint("PLEASE ENTER A VALID COMMAND")
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
def ConnectMenu():
    os.system('cls||clear')

    if myPlayer.CableConnected == False:
        slowprint("ERROR: NOT CONNECTED TO THE INTERNET")
        StartGame()
    else:
        slowprint("PLEASE ENTER THE IP YOU WANT TO CONNECT TO")
        while True:
            option = TextInput()
            if myPlayer.CableConnected == True and ip in option:
                os.system('cls||clear')
                myPlayer.ConnectionOnline = True
                FakeLoading("CONNECTING","CONNECTION ESTABLISHED")
                StartGame()
                break
            else:
                slowprint("ERROR: CANT CONNECT TO IP")
                StartGame()
                break
#--------------------------------------------------------------------
def LoginMenu():
    os.system('cls||clear')

    if myPlayer.CableConnected == False:
        slowprint("ERROR: NOT CONNECTED TO THE INTERNET")
        StartGame()
    elif myPlayer.ConnectionOnline == False:
        slowprint("ERROR: NOT CONNECTED TO A OTHER COMPUTER")
        StartGame()
    elif myPlayer.ConnectionOnline == True and myPlayer.CableConnected == True:
        while True:
            slowprint("PLEASE ENTER PASSWORD")
            option = TextInput()
            if LoginCode == option:
                myPlayer.LogedIn = True
                FakeLoading("CONNECTING","LOGIN SUCCESFULL")
                StartGame()
            else:
                slowprint("ERROR: PASSWORD INCORRECT")

#--------------------------------------------------------------------
def ChangeAmountMenu():
    os.system('cls||clear')

    if myPlayer.CableConnected == False:
        slowprint("ERROR: NOT CONNECTED TO THE INTERNET")
        StartGame()
    elif myPlayer.ConnectionOnline == False:
        slowprint("ERROR: NOT CONNECTED TO A OTHER COMPUTER")
        StartGame()
    elif myPlayer.LogedIn == False:
        slowprint("ERROR: NOT LOGGED IN")
        StartGame()
    else:
        slowprint("PLEASE ENTER TRANSPORT NUMBER")
        while True:
            option = TextInput()
            if option == TransportNumber:
                FakeLoading("SEARCHING","SEARCH COMPLETED")
                TransportMenu()
                break
            else:
                FakeLoading("SEARCHING","SEARCH FAILED")
                StartGame()
                break

#--------------------------------------------------------------------
def TransportMenu():
    time.sleep(1.00)
    os.system('cls||clear')
    SlowPrintArray(TransportMenuText, "PLEASE ENTER A COMMAND")

    while True:
        option = TextInput()
        if Commands[0] == option: #1 = CANCEL TRANSPORT
            slowprint("ADMINISTRATOR ACCESS REQUIRED")
        elif Commands[2] == option: #3 = DELAY TRANSPORT
            slowprint("ADMINISTRATOR ACCESS REQUIRED")
        elif Commands[3] == option: #4 = RETURN TO LAST MENU
            StartGame()
            break
        elif Commands[1] == option: #2 = CHANGE PRISONER AMOUNT FOR TRANSPORT
            PrisonerAmount()
            break
        else:
            slowprint("PLEASE ENTER A VALID COMMAND")
#--------------------------------------------------------------------
def PrisonerAmount():
    slowprint("PLEASE ENTER THE AMOUNT OF PRISONERS THAT NEED TO BE TRANSPORTED")
    while True:
        option = TextInput()
        if option == TransportMinAmount:
            myPlayer.TransportManifestCompleted = True
            FakeLoading("PROCESSING","TASK COMPLETED PLEASE SAVE THE CHANGES AND CARRY ON WITH YOUR WORK")
            time.sleep(1.00)
            StartGame()
        else:
            FakeLoading("PROCESSING","ERROR: INVALID NUMBER")
            TransportMenu()
#--------------------------------------------------------------------
def ExitMenu():
    os.system('cls||clear')

    if myPlayer.TransportManifestCompleted == True:
        slowprint("FILE CHANGES DETECTED, PLEASE EXIT TO SAVE CHANGES")
    else:
        slowprint("NO FILE CHANGES DETECTED, ARE YOU SURE YOU WANT TO EXIT?")
        slowprint("ALL PROGRESS WILL BE LOST!")

    print('')
    SlowPrintArray(ExitMenuText, "PLEASE ENTER A COMMAND")

    while True:
        option = TextInput()
        if Commands[0] == option: #1 = YES
            if myPlayer.TransportManifestCompleted == True:
                myPlayer.GameWon = True
                #execute opening door code or something here
                EndScreen(True)
                break
            else:
                myPlayer.ConnectionOnline = False
                myPlayer.LogedIn = False
                myPlayer.GameStarted = False
                myPlayer.TransportManifestCompleted = False
                myPlayer.GameWon = False
                FirstLoad = True
                EndScreen(False)
                break
        elif Commands[1] == option: #2 = NO
            StartGame()
            break
#--------------------------------------------------------------------
def EndScreen(type):

    if type == False: # wrong end, player can start again
        FullScreenMessage(EndScreenExitGameText)
        while True:
            option = TextInput()
            if Commands[0] == option:
                StartGame()
                break
    elif type == True: # right end
        FullScreenMessage(EndScreenText)
#--------------------------------------------------------------------

# here we can catch text before its used
def TextInput():
    text = input().lower()
    #print(text)
    if text == "cable":
        myPlayer.CableConnected = True
        print("Cable active")
    elif text == "quit":
        sys.exit()
    elif text == "transportmenu":
        TransportMenu()
    return text
#--------------------------------------------------------------------

TitleScreen()
