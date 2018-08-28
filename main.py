#created by MettaliKk

print("Loading modules...")
gameVersion = "0.1.1 - UNFINISHED"
import os, time, sys
from colorama import init
from termcolor import cprint, colored
import random
init()
print("Loading functions...")
time.sleep(0.3)
#Programming utils
def cmd(x):
    os.system(x)
def cls():
    cmd("cls")
def sleep(x):
    time.sleep(x)
def pause():
    cmd("pause")
#END
def aboutMenu():
    cls()
    cprint("===Smartphone Tycoon===", "grey", "on_white")
    cprint("Created by", colored("Erwan Egasse", "cyan"), "AKA 'MettaliKk'")
def mainMenu():
    cls()
    print("1/ Start (new Game)")
    print("2/ About")
    user = input(">")
    if user == "1":
        setupGame()
        mainGameMenu()
    elif user == "2":
        aboutMenu()
        pause()
        mainMenu()

print("Loading 'SetupGame'...")
sleep(0.2)
def setupGame():
    global SOCIETYNAME
    global EMPLOYEECOUNT
    global SOCIETYFUNDS
    global SOCIETYFUNDS_STR

    cls()

    cprint("Name your society :", "cyan")

    SOCIETYNAME = input(">")
    SOCIETYFUNDS = 50000000
    SOCIETYFUNDS_STR = str(SOCIETYFUNDS)
    EMPLOYEECOUNT = 1

    global isSmartphoneSelling
    global isMarketingActive
    global MARKETINGLEVEL

    isSmartphoneSelling = False
    isMarketingActive = False
    MARKETINGLEVEL = 0
    #Définition des gammes (Series)

    global intINTELSERIES
    global intMEDIATEKSERIES
    global intNVIDIASERIES
    global intQUALCOMMSERIES

    intINTELSERIES = 0
    intMEDIATEKSERIES = 0
    intNVIDIASERIES = 0
    intQUALCOMMSERIES = 0

    #Création des gammes de base [newSeries]
    newSeries("ALL")
    cls()

def updateTitle():
    global SOCIETYNAME
    global SOCIETYFUNDS
    cmd("title Smartphone Tycoon ["+gameVersion+"]- "+SOCIETYNAME+" - "+str(SOCIETYFUNDS)+"$")

def mainGameMenu():
    updateTitle()
    cls()
    global isMarketingActive
    global MARKETINGLEVEL
    global isSmartphoneSelling
    global currentSmartphoneName
    if isMarketingActive == True:
        print("**Marketing level: "+colored(str(MARKETINGLEVEL)))
    else:
        pass
    cprint("Your Money: "+str(SOCIETYFUNDS), "cyan")
    print("Number of employees: "+colored(EMPLOYEECOUNT, "cyan"))
    print("-"*16)
    print("1/ Create new smartphone")
    print("2/ Marketing")
    print("3/ Employees")
    print("4/ Smartphones")
    print("5/ [Pass time]"+("\n"*2))
    USERCHOICE = input(">")
    if USERCHOICE == "1":
        if isSmartphoneSelling == True:
            cprint("Wait until the sales of ["+currentSmartphoneName+"]!", "yellow")
            pause()
            mainGameMenu()
        else:
            smartphoneMaker()
    elif USERCHOICE == "2":
        marketingMenu()
    elif USERCHOICE == "3":
        employeesMenu()
    elif USERCHOICE == "4":
        smartphoneList()
    elif USERCHOICE == "5":
        if isSmartphoneSelling == False:
            cprint("You need to have a smartphone selling!", "yellow")
            pause()
            mainGameMenu()
        else:
            passGameTime()
    else:
        cprint("Please select a valid number!", "yellow")
        pause()
        cls()
        mainGameMenu()

