import cmd,textwrap,sys,os,time,pyudev,multiprocessing,datetime,json,urllib,urllib.request
import TerminalGameLanguage,TerminalGameMYSQL, TerminalGameIPInput
import RPi.GPIO as GPIO
from TerminalGameTools import slowprint, FakeLoading, SlowPrintArray, FullScreenMessage
#from TerminalGameFolderChecker import GetPlayerAmount # not used anymore, is still an option is case something doesnt work
from TerminalGameMYSQL import PlayersInformation 
from multiprocessing import Process, Value
from flask import Flask, request


context = pyudev.Context()
columns, rows = os.get_terminal_size(1)
FirstLoad = True

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
DEVMODE = True # SET TO FALSE IF NOT USED
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# codes the player needs to enter
ip = "127.0.0.1"
LoginCode = "12345"
TransportNumber = "101"
TransportAmount = 0

#data we get from MYSQL
LastMessageTime = "2000-10-02 01:03:46" #just leave this
uid = 0

#gpio variables for lan connection test
GPIO.setmode(GPIO.BCM) #referring to the pins by the "Broadcom SOC channel" number
GPIO.setwarnings(False) #disable GPIO warnings
keyBtnGpio = 17
GPIO.setup(keyBtnGpio, GPIO.IN, pull_up_down=GPIO.PUD_UP) #key


class TextAndInput:
    def __init__(self):
        # inputs made by player/dev
        self.DevInputText = ["start","help","quit"]
        self.InputCommands = ["1","2","3","4"]
        # screen text for special screens
        self.BootScreenLockedText = ["SYSTEM LOCKED","PLEASE INSERT USB KEY"]
        self.BootScreenUnlockedText = ["SYSTEM UNLOCKED","PLEASE ENTER 1 TO START"]
        self.EndScreenText = ["CHANGES SAVED","PLEASE TRANSPORT THE PRISONERS"]
        # options text shown to the player
        self.InputCommandsText = ["1 = CONNECT TO COMPUTER","2 = LOGIN TO COMPUTER",
                          "3 = EDIT PRISONER TRANSPORT MANIFEST","4 = SAVE CHANGES AND EXIT"]
        self.TransportMenuText = ["1 = CANCEL TRANSPORT","2 = CHANGE PRISONER AMOUNT FOR TRANSPORT",
                          "3 = DELAY TRANSPORT","4 = RETURN TO LAST MENU"]
        self.ExitMenuText = ["1 = YES", "2 = NO"]
        # all other text
        self.FakeLoadingText1 = ["INSTALLING KEYCRACKER.PY", "INSTALL COMPLETED"]
        self.ACCESSGRANTEDTEXT = "ACCESS GRANTED"
        self.PLEASEENTERCOMMANDTEXT = "PLEASE ENTER A COMMAND"
        self.PLEASEENTERAVALIDCOMMANDTEXT = "PLEASE ENTER A VALID COMMAND"
        self.ConnectText1 = "ERROR: NOT CONNECTED TO THE INTERNET"
        self.ConnectText2 = "PLEASE ENTER THE IP YOU WANT TO CONNECT TO"
        self.ConnectText3 = "ERROR: CANT CONNECT TO IP"
        self.ConnectFakeLoadingText1 = ["CONNECTING","CONNECTION ESTABLISHED"]
        self.LoginText1 = "ERROR: NOT CONNECTED TO THE INTERNET"
        self.LoginText2 = "ERROR: NOT CONNECTED TO A OTHER COMPUTER"
        self.LoginText3 = "PLEASE ENTER PIN CODE"
        self.LoginText4 = "ERROR: PINCODE INCORRECT, RETURNING TO MENU"
        self.LoginFakeLoadingText1 = ["CONNECTING","LOGIN SUCCESFULL"]
        self.ChangeAmountText1 = "ERROR: NOT CONNECTED TO THE INTERNET"
        self.ChangeAmountText2 = "ERROR: NOT CONNECTED TO A OTHER COMPUTER"
        self.ChangeAmountText3 = "ERROR: NOT LOGGED IN"
        self.ChangeAmountText4 = "PLEASE ENTER TRANSPORT NUMBER"
        self.ChangeAmountFakeLoadingText1 = "SEARCHING","SEARCH COMPLETED"
        self.ChangeAmountFakeLoadingText2 = "SEARCHING","SEARCH FAILED"
        self.TransportText1 = "ADMINISTRATOR ACCESS REQUIRED"
        self.PrisonerText1 = "PLEASE ENTER THE AMOUNT OF PRISONERS THAT NEED TO BE TRANSPORTED"
        self.PrisonerFakeLoadingText1 = ["PROCESSING","TASK COMPLETED PLEASE SAVE THE CHANGES AND CARRY ON WITH YOUR WORK"]
        self.PrisonerFakeLoadingText2 = ["PROCESSING","ERROR: INVALID NUMBER"]
        self.ExitMenuText1 = "FILE CHANGES DETECTED, PLEASE EXIT TO SAVE CHANGES"
        self.ExitMenuText2 = "NO FILE CHANGES DETECTED, ARE YOU SURE YOU WANT TO EXIT?"
        self.ExitMenuText3 = "ALL PROGRESS WILL BE LOST!"
