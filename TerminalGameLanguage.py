import cmd,textwrap,sys,os,time,random,math,re


#change all values to a class so we can global everything while not fucking with memory or something




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
        self.ENGFakeLoadingText1 = ["INSTALLING KEYCRACKER.PY", "INSTALL COMPLETED"]
        self.ENGACCESSGRANTEDTEXT = "ACCESS GRANTED"
        self.ENGPLEASEENTERCOMMANDTEXT = "PLEASE ENTER A COMMAND"
        self.ENGPLEASEENTERAVALIDCOMMANDTEXT = "PLEASE ENTER A VALID COMMAND"
        self.ENGConnectText1 = "ERROR: NOT CONNECTED TO THE INTERNET"
        self.ENGConnectText2 = "PLEASE ENTER THE IP YOU WANT TO CONNECT TO"
        self.ENGConnectText3 = "ERROR: CANT CONNECT TO IP"
        self.ENGConnectFakeLoadingText1 = ["CONNECTING","CONNECTION ESTABLISHED"]
        self.ENGLoginText1 = "ERROR: NOT CONNECTED TO THE INTERNET"
        self.ENGLoginText2 = "ERROR: NOT CONNECTED TO A OTHER COMPUTER"
        self.ENGLoginText3 = "PLEASE ENTER PIN CODE"
        self.ENGLoginText4 = "ERROR: PINCODE INCORRECT, RETURNING TO MENU"
        self.ENGLoginFakeLoadingText1 = ["CONNECTING","LOGIN SUCCESFULL"]
        self.ENGChangeAmountText1 = "ERROR: NOT CONNECTED TO THE INTERNET"
        self.ENGChangeAmountText2 = "ERROR: NOT CONNECTED TO A OTHER COMPUTER"
        self.ENGChangeAmountText3 = "ERROR: NOT LOGGED IN"
        self.ENGChangeAmountText4 = "PLEASE ENTER TRANSPORT NUMBER"
        self.ENGChangeAmountFakeLoadingText1 = "SEARCHING","SEARCH COMPLETED"
        self.ENGChangeAmountFakeLoadingText2 = "SEARCHING","SEARCH FAILED"
        self.ENGTransportText1 = "ADMINISTRATOR ACCESS REQUIRED"
        self.ENGPrisonerText1 = "PLEASE ENTER THE AMOUNT OF PRISONERS THAT NEED TO BE TRANSPORTED"
        self.ENGPrisonerFakeLoadingText1 = ["PROCESSING","TASK COMPLETED PLEASE SAVE THE CHANGES AND CARRY ON WITH YOUR WORK"]
        self.ENGPrisonerFakeLoadingText2 = ["PROCESSING","ERROR: INVALID NUMBER"]
        self.ENGExitMenuText1 = "FILE CHANGES DETECTED, PLEASE EXIT TO SAVE CHANGES"
        self.ENGExitMenuText2 = "NO FILE CHANGES DETECTED, ARE YOU SURE YOU WANT TO EXIT?"
        self.ENGExitMenuText3 = "ALL PROGRESS WILL BE LOST!"
TextColl = TextAndInput()

#-------------------------------------------------------------------------------------------------------------------------------------

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
        self.NLFakeLoadingText1 = ["KEYCRACKER.PY AAN HET INSTALEREN", "INSTALATIE VOLTOOID"]
        self.NLACCESSGRANTEDTEXT = "TOEGANG VERLEEND"
        self.NLPLEASEENTERCOMMANDTEXT = "VOER EEN OPDRACHT IN"
        self.NLPLEASEENTERAVALIDCOMMANDTEXT = "VOER EEN GELDIGE OPDRACHT IN"
        self.NLConnectText1 = "ERROR: KAN NIET MET HET INTERNET VERBINDEN"
        self.NLConnectText2 = "VOER HET IP ADRES IN WAARMEE U WILT VERBINDEN"
        self.NLConnectText3 = "ERROR: KAN NIET MET IP VERBINDEN"
        self.NLConnectFakeLoadingText1 = ["AAN HET VERBINDEN","VERBINDING GESLAAGD"]
        self.NLLoginText1 = "ERROR: NIET VERBONDEN AAN HET INTERNET"
        self.NLLoginText2 = "ERROR: NIET VERBONDEN MET EEN ANDERE COMPUTER"
        self.NLLoginText3 = "VOER PINCODE IN"
        self.NLLoginText4 = "ERROR: PINCODE ONGELDIG, KEERT TERUG NAAR HET MENU"
        self.NLLoginFakeLoadingText1 = ["VERBINDEN","LOGIN GESLAAGD"]
        self.NLChangeAmountText1 = "ERROR: NIET VERBONDEN MET HET INTERNET"
        self.NLChangeAmountText2 = "ERROR: NIET VERBONDEN MET EEN ANDERE COMPUTER"
        self.NLChangeAmountText3 = "ERROR: NIET INGELOGD"
        self.NLChangeAmountText4 = "VOER TRANSPORT NUMMER IN"
        self.NLChangeAmountFakeLoadingText1 = "ZOEKEN","ZOEKEN GESLAAGD"
        self.NLChangeAmountFakeLoadingText2 = "ZOEKEN","ZOEKEN MISLUKT"
        self.NLTransportText1 = "ADMINISTRATOR TOEGANG NODIG"
        self.NLPrisonerText1 = "VOER HOEVEELHEID GEVANGENEN VOOR TRANSPORT IN A.U.B."
        self.NLPrisonerFakeLoadingText1 = ["AAN HET VERWERKEN","OPDRACHT VOLTOOID, SLA ALSTUBLIEFT UW VERANDERINGEN OP EN GA DOOR MET UW WERK"]
        self.NLPrisonerFakeLoadingText2 = ["AAN HET VERWERKEN","ERROR: FOUT NUMMER"]
        self.NLExitMenuText1 = "AANPASSINGEN GEDETECTEERD, SLUIT AF OM OP TE SLAAN"
        self.NLExitMenuText2 = "GEEN AANPASSINGEN GEDETECTEERD, WEET U ZEKER DAT U WILT AFSLUITEN?"
        self.NLExitMenuText3 = "ALLE VERANDERINGEN WORDEN NIET OPGESLAGEN!"
TextColl = TextAndInput()