print("Loading 'newSeries(BRANDNAME)'...")
sleep(0.4)
def newSeries(BRANDNAME):

    global intNVIDIASERIES
    global intINTELSERIES
    global intMEDIATEKSERIES
    global intQUALCOMMSERIES

    global NVIDIASERIES
    global INTELSERIES
    global MEDIATEKSERIES
    global QUALCOMMSERIES

    if BRANDNAME == "NVIDIA":
        intNVIDIASERIES = intNVIDIASERIES+1
        NVIDIASERIES = "Series T"+str(intNVIDIASERIES)
    elif BRANDNAME == "INTEL":
        intINTELSERIES = intINTELSERIES+1
        INTELSERIES = "Series x"+str(intINTELSERIES) 
    elif BRANDNAME == "MEDIATEK":
        intMEDIATEKSERIES = intMEDIATEKSERIES+100
        MEDIATEKSERIES = "Series M"+str(intMEDIATEKSERIES)
    elif BRANDNAME == "QUALCOMM":
        intQUALCOMMSERIES = intQUALCOMMSERIES+10
        QUALCOMMSERIES = "Series Q"+str(intQUALCOMMSERIES)
    elif BRANDNAME == "ALL": #'ALL' ne devrait être utilisé que pour la fontion setupGame()
        #Nvidia: +1
        intNVIDIASERIES = intNVIDIASERIES+1
        NVIDIASERIES = "Series T"+str(intNVIDIASERIES)
        #Intel: +1
        intINTELSERIES = intINTELSERIES+1
        INTELSERIES = "Series x"+str(intINTELSERIES) 
        #Mediatek: +100
        intMEDIATEKSERIES = intMEDIATEKSERIES+100
        MEDIATEKSERIES = "Series M"+str(intMEDIATEKSERIES)
        #Qualcomm: +10
        intQUALCOMMSERIES = intQUALCOMMSERIES+10
        QUALCOMMSERIES = "Series Q"+str(intQUALCOMMSERIES)
    else:
        cprint("Error in funtion 'newSeries'!", "red")
        cprint("..Reason: Unknown brand '"+BRANDNAME+"'", "red")
def percentage(percent, whole):
  return (percent * whole) / 100.0

