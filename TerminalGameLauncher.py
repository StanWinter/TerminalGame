import cmd,textwrap,sys,os,time,random,math,re,pyudev,ctypes,TerminalGameLanguage,TerminalGameMYSQL,TerminalGameUsbDetector, LanDetector
import threading,random,queue,subprocess
from TerminalGameTools import slowprint, FakeLoading, SlowPrintArray, FullScreenMessage
from TerminalGameFolderChecker import GetPlayerAmount
from TerminalGameMYSQL import PlayersInformation
import multiprocessing 
from multiprocessing import Process, Value

context = pyudev.Context()
columns, rows = os.get_terminal_size(1)
FirstLoad = True
# codes the player needs to enter
ip = "127.0.0.1"
LoginCode = "12345"
TransportNumber = "101"
TransportAmount = 0

# inputs made by player/dev
DevInputText = ["start","help","quit"]
InputCommands = ["1","2","3","4"]

# screen text for special screens
BootScreenLockedText = ["SYSTEM LOCKED","PLEASE INSERT USB KEY"]
BootScreenUnlockedText = ["SYSTEM UNLOCKED","PLEASE ENTER 1 TO START"]
EndScreenText = ["CHANGES SAVED","PLEASE TRANSPORT THE PRISONERS"]

# options text shown to the player
InputCommandsText = ["1 = CONNECT TO COMPUTER","2 = LOGIN TO COMPUTER",
                        "3 = EDIT PRISONER TRANSPORT MANIFEST","4 = SAVE CHANGES AND EXIT"]
TransportMenuText = ["1 = CANCEL TRANSPORT","2 = CHANGE PRISONER AMOUNT FOR TRANSPORT",
                        "3 = DELAY TRANSPORT","4 = RETURN TO LAST MENU"]
ExitMenuText = ["1 = YES", "2 = NO"]

# all other text
class TextAndInput:
    def __init__(self):
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

# Screen the player will see on startup
def TitleScreen():   
    global Pinfo
    global TransportAmount
    
   
    Pinfo = TerminalGameMYSQL.IndexData()
    if Pinfo.Language == 0:
        SetLanguage(False) # True = English, False = Dutch  
    else:
        SetLanguage(True) # True = English, False = Dutch  

    TransportAmount = Pinfo.PlayerAmount
    #TransportAmount = int(GetPlayerAmount()) # get the amount of players trough file that changed

    FullScreenMessage(BootScreenLockedText)
    TitleScreen_Selections()

#--------------------------------------------------------------------
# selection menu (for dev purposes)
def TitleScreen_Selections():
    while True:
        option = TextInput()
        if option == DevInputText[0] or MPvalue.value == 1:
            myPlayer.GameStarted = True
            os.system('cls||clear')
            FakeLoading(TextColl.FakeLoadingText1)
            slowprint(TextColl.ACCESSGRANTEDTEXT)
            time.sleep(2.00)
            StartGame()
            break
        # elif option == StartMenuText[1]:
        #     HelpMenu()
        #     break
        elif option == DevInputText[2]:
            sys.exit()
        elif option is not "":
            print(option)
            slowprint("DEV START SCREEN ENTER START")
#--------------------------------------------------------------------

def StartGame():
    global FirstLoad
    global TransportAmount
    if FirstLoad == False:
        time.sleep(1.00)
    else:
        FirstLoad = False

    os.system('cls||clear')
    SlowPrintArray(InputCommandsText, TextColl.PLEASEENTERCOMMANDTEXT)
    while True:
        option = TextInput()
        if InputCommands[0] == option: #1 = CONNECT TO COMPUTER
            ConnectMenu()
            break
        elif InputCommands[1] == option: #2 = LOGIN TO COMPUTER
            LoginMenu()
            break
        elif InputCommands[2] == option: #3 = EDIT PRISONER TRANSPORT MANIFEST
            ChangeAmountMenu()
            break
        elif InputCommands[3] == option: #4 = SAVE CAHNGES AND EXIT
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
def ConnectMenu():
    os.system('cls||clear')

    if myPlayer.CableConnected == False:
        slowprint(TextColl.ConnectText1)
        StartGame()
    else:
        slowprint(TextColl.ConnectText2)
        while True:
            option = TextInput()
            if myPlayer.CableConnected == True and ip in option:
                os.system('cls||clear')
                myPlayer.ConnectionOnline = True
                FakeLoading(TextColl.ConnectFakeLoadingText1)
                StartGame()
                break
            else:
                slowprint(TextColl.ConnectText3)
                StartGame()
                break
#--------------------------------------------------------------------
def LoginMenu():
    os.system('cls||clear')

    #if LanDetector.getKeyStatus is True:   # THIS IS THE LAN CABLE CONNECTION CHECK, NOT TESTED 
    #    myPlayer.CableConnected = True
        
    if myPlayer.CableConnected == False:
        slowprint(TextColl.LoginText1)
        StartGame()
    elif myPlayer.ConnectionOnline == False:
        slowprint(TextColl.LoginText2)
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
                slowprint(TextColl.LoginText4)
                StartGame()

