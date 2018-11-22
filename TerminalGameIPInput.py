import sys, termios, tty, os, time, random
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def CheckedInput(fakeip = ""):

    charCounter = 0
    button_delay = 0.001
    splitIP = fakeip.split('.')
    countLength = len(splitIP[0])
    splitsCounted = 0
    playerinput = ""
    ipCharLength = (len(splitIP[0])+len(splitIP[1])+len(splitIP[2])+len(splitIP[3]))

    while True:
        char = getch()
        playerinput = playerinput + char

        if (char == "p"):
            print("Stop!")
            exit(0)

        sys.stdout.write(char)
        charCounter +=1
        
        if (charCounter == countLength):
            sys.stdout.write('.')
            splitsCounted += 1
            if(splitsCounted <= 2):
                countLength += len(splitIP[splitsCounted])
            
        if(ipCharLength == charCounter):
            sys.stdout.write(' \n')
            sys.stdout.flush()
            if(splitIP[0]+splitIP[1]+splitIP[2]+splitIP[3]) == playerinput:
                #print("succes")
                return True
            else:
                #print("fail")
                return False

        sys.stdout.flush()
        time.sleep(button_delay)

#CheckedInput("127.0.0.1")