print("Loading 'smartphoneMaker'...")
sleep(1.2)
def smartphoneMaker():
    global SOCIETYFUNDS
    cls()
    cprint("Creating a new smartphone costs!", "yellow")
    cprint("Any money spended in the editor cannot be refunded!", "yellow")
    print("")
    print("Name your new smartphone :", colored("(type 'exit' to return to the main game menu)", "cyan"))
    global currentSmartphoneName
    currentSmartphoneName = input(">")
    if currentSmartphoneName == "exit":
        mainGameMenu()
    else:
        pass
    cls()
    cprint("===Screen dimentions===", "grey", "on_white")
    smartphoneScreenHeigh = input("Screen height [0-8] >")
    smartphoneScreenWidth = input("Screen width [0-8] >")
    smartphoneScreenRatio = input("Screen ratio [0-10] >")
    #Price Setting
    global actualSmartphoneScreenHeigh
    global actualSmartphoneScreenWidth
    global actualSmartphoneScreenRatio
    #Price described in dollars
    #SCREEN HEIGH
    if smartphoneScreenHeigh == "0":
        actualSmartphoneScreenHeigh = 25
    elif smartphoneScreenHeigh == "1":
        actualSmartphoneScreenHeigh = 60
    elif smartphoneScreenHeigh == "2":
        actualSmartphoneScreenHeigh = 70
    elif smartphoneScreenHeigh == "3":
        actualSmartphoneScreenHeigh = 80
    elif smartphoneScreenHeigh == "4":
        actualSmartphoneScreenHeigh = 90
    elif smartphoneScreenHeigh == "5":
        actualSmartphoneScreenHeigh = 100
    elif smartphoneScreenHeigh == "6":
        actualSmartphoneScreenHeigh = 110
    elif smartphoneScreenHeigh == "7":
        actualSmartphoneScreenHeigh = 120
    elif smartphoneScreenHeigh == "8":
        actualSmartphoneScreenHeigh = 130
    else:
        cprint("Type numbers as described", "yellow")
        pause()
        smartphoneMaker()
    #SCREEN WIDTH
    if smartphoneScreenWidth == "0":
        actualSmartphoneScreenWidth = 25
    elif smartphoneScreenWidth == "1":
        actualSmartphoneScreenWidth = 60
    elif smartphoneScreenWidth == "2":
        actualSmartphoneScreenWidth = 70
    elif smartphoneScreenWidth == "3":
        actualSmartphoneScreenWidth = 80
    elif smartphoneScreenWidth == "4":
        actualSmartphoneScreenWidth = 90
    elif smartphoneScreenWidth == "5":
        actualSmartphoneScreenWidth = 100
    elif smartphoneScreenWidth == "6":
        actualSmartphoneScreenWidth = 110
    elif smartphoneScreenWidth == "7":
        actualSmartphoneScreenWidth = 120
    elif smartphoneScreenWidth == "8":
        actualSmartphoneScreenWidth = 130
    else:
        cprint("Type numbers as described", "yellow")
        pause()
        smartphoneMaker()
    #SCREEN RATIO
    if smartphoneScreenRatio == "0":
        actualSmartphoneScreenRatio = 45
    elif smartphoneScreenRatio == "1":
        actualSmartphoneScreenRatio = 90
    elif smartphoneScreenRatio == "2":
        actualSmartphoneScreenRatio = 110
    elif smartphoneScreenRatio == "3":
        actualSmartphoneScreenRatio = 130
    elif smartphoneScreenRatio == "4":
        actualSmartphoneScreenRatio = 150
    elif smartphoneScreenRatio == "5":
        actualSmartphoneScreenRatio = 170
    elif smartphoneScreenRatio == "6":
        actualSmartphoneScreenRatio = 190
    elif smartphoneScreenRatio == "7":
        actualSmartphoneScreenRatio = 210
    elif smartphoneScreenRatio == "8":
        actualSmartphoneScreenRatio = 230
    elif smartphoneScreenRatio == "9":
        actualSmartphoneScreenRatio = 250
    elif smartphoneScreenRatio == "10":
        actualSmartphoneScreenRatio = 270
    else:
        cprint("Type numbers as described", "yellow")
        pause()
        smartphoneMaker()

    global SMARTPHONEPRICE
    SMARTPHONEPRICE = actualSmartphoneScreenHeigh + actualSmartphoneScreenWidth + actualSmartphoneScreenRatio
    print("Smarphone price:", colored(str(SMARTPHONEPRICE), "cyan"))
    print("\nAre you sur about the price? [Y/n]")
    user = input(">")
    if user == "Y":
        pass
    else:
        smartphoneMaker()

    #Le joueur a dépensé de l'argent en R/D
    SOCIETYFUNDS -= 100000 #-100,000$
    
    cls()
    # SOC BRANDS
    global NVIDIASERIES
    global INTELSERIES
    global MEDIATEKSERIES
    global QUALCOMMSERIES

    while True:
        cls()
        cprint("===Smartphone SOC===", "cyan")
        print("1/ Nvidia "+NVIDIASERIES)
        print("2/ Intel "+INTELSERIES)
        print("3/ Mediatek "+MEDIATEKSERIES)
        print("4/ Qualcomm "+QUALCOMMSERIES)
        print("\n5/Exit")
        print("="*5)
        BRANDCHOSE = input(">")
        global BRAND #On utilise une var globale pour la garder hors de 'while'
        if BRANDCHOSE == "1":
            BRAND = "NVIDIA"
            break
        elif BRANDCHOSE == "2":
            BRAND = "INTEL"
            break
        elif BRANDCHOSE == "3":
            BRAND = "MEDIATEK"
            break
        elif BRANDCHOSE == "4":
            BRAND = "QUALCOMM"
            break
        elif BRANDCHOSE == "5":
            cprint("Are you sure about that?", "yellow")
            cprint("If you exit now, you will lose money!", "yellow")
            print("Are you sure ? [Y/n]")
            user = input(">")
            if user == "Y": #Le joueur a choisi de quitter l'éditeur,
                SOCIETYFUNDS -= 150000 #-150,000$
                cls()
                mainGameMenu()
            else:
                pass #Le joueur a choisi de rester dans l'éditeur
        else:
            print("Please enter a valid number!")
            cls()
    #On sort de la boucle, Définition des prix:
    global SMARTPHONEMARK
    SMARTPHONEMARK = 10
    if BRAND == "NVIDIA":
        SOCPRICE = 145
    elif BRAND == "INTEL":
        SOCPRICE = 200
    elif BRAND == "MEDIATEK":
        SOCPRICE = 50
    elif BRAND == "QUALCOMM":
        SOCPRICE = 85
    else:
        cprint("Error in funtion 'smartphoneMaker'!", "red")
        cprint("LOCATION: SOCPRICE_SETTING", "yellow")
        cprint("..reason: Incorrect brand name, error from the programmer, not the user", "red")
    SMARTPHONEPRICE = SMARTPHONEPRICE + SOCPRICE
    #On avance, enfin!
    #Définition du prix par l'utilisateur!
    while True:
        cls()
        cprint("===Price setting===", "cyan")
        FINALPRICE = int(percentage(15, SMARTPHONEPRICE) + SMARTPHONEPRICE)
        MAXPRICE = int(percentage(150, SMARTPHONEPRICE) + SMARTPHONEPRICE)
        print("Minimum price: "+str(FINALPRICE))
        print("Maximum price: "+str(MAXPRICE))
        global USERPRICE
        USERPRICE = input(">")
        try:
            USERPRICE = int(USERPRICE)
        except:
            continue
        if USERPRICE > MAXPRICE:
            cprint("Your price is too high!", "yellow")
            pause()
        elif USERPRICE < FINALPRICE:
            cprint("Your price is too low!", "yellow")
            pause()
        elif USERPRICE > percentage(25, FINALPRICE) + FINALPRICE:
            SMARTPHONEMARK = SMARTPHONEMARK - 3
            break
        elif USERPRICE > percentage(15, FINALPRICE) + FINALPRICE:
            SMARTPHONEMARK = SMARTPHONEMARK - 1
            break
        elif USERPRICE > percentage(35, SMARTPHONEPRICE) + SMARTPHONEPRICE:
            SMARTPHONEMARK = SMARTPHONEMARK - 5
            break
        else:
            break
    cls()
    #Définition des stocks!
    while True:
        cls()
        cprint("===Stocks===", "cyan")
        print("1/ 15% of your money ("+str(percentage(15, SOCIETYFUNDS))+"$), ["+str(int(percentage(15, SOCIETYFUNDS)/USERPRICE))+"] copies")
        print("2/ 33% of your money ("+str(percentage(33, SOCIETYFUNDS))+"$), ["+str(int(percentage(33, SOCIETYFUNDS)/USERPRICE))+"] copies")
        print("3/ 66% of your money ("+str(percentage(66, SOCIETYFUNDS))+"$), ["+str(int(percentage(66, SOCIETYFUNDS)/USERPRICE))+"] copies")
        print("====================")
        user = input(">")
        global copiesToSell
        if user == "1":
            SOCIETYFUNDS = SOCIETYFUNDS-percentage(15, SOCIETYFUNDS)
            copiesToSell = int(percentage(15, SOCIETYFUNDS)/USERPRICE) #on évite les nombres à virgule
            break
        elif user == "2":
            SOCIETYFUNDS = SOCIETYFUNDS-percentage(33, SOCIETYFUNDS)
            copiesToSell = int(percentage(33, SOCIETYFUNDS)/USERPRICE) #on évite les nombres à virgule
            break
        elif user == "3":
            SOCIETYFUNDS = SOCIETYFUNDS-percentage(66, SOCIETYFUNDS)
            copiesToSell = int(percentage(66, SOCIETYFUNDS)/USERPRICE) #on évite les nombres à virgule
            break
        else:
            cprint("Enter a valid number!", "yellow")
    global isSmartphoneSelling
    isSmartphoneSelling = True
    mainGameMenu()

