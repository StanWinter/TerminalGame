import cmd,textwrap,sys,os,time,random,math,re

# english text

# inputs made by player/dev
ENGDevInputText = ["start","help","quit"]
ENGInputCommands = ["1","2","3","4"]

# screen text for special screens
ENGBootScreenLockedText = ["SYSTEM LOCKED","PLEASE INSERT USB KEY"]
ENGBootScreenUnlockedText = ["SYSTEM UNLOCKED","PLEASE ENTER 1 TO START"]
ENGEndScreenText = ["CHANGES SAVED","PLEASE TRANSPORT THE PRISONERS"]

# options text shown to the player
ENGInputCommandsText = ["1 = CONNECT TO COMPUTER","2 = LOGIN TO COMPUTER",
                     "3 = EDIT PRISONER TRANSPORT MANIFEST","4 = SAVE CHANGES AND EXIT"]
ENGTransportMenuText = ["1 = CANCEL TRANSPORT","2 = CHANGE PRISONER AMOUNT FOR TRANSPORT",
                     "3 = DELAY TRANSPORT","4 = RETURN TO LAST MENU"]
ENGExitMenuText = ["1 = YES", "2 = NO"]

# misc text
class TextAndInput:
    def __init__(self):
        self.DevInputText = ["start","help","quit"]
        self.InputCommands = ["1","2","3","4"]
        self.BootScreenLockedText = ["SYSTEM LOCKED","PLEASE INSERT USB KEY"]
        self.BootScreenUnlockedText = ["SYSTEM UNLOCKED","PLEASE ENTER 1 TO START"]
        self.EndScreenText = ["CHANGES SAVED","PLEASE TRANSPORT THE PRISONERS"]

        self.InputCommandsText = ["1 = CONNECT TO COMPUTER","2 = LOGIN TO COMPUTER",
                          "3 = EDIT PRISONER TRANSPORT MANIFEST","4 = SAVE CHANGES AND EXIT"]
        self.TransportMenuText = ["1 = CANCEL TRANSPORT","2 = CHANGE PRISONER AMOUNT FOR TRANSPORT",
                          "3 = DELAY TRANSPORT","4 = RETURN TO LAST MENU"]
        self.ExitMenuText = ["1 = YES", "2 = NO"]
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
        self.ChangeAmountFakeLoadingText3 = "TRANSPORTNUMMER 114","BESTUURDER: PETE LAREN","BEWAKER: BILL MACCOY" #MOETEN JULLIE VERTALEN!
        self.ChangeAmountFakeLoadingText4 = "REISTIJD: 15 MINUTEN","BESTEMMING: TGE PRISON"      #MOETEN JULLIE VERTALEN!
        self.TransportText1 = "ADMINISTRATOR ACCESS REQUIRED"
        self.PrisonerText1 = "PLEASE ENTER THE AMOUNT OF PRISONERS THAT NEED TO BE TRANSPORTED"
        self.PrisonerFakeLoadingText1 = ["PROCESSING","TASK COMPLETED PLEASE SAVE THE CHANGES AND CARRY ON WITH YOUR WORK"]
        self.PrisonerFakeLoadingText2 = ["PROCESSING","ERROR: INVALID NUMBER"]
        self.ExitMenuText1 = "FILE CHANGES DETECTED, PLEASE EXIT TO SAVE CHANGES"
        self.ExitMenuText2 = "NO FILE CHANGES DETECTED, ARE YOU SURE YOU WANT TO EXIT?"
        self.ExitMenuText3 = "ALL PROGRESS WILL BE LOST!"
ENGTextColl = TextAndInput()

#-------------------------------------------------------------------------------------------------------------------------------------

# Dutch Text

# inputs made by player/dev
NLDevInputText = ["start","help","quit"]
NLInputCommands = ["1","2","3","4"]

# screen text for special screens
NLBootScreenLockedText = ["SYSTEEM GESLOTEN","VOER USB-SLEUTEL IN A.U.B."]
NLBootScreenUnlockedText = ["SYSTEEM OPEN","VOER 1 IN OM TE STARTEN"]
NLEndScreenText = ["AANPASSINGEN OPGESLAGEN","VERVOER NU DE GEVANGENEN"]

# options text shown to the player
NLInputCommandsText = ["1 = VERBIND MET EEN COMPUTER","2 = LOGIN OP EEN COMPUTER",
                     "3 = BEWERK LIJST GEVANGENENVERVOER","4 = SLA AANPASSINGEN OP EN GA TERUG"]
NLTransportMenuText = ["1 = ANNULEER GEVANGENENVERVOER","2 = VERANDER HOEVEELHEID GEVANGENEN VOOR TRANSPORT",
                     "3 = STEL TRANSPORT UIT","4 = GA TERUG NA HET LAATSTE MENU"]
