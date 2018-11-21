
fakeip = "127.0.0.1" 

def EnterIP():
    splitIP = fakeip.split('.')
    print("Please enter the first " +str(len(splitIP[0])) + " numbers of the ip adress")
    firstEntry = TextInput()
    print("Please enter the next " +str(len(splitIP[1])) + " numbers of the ip adress")
    secondEntry = TextInput()
    print("Please enter the next " +str(len(splitIP[2])) + " numbers of the ip adress")
    thirdEntry = TextInput()
    print("Please enter the last " +str(len(splitIP[3])) + " numbers of the ip adress")
    fourthEntry = TextInput()

    if(splitIP[0]+splitIP[1]+splitIP[2]+splitIP[3]) == (firstEntry+secondEntry+thirdEntry+fourthEntry):
        print("succes")
        #exicute code here
    else:
        print("nope")
        # return to menu because the player failed
    

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

EnterIP()