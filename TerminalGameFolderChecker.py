import sys, os, re

RecieverFolderName = "\RECIEVER_FOLDER"
TextToFind = "PLAYERAMOUNT"
CurrentAmountOfPlayers = 0
FileNamesRaw = [" "]
FileNamesCut = [" "]

#--------------------------------------------------------------------
def GetPlayerAmount():
    global FileNamesRaw
    del FileNamesRaw[:]

    pathname = os.path.dirname(sys.argv[0])
    #print('path =', pathname)
    #print('path =', pathname+RecieverFolderName)

    for dirpath,dirnames,filenames in os.walk(pathname+RecieverFolderName):
        global filename
        FileNamesRaw += filenames

    global FileNamesCut
    del FileNamesCut[:]

    for file in FileNamesRaw:
        FileNamesCut += file.split('.')[:-1]
        #print (FileNamesCut)

    for file in FileNamesCut:
        if TextToFind in file:
            number = re.findall('\d+', file)
            return int(number[0])
            #print("amount: " + str(CurrentAmountOfPlayers))
            break

    return 0
#--------------------------------------------------------------------