print("Loading 'passGameTime'...")
sleep(0.5)
def passGameTime():
    cls()

    global isMarketingActive
    global MARKETINGLEVEL
    global SOCIETYFUNDS
    global NVIDIASERIES
    global INTELSERIES
    global MEDIATEKSERIES
    global QUALCOMMSERIES
    global currentSmartphoneName
    global SMARTPHONEMARK
    global USERPRICE
    global isSmartphoneSelling
    global copiesToSell

    _RANDINT = percentage(random.randint(2,7), copiesToSell)
    
    while isSmartphoneSelling == True:
        cls()
        cprint("===Passing time===", "grey", "on_white")
        print("Smartphone name: ["+colored(currentSmartphoneName, "cyan")+"]")
        print("==================================")
        print("Copies to sell: "+str(int(copiesToSell)))
        print("Society Money: "+str(int(SOCIETYFUNDS)))
        print("Smartphone Mark: "+str(SMARTPHONEMARK))
        copiesToSell -= _RANDINT
        if copiesToSell < 2:
            #Test si on doit créer une nouvelle gamme
            BRANDS = ["NVIDIA", "INTEL", "MEDIATEK", "QUALCOMM", "ALL"]
            if random.randint(1,4) == 1: #Une chance sur 4 d'avoir une nouvelle série
                newSeries(random.choice(BRANDS))
                pass
            else:
                pass
            isSmartphoneSelling = False #On sort de la boucle
            isMarketingActive = False
            MARKETINGLEVEL = 0
            cprint("Selling done!", "cyan")
            pause()
            mainGameMenu()
        else:
            if isMarketingActive == True:
                SOCIETYFUNDS += (_RANDINT*USERPRICE) * SMARTPHONEMARK * MARKETINGLEVEL
                sleep(0.2)
                pass
            else:
                SOCIETYFUNDS += (_RANDINT*USERPRICE) * SMARTPHONEMARK
                sleep(0.2)
                pass