TextColl = TextAndInput()


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
#mySQL data
Pinfo = PlayersInformation()

#--------------------------------------------------------------------
# Screen the player will see on startup
def TitleScreen(): 
        
    global Pinfo
    global TransportAmount
      
    Pinfo = TerminalGameMYSQL.IndexData()
    if Pinfo.Language == 0:
        SetLanguage(False) # True = English, False = Dutch  
    else:
        SetLanguage(True) # True = English, False = Dutch  

    uid = Pinfo.UID
    TransportAmount = Pinfo.PlayerAmount
    #TransportAmount = int(GetPlayerAmount()) # get the amount of players trough file that changed

    FullScreenMessage(TextColl.BootScreenLockedText,1)
    TitleScreen_Selections()       
#--------------------------------------------------------------------
# checks if the usb is connected or if a dev enterd a command
def TitleScreen_Selections():   
    while True:      
        option = ""
        if DEVMODE is True:
            option = TextInput()
        if option == TextColl.DevInputText[0] or MPvalue.value == 1:
            myPlayer.GameStarted = True
            os.system('cls||clear')
            FakeLoading(TextColl.FakeLoadingText1)
            slowprint(TextColl.ACCESSGRANTEDTEXT,2)
            time.sleep(2.00)
            StartGame()
            break
        # elif option == StartMenuText[1]:
        #     HelpMenu()
        #     break
        elif option == TextColl.DevInputText[2]:
            sys.exit()
        elif option is not "":
            print(option)
            slowprint("DEV START SCREEN ENTER START")
#--------------------------------------------------------------------
#main menu
def StartGame():
    global FirstLoad
    global TransportAmount
    if FirstLoad == False:
        time.sleep(1.00)
    else:
        FirstLoad = False
        SendProgress(10)

    os.system('cls||clear')
    SlowPrintArray(TextColl.InputCommandsText, TextColl.PLEASEENTERCOMMANDTEXT)
    while True:
        CheckForMessage()
        option = TextInput()
        if TextColl.InputCommands[0] == option: #1 = CONNECT TO COMPUTER
            ConnectMenu()
            break
        elif TextColl.InputCommands[1] == option: #2 = LOGIN TO COMPUTER
            LoginMenu()
            break
        elif TextColl.InputCommands[2] == option: #3 = EDIT PRISONER TRANSPORT MANIFEST
            ChangeAmountMenu()
            break
        elif TextColl.InputCommands[3] == option: #4 = SAVE CAHNGES AND EXIT
            ExitMenu()
            break
        else:
            slowprint(TextColl.PLEASEENTERAVALIDCOMMANDTEXT)
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
#checks if the players connected the lan cable
def ConnectMenu():
    os.system('cls||clear')
    global ip
    #if DEVMODE == False:
    myPlayer.CableConnected = CheckLanConnection()

    if myPlayer.CableConnected == False:
        slowprint(TextColl.ConnectText1,1)
        StartGame()
    else:
        slowprint(TextColl.ConnectText2)
        while True:
            option = TextInput()
            if myPlayer.CableConnected == True and TerminalGameIPInput.CheckedInput(ip) == True:
                os.system('cls||clear')
                myPlayer.ConnectionOnline = True
                FakeLoading(TextColl.ConnectFakeLoadingText1)
                StartGame()
                break
            else:
                slowprint(TextColl.ConnectText3,1)
                StartGame()
                break