#--------------------------------------------------------------------
def ChangeAmountMenu():
    os.system('cls||clear')

    if myPlayer.CableConnected == False:
        slowprint(TextColl.ChangeAmountText1)
        StartGame()
    elif myPlayer.ConnectionOnline == False:
        slowprint(TextColl.ChangeAmountText2)
        StartGame()
    elif myPlayer.LogedIn == False:
        slowprint(TextColl.ChangeAmountText3)
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
                FakeLoading(TextColl.ChangeAmountFakeLoadingText2)
                StartGame()
                break

#--------------------------------------------------------------------
def TransportMenu():
    time.sleep(1.00)
    os.system('cls||clear')
    SlowPrintArray(TransportMenuText, TextColl.PLEASEENTERCOMMANDTEXT)

    while True:
        option = TextInput()
        if InputCommands[0] == option: #1 = CANCEL TRANSPORT
            slowprint(TextColl.TransportText1)
        elif InputCommands[2] == option: #3 = DELAY TRANSPORT
            slowprint(TextColl.TransportText1)
        elif InputCommands[3] == option: #4 = RETURN TO LAST MENU
            StartGame()
            break
        elif InputCommands[1] == option: #2 = CHANGE PRISONER AMOUNT FOR TRANSPORT
            PrisonerAmount()
            break
        else:
            slowprint(TextColl.PLEASEENTERAVALIDCOMMANDTEXT)
#--------------------------------------------------------------------
def PrisonerAmount():
    slowprint(TextColl.PrisonerText1)
    while True:
        option = int(TextInput())
        if option == TransportAmount:
            myPlayer.TransportManifestCompleted = True
            FakeLoading(TextColl.PrisonerFakeLoadingText1)
            time.sleep(1.00)
            StartGame()
        else:
            FakeLoading(TextColl.PrisonerFakeLoadingText2)
            TransportMenu()
#--------------------------------------------------------------------
def ExitMenu():
    os.system('cls||clear')

    if myPlayer.TransportManifestCompleted == True:
        slowprint(TextColl.ExitMenuText1)
    else:
        slowprint(TextColl.ExitMenuText2)
        slowprint(TextColl.ExitMenuText3)

    print('')
    SlowPrintArray(ExitMenuText, TextColl.PLEASEENTERCOMMANDTEXT)

    while True:
        option = TextInput()
        if InputCommands[0] == option: #1 = YES
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
        elif InputCommands[1] == option: #2 = NO
            StartGame()
            break
#--------------------------------------------------------------------
def EndScreen(type):

    if type == False: # wrong end, player can start again
        FullScreenMessage(BootScreenUnlockedText)
        while True:
            option = TextInput()
            if InputCommands[0] == option:
                StartGame()
                break
    elif type == True: # right end
        FullScreenMessage(EndScreenText)
#--------------------------------------------------------------------

# here we can catch text before its used
def TextInput():
    while True:
        try:
            text = input().lower()
            print(text)
        except SyntaxError: #except EOFError:
            print("fail")
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
def SetLanguage(IsEnglish):

    #change all values to a class so we can global everything while not fucking with memory or something


    global DevInputText
    global InputCommands
    global BootScreenLockedText
    global BootScreenUnlockedText
    global EndScreenText
    global InputCommandsText
    global TransportMenuText
    global ExitMenuText
    global TextColl

    if IsEnglish == True:
        DevInputText = TerminalGameLanguage.ENGDevInputText
        InputCommands = TerminalGameLanguage.ENGInputCommands
        BootScreenLockedText = TerminalGameLanguage.ENGBootScreenLockedText
        BootScreenUnlockedText =TerminalGameLanguage.ENGBootScreenUnlockedText
        EndScreenText = TerminalGameLanguage.ENGEndScreenText
        InputCommandsText = TerminalGameLanguage.ENGInputCommandsText       
        TransportMenuText = TerminalGameLanguage.ENGTransportMenuText                 
        ExitMenuText = TerminalGameLanguage.ENGExitMenuText

        TextColl = TerminalGameLanguage.ENGTextColl
    else:
        DevInputText = TerminalGameLanguage.NLDevInputText
        InputCommands = TerminalGameLanguage.NLInputCommands
        BootScreenLockedText = TerminalGameLanguage.NLBootScreenLockedText
        BootScreenUnlockedText =TerminalGameLanguage.NLBootScreenUnlockedText
        EndScreenText = TerminalGameLanguage.NLEndScreenText
        InputCommandsText = TerminalGameLanguage.NLInputCommandsText      
        TransportMenuText = TerminalGameLanguage.NLTransportMenuText              
        ExitMenuText = TerminalGameLanguage.NLExitMenuText

        TextColl = TerminalGameLanguage.NLTextColl

#--------------------------------------------------------------------
def UsbMonitor(Tvalue):   
        monitor = pyudev.Monitor.from_netlink(context)
        monitor.filter_by('block')
        for device in iter(monitor.poll, None):
            if 'ID_FS_TYPE' in device:
                if device.action == "add":
                    #print("True")
                    Tvalue.value = 1
                    #print(Tvalue.value)
                else:
                    #print("false")
                    Tvalue.value = 0
                    #print(Tvalue.value)         

#start of the process so we can run the game and check for connections    
if __name__ == "__main__":
    manager = multiprocessing.Manager()
    MPstring = manager.Value(ctypes.c_char_p, "")
    MPvalue = Value('i',0)
    p1 = multiprocessing.Process(target=UsbMonitor, args=(MPvalue,))
    p1.start()
    TitleScreen()


    
    