print("Loading 'marketingMenu'...")
sleep(0.4)
def marketingMenu():
    global MARKETINGLEVEL
    global isMarketingActive
    global SOCIETYFUNDS
    cls()
    while True:
        cls()
        cprint("===Marketing===", "grey", "on_white")
        print("1/ Low-priced marketing (magazines) [500,000$]")
        print("2/ Standard marketing campain (billboards) [5,000,000$]")
        print("3/ AAA marketing campain (TV) [10,000,000$]")
        print("\n4/ [Exit]")
        print("\n"+("="*16))
        user = input(">")
        if user == "1":
            MARKETINGLEVEL = 1
            isMarketingActive = True
            SOCIETYFUNDS -= 500000
            mainGameMenu()
        elif user == "2":
            MARKETINGLEVEL = 2
            isMarketingActive = True
            SOCIETYFUNDS -= 5000000
            mainGameMenu()
        elif user == "3":
            MARKETINGLEVEL = 3
            isMarketingActive = True
            SOCIETYFUNDS -= 10000000
            mainGameMenu()
        elif user == "4":
            mainGameMenu()
        else:
            cprint("Please enter a valid number!", "yellow")
            continue
def employeesMenu():
    cprint("as the game's not finished yet, this menu is not accessible", "yellow")
    pause()
    mainGameMenu()
def smartphoneList():
    cprint("as the game's not finished yet, this menu is not accessible", "yellow")
    pause()
    mainGameMenu()

print("Done!")
print("running 'setupGame()'...")
sleep(0.5)
print("running 'mainGameMenu()'...")
sleep(0.2)
setupGame()
mainGameMenu()