#--------------------------------------------------------------------
#checks if the players connected the lan cable, if so it checks for the right login code/password
def LoginMenu():
    os.system('cls||clear')
       
    if myPlayer.CableConnected == False:
        slowprint(TextColl.LoginText1,1)
        StartGame()
    elif myPlayer.ConnectionOnline == False:
        slowprint(TextColl.LoginText2,1)
        StartGame()
    elif myPlayer.ConnectionOnline == True and myPlayer.CableConnected == True:
        while True:
            slowprint(TextColl.LoginText3)
            option = TextInput()
            if LoginCode == option:
                myPlayer.LogedIn = True
                FakeLoading(TextColl.LoginFakeLoadingText1)
                StartGame()
            else:
                slowprint(TextColl.LoginText4,1)
                StartGame()

#--------------------------------------------------------------------
#prisoner menu, checks if the players enterd the right transport number
def ChangeAmountMenu():
    os.system('cls||clear')

    if myPlayer.CableConnected == False:
        slowprint(TextColl.ChangeAmountText1,1)
        StartGame()
    elif myPlayer.ConnectionOnline == False:
        slowprint(TextColl.ChangeAmountText2,1)
        StartGame()
    elif myPlayer.LogedIn == False:
        slowprint(TextColl.ChangeAmountText3,1)
        StartGame()
    else:
        slowprint(TextColl.ChangeAmountText4)
        while True:
            option = TextInput()
            if option == TransportNumber:
                FakeLoading(TextColl.ChangeAmountFakeLoadingText1)
                TransportMenu()
                break
            else:
                FakeLoading(TextColl.ChangeAmountFakeLoadingText2,1)
                StartGame()
                break

#--------------------------------------------------------------------
#transport menu, simply a selection menu for new options
def TransportMenu():
    time.sleep(1.00)
    os.system('cls||clear')
    SlowPrintArray(TextColl.TransportMenuText, TextColl.PLEASEENTERCOMMANDTEXT)

    while True:
        CheckForMessage()
        option = TextInput()
        if TextColl.InputCommands[0] == option: #1 = CANCEL TRANSPORT
            os.system('cls||clear')
            slowprint(TextColl.TransportText1,1)
            TransportMenu()
        elif TextColl.InputCommands[2] == option: #3 = DELAY TRANSPORT
            os.system('cls||clear')
            slowprint(TextColl.TransportText1,1)
            TransportMenu()
        elif TextColl.InputCommands[3] == option: #4 = RETURN TO LAST MENU
            StartGame()
            break
        elif TextColl.InputCommands[1] == option: #2 = CHANGE PRISONER AMOUNT FOR TRANSPORT
            PrisonerAmount()
            break
        else:
            slowprint(TextColl.PLEASEENTERAVALIDCOMMANDTEXT)
#--------------------------------------------------------------------
#checks if the players enterd the right amount of prisoners 
def PrisonerAmount():
    os.system('cls||clear')
    slowprint(TextColl.PrisonerText1)
    while True:
        option = int(TextInput())
        if option == TransportAmount:
            myPlayer.TransportManifestCompleted = True
            FakeLoading(TextColl.PrisonerFakeLoadingText1)
            time.sleep(1.00)
            StartGame()
        else:
            FakeLoading(TextColl.PrisonerFakeLoadingText2,1)
            TransportMenu()
#--------------------------------------------------------------------
# the games exit menu when the player wants to "exit the program"
def ExitMenu():
    os.system('cls||clear')

    if myPlayer.TransportManifestCompleted == True:
        slowprint(TextColl.ExitMenuText1)
    else:
        slowprint(TextColl.ExitMenuText2,1)
        slowprint(TextColl.ExitMenuText3,1)

    print('')
    SlowPrintArray(TextColl.ExitMenuText, TextColl.PLEASEENTERCOMMANDTEXT)

    while True:
        option = TextInput()
        if TextColl.InputCommands[0] == option: #1 = YES
            if myPlayer.TransportManifestCompleted == True:
                myPlayer.GameWon = True
                #execute opening door code or something here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                print("execute opening door code or something here")
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
        elif TextColl.InputCommands[1] == option: #2 = NO
            StartGame()
            break
