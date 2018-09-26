import os
import RPi.GPIO as GPIO
from omxplayer.player import OMXPlayer
from time import sleep
 
GPIO.setmode(GPIO.BCM) #referring to the pins by the "Broadcom SOC channel" number
GPIO.setwarnings(False) #disable GPIO warnings
 
ledRedGpio = 22
ledOrangeGpio = 23
btnGpio = 17
keyBtnGpio = 18
 
GPIO.setup(btnGpio, GPIO.IN, pull_up_down=GPIO.PUD_UP) #btn
GPIO.setup(keyBtnGpio, GPIO.IN, pull_up_down=GPIO.PUD_UP) #key
GPIO.setup(ledRedGpio, GPIO.OUT) #Red led, for standby
GPIO.setup(ledOrangeGpio, GPIO.OUT) #Orange led, for key activation
 
movie1 ='/home/pi/Downloads/loopescaperoom.mp4'
movie2 ='/home/pi/Downloads/hintescaperoom.mp4'
 
secondFragmentTimer = 139 #PLEASE ENTER DURATION OF SECOND VIDEO!
isrunning =False
 
def getButtonPress(): #Checks if the btn is pressed. If this is the case it returns True
    while 1:
        if GPIO.input(keyBtnGpio) == False:
            return True
            break
        else:
            return False
            break
 
def getKeyStatus(): #Checks if the key is active. If this is the case it returns True and turns on the Orange led
    while 1:
        if GPIO.input(btnGpio) == False:
            GPIO.output(ledOrangeGpio, GPIO.HIGH)
            return True
            break
        else:
            GPIO.output(ledOrangeGpio, GPIO.LOW)
            return False
            break
 
 
def killProces(): #killing the Omxplayer RIP
    print('Killing omxplayer instance')
    os.system('sudo pkill omxplayer')
 
def startingSecondInstance(): #Starting new Omxplayer instance with second movie
    print('Starting movie 2 with new instance')
    player = OMXPlayer(movie2, args=['--win', '0 0 720 564'])
    sleep(secondFragmentTimer)
 
def startingMainInstance(): #Starting new Omxplayer instance with first movie in a loop
    print('Staring new instance of Omxplayer')
    player = OMXPlayer(movie1, args=['-b', '--loop'])
 
def main(isrunning): #activate red led kill all previous processes and starting movie. Always checks if key and btn is active/pressed, if this is the case it runs the second movie
    GPIO.output(ledRedGpio, GPIO.HIGH)
    killProces()
    try:
        startingMainInstance()
        while True:
            if getKeyStatus() == True:
                if getButtonPress() == True:
                    if isrunning == False:
                        isrunning = True
                        killProces()
                        startingSecondInstance()
                        killProces()
                        startingMainInstance()
                        isrunning = False
    except Exception:
        print('Closing Player')
        killProces()
        GPIO.output(ledRedGpio, GPIO.LOW)
        GPIO.output(ledOrangeGpio, GPIO.LOW)
        GPIO.cleanup()
 
if __name__ == "__main__": #Starting main function
    isrunning = False
    main(isrunning)