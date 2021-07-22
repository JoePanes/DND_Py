import os

import wildmagic.wild_magic as wildTable

from wildmagic.wild_text_to_spreadsheet import converter


def wildMagicMenu():
    """
    The menu system for the Wild Magic part of the program

    INPUT:
        None
    
    OUTPUT:
        returns nothing
    """
    targetEffectsDict = {
        "o" : "objects",
        "c" : "characters",
        "a" : "areas",
    }


    print("¬Wild Magic Menu")
    print("(1) Would you like to update the spreadsheet?")
    print("(2) Use the Wild Magic table?")
    print("(3) Exit?")

    inp = input("~ ")

    if inp == "1":
        converter(False)
    


    elif inp == "2":
        print("-Wild Magic Menu")
        print(" ¬Table")
        
        print("Use default (WildMagicEffects) table? [y]/n")

        usingDefault = False
        inp = input("~ ")
        
        fileName = ""
        
        if inp.lower() == "n":
            validInput = False
            #Get the filename and check if valid
            while validInput != True:
                fileName = input("Enter the name of the .csv file (don't include the .csv): ")
                
                filePath = wildTable.SPREADSHEET_PATH[3:] +fileName+".csv"
                if os.path.isfile(filePath):
                    validInput = True
                else:
                    print("Invalid filename, please check your input or folder")

        else:
            fileName = wildTable.CURRENT_TABLE
            usingDefault = True

        print("Reading spreadsheet...")
        effects, maxNo = wildTable.readEffectsFile(fileName, True)
        print("Successfully read spreadsheet...")
    
        stop = False
        
        while stop == False:
        
            print("(1) Select an effect")
            print("(2) Random effect")
            print("(3) Exit")
            
            inp = input("~ ")
            if inp == "1" or inp == "2":
                effectNo = ""

                if inp == "1":
                    validInput = False
                    
                    #Get a valid number from the user
                    while validInput == False:
                        try:
                            currNo = int(input(f"Enter a number in the range of 1 to {maxNo}: "))

                            if currNo < 1 or currNo > maxNo:
                                raise ValueError()
                            else:
                                validInput = True
                                effectNo = currNo
                        except:
                            print("You did not enter a valid Integer, please try again")
                else:
                    effectNo = wildTable.getNumber(maxNo)

                print("-----------------")
                effectText = wildTable.getEffect(effects, maxNo, effectNo)

                categoryOfEffect, categoryOfEffectInteger = wildTable.getCategory(effectNo, True)

                print(f"Type of Effect: {categoryOfEffect}")

                print(f"{effectNo} - {effectText}")
                print("-----------------")
                print("Would you like to save the result? [y]/n")

                inp = input("~ ")

                if inp.lower() != "n":
                    noIterations = 1
                    targetOfEffect = ""

                    #Based upon which category is in effect, it will require different manners of book keeping
                    if categoryOfEffectInteger == 1 or categoryOfEffectInteger == 2:
                        print("Who is the effect being applied to?")
                        print("(C)haracter")
                        print("(O)bject (e.g. a building, chair, etc.)")
                        validInput = False
                        while validInput != True:
                            inp = input("~ ")
                        
                            if inp.lower() == "c" or inp.lower() == "o": 
                                validInput = True
                                targetOfEffect = targetEffectsDict[inp]
                            else:
                                print("Invalid input, please try again")
                            
                        

                    elif categoryOfEffectInteger == 3:
                        print("Does the effect specify effecting specific people (not a general area or object)?")
                        print("Type either:")
                        print("(A)rea - Where it effects the world, settlement, or region in some way.")
                        print("(O)bject - Where it effects an object (e.g. the next weapon to do...)")
                        print("(C)haracter - Where it impacts one or more characters")

                        targetOfEffect = ""

                        inp = input("~ ")
                        
                        while inp.lower() not in targetEffectsDict:
                            print("Invalid input, please try again")
                            inp = input("~ ")

                        targetOfEffect = targetEffectsDict[inp]

                        
                        if targetOfEffect.lower() == "characters" or targetOfEffect.lower() == "objects":
                            print(f"How many noteworthy {targetOfEffect} affected by Wild Magic?")
                            noIterations = ""

                            while type(noIterations) != int:
                                try:
                                    noIterations = int(input("Enter number: "))
                                
                                except:
                                    print("Invalid value, please enter any number")

                    else:
                        print("ERROR")
                        print("An unexpected value has been recieved for the category of effect")
                        print("If you have made changes, then you need to specify how to handle this category")
                        
                    for _ in range(noIterations):
                        saveEffect(effectNo, effectText, targetOfEffect)
                               

            elif inp == "3":
                stop = True


def saveEffect(effectNo, effectText, targetOfEffect):
    """
    After knowing what the target is, get further information so that it is saved as a .csv
    Also, add the entered name as a shortcut option in later use.

    INPUT:
        :param effectNo: Integer, the number of the effect in the Wild Magic Table
        :param effectText: String, the description of what the effect is
        :param targetOfEffect: String, who is being effected by the magic

    OUTPUT:
        returns nothing, but saves to two .csv
    """
    names = wildTable.readShortCuts(targetOfEffect, True)

    namesList = list(names.keys())

    print("After reading your shortcut folder...")

    if len(namesList) > 0:
        print("I found the following options:")
        i = 1
        for currName in namesList:
            print(f"\t{i}) {currName}")
            i+= 1

        print("Enter the corresponding number to quickly choose that name")
        print("Otherwise, type the name/descriptor of what you wish to save the effect to")
    else:
        print("I found nothing")
        print("Please enter a name or descriptor of what you wish to save the effect to")
    
    validInput = False
    targetName = ""
    while validInput != True:
        targetName = input("~ ")

        print(f"you have written {targetName}, is this correct? y/[n]")

        confirmation = input("~ ")

        if confirmation.lower() == "y":
            validInput = True
    
    try:
        #Test whether the input is a shortcut
        shortcutNo = int(targetName)
        print(shortcutNo)
        targetName = namesList[shortcutNo-1]
    except:
        #Otherwise, this means it is a new string, therefore add it as a shortcut
        #However, just incase the written text is a duplicate of a pre-existing name, check if unique
        if targetName in names:
            i = 1
            isUnique = False
            newName = ""

            while isUnique != True:
                newName = targetName + "_" + str(i)
                i+= 1

                if newName not in names:
                    isUnique = True
            
            targetName = newName
        
        wildTable.saveShortcut(targetOfEffect, targetName, True)

    wildTable.saveOutcome(targetName, targetOfEffect, effectNo, effectText, True)


print("Hello, and welcome to my D&D program!")
print("Please enter the bracketed character to select:")

print("(W)ild Magic")
print("(E)xit")

inp = input("~ ")

if inp.lower() == "w":
    wildMagicMenu()