#--------------------------------------------------------------------
#show the end screen with the right text
def EndScreen(type):
    if type == False: # wrong end, player can start again
        FullScreenMessage(TextColl.BootScreenUnlockedText)
        while True:
            option = TextInput()
            if TextColl.InputCommands[0] == option:
                StartGame()
                break
    elif type == True: # right end
        FullScreenMessage(TextColl.EndScreenText)
        RestartCountDown()
#--------------------------------------------------------------------
# WHEN THIS FUNCTION IS CALLED IT WONT END UNTILL THE USER PRESSES ENTER
# here we can catch text before its used.
def TextInput():
    while True:
        try:
            text = input().lower()
        except SyntaxError: #except EOFError:
            return ""
        else:
            if text is "":
                return ""
            elif text == "cable":
                myPlayer.CableConnected = True
                print("Cable active")
            elif text == "quit":
                sys.exit()
            elif text == "transportmenu":
                TransportMenu()
            else:
                return text
       # textval.value = text
       # print("put in:",text)
       # print("val is:",textval.value)
   
#--------------------------------------------------------------------
#THIS CODE IS BEING RUN AS A PROCESS! ALL DATA IS BEING RETURED IN Tvalue, SO DONT USE return       
#the code checks if a usb device is being connected or disconnected
#connected returns 1, disconnected returns 0
def UsbMonitor(Tvalue):   
        monitor = pyudev.Monitor.from_netlink(context)
        monitor.filter_by('block')
        for device in iter(monitor.poll, None):
            if 'ID_FS_TYPE' in device:
                if device.action == "add":
                    #print("True")
                    Tvalue.value = 1
                    return
                    #print(Tvalue.value)
                else:
                    #print("false")
                    Tvalue.value = 0
                    #print(Tvalue.value)  
#--------------------------------------------------------------------
def SetLanguage(IsEnglish):

    global TextColl

    if IsEnglish == True:
        TextColl = TerminalGameLanguage.ENGTextColl
    else:
        TextColl = TerminalGameLanguage.NLTextColl

#--------------------------------------------------------------------    
def CheckForMessage():
    global LastMessageTime
    Pinfo = TerminalGameMYSQL.IndexData()
    uid = Pinfo.UID
    if DEVMODE == False: 
        if Pinfo.DateAndTime > datetime.datetime.strptime(str(LastMessageTime), '%Y-%m-%d %H:%M:%S'):       
           LastMessageTime = datetime.datetime.strptime(str(Pinfo.DateAndTime), '%Y-%m-%d %H:%M:%S')
     
           if Pinfo.LastMessage is not "":
               print("")
               slowprint(Pinfo.LastMessage,3)  
#-------------------------------------------------------------------- 
def RestartCountDown():
    Pinfo = TerminalGameMYSQL.IndexData()
    uid = Pinfo.UID

    if DEVMODE == True:
        time.sleep(5)
    else:
        while True:
            Pinfo = TerminalGameMYSQL.IndexData()
            if Pinfo.UID > uid:
                #print("true pinfo = ",Pinfo.UID," old uid: ",uid)
                os.execv(sys.executable, ['python3'] + sys.argv)
            else:
                #print("false pinfo = ",Pinfo.UID," old uid: ",uid)
                time.sleep(10)
    
#-------------------------------------------------------------------- 
def SendProgress(value):
    if DEVMODE == False:
        try:
            url = "http://10.0.0.10:8080/json.htm?type=command&param=udevice&idx=26&nvalue="+str(value)+"0&svalue=;"
            urllib.request.urlopen(url)
        except urllib.request.HTTPError:
            print ("error http")
        except urllib.request.URLError as e:
	        print ("error url")      
        finally:
	        print ("This is going to be printed even if no exception occurs")

#    #payload = {'name': 'bob', 'job': 'driver'}
#    #r = request.post('https://reqres.in/api/users',json=payload)
#    #print(r.text)
#    #10.0.0.110:8080/
#-------------------------------------------------------------------- 
def CheckLanConnection(): #Checks if the btn is pressed. If this is the case it returns True
        if GPIO.input(keyBtnGpio) == False:
            return True
        else:
            return False
#-------------------------------------------------------------------- 
#start of the process so we can run the game and check for connections    
if __name__ == "__main__":
    MPvalue = Value('i',0)
    p1 = multiprocessing.Process(target=UsbMonitor, args=(MPvalue,))
    p1.deamon = True
    p1.start()  
    TitleScreen()
    #SendJsonUpdate()

    
    