NLExitMenuText = ["1 = JA", "2 = NEE"]

# misc text
class TextAndInput:
    def __init__(self):
        self.DevInputText = ["start","help","quit"]
        self.InputCommands = ["1","2","3","4"]
        self.BootScreenLockedText = ["SYSTEEM GESLOTEN","VOER USB-SLEUTEL IN A.U.B."]
        self.BootScreenUnlockedText = ["SYSTEEM OPEN","VOER 1 IN OM TE STARTEN"]
        self.EndScreenText = ["AANPASSINGEN OPGESLAGEN","VERVOER NU DE GEVANGENEN"]
        self.InputCommandsText = ["1 = VERBIND MET EEN COMPUTER","2 = LOGIN OP EEN COMPUTER",
                           "3 = BEWERK LIJST GEVANGENENVERVOER","4 = SLA AANPASSINGEN OP EN GA TERUG"]
        self.TransportMenuText = ["1 = ANNULEER GEVANGENENVERVOER","2 = VERANDER HOEVEELHEID GEVANGENEN VOOR TRANSPORT",
                          "3 = STEL TRANSPORT UIT","4 = GA TERUG NA HET LAATSTE MENU"]
        self.ExitMenuText = ["1 = JA", "2 = NEE"]
        self.FakeLoadingText1 = ["KEYCRACKER.PY AAN HET INSTALLEREN", "INSTALLATIE VOLTOOID"]
        self.ACCESSGRANTEDTEXT = "TOEGANG VERLEEND"
        self.PLEASEENTERCOMMANDTEXT = "VOER EEN OPDRACHT IN"
        self.PLEASEENTERAVALIDCOMMANDTEXT = "VOER EEN GELDIGE OPDRACHT IN"
        self.ConnectText1 = "ERROR: KAN NIET MET HET INTERNET VERBINDEN"
        self.ConnectText2 = "VOER HET IP ADRES IN WAARMEE U WILT VERBINDEN"
        self.ConnectText3 = "ERROR: KAN NIET MET IP VERBINDEN"
        self.ConnectFakeLoadingText1 = ["AAN HET VERBINDEN","VERBINDING GESLAAGD"]
        self.LoginText1 = "ERROR: NIET VERBONDEN MET HET INTERNET"
        self.LoginText2 = "ERROR: NIET VERBONDEN MET EEN ANDERE COMPUTER"
        self.LoginText3 = "VOER PINCODE IN"
        self.LoginText4 = "ERROR: PINCODE ONGELDIG, KEERT TERUG NAAR HET MENU"
        self.LoginFakeLoadingText1 = ["VERBINDEN","LOGIN GESLAAGD"]
        self.ChangeAmountText1 = "ERROR: NIET VERBONDEN MET HET INTERNET"
        self.ChangeAmountText2 = "ERROR: NIET VERBONDEN MET EEN ANDERE COMPUTER"
        self.ChangeAmountText3 = "ERROR: NIET INGELOGD"
        self.ChangeAmountText4 = "VOER TRANSPORT NUMMER IN"
        self.ChangeAmountFakeLoadingText1 = "ZOEKEN","ZOEKEN GESLAAGD"
        self.ChangeAmountFakeLoadingText2 = "ZOEKEN","ZOEKEN MISLUKT"
        self.ChangeAmountFakeLoadingText3 = "TRANSPORTNUMMER 114","BESTUURDER: PETE LAREN","BEWAKER: BILL MACCOY"
        self.ChangeAmountFakeLoadingText4 = "REISTIJD: 15 MINUTEN","BESTEMMING: TGE PRISON"       
        self.TransportText1 = "ADMINISTRATOR TOEGANG NODIG"
        self.PrisonerText1 = "VOER HOEVEELHEID GEVANGENEN VOOR TRANSPORT IN A.U.B."
        self.PrisonerFakeLoadingText1 = ["AAN HET VERWERKEN","OPDRACHT VOLTOOID, SLA ALSTUBLIEFT UW VERANDERINGEN OP EN GA DOOR MET UW WERK"]
        self.PrisonerFakeLoadingText2 = ["AAN HET VERWERKEN","ERROR: FOUT NUMMER"]
        self.ExitMenuText1 = "AANPASSINGEN GEDETECTEERD, SLUIT AF OM OP TE SLAAN"
        self.ExitMenuText2 = "GEEN AANPASSINGEN GEDETECTEERD, WEET U ZEKER DAT U WILT AFSLUITEN?"
        self.ExitMenuText3 = "ALLE VERANDERINGEN WORDEN NIET OPGESLAGEN!"
NLTextColl = TextAndInput()

