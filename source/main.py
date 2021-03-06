import os

import wildmagic.wild_magic as wildTable

from wildmagic.wild_text_to_spreadsheet import converter

"""
1. Properly handle the situation when usingDefault = False
"""

def wildMagicMenu():
    """
    The menu system for the Wild Magic part of the program

    INPUT:
        None
    
    OUTPUT:
        returns nothing
    """
    categoryConversion = {
        "o" : "objects",
        "c" : "characters",
        "a" : "areas",
    }


    print("¬Wild Magic Menu")
    print("(1) Would you like to update the spreadsheet?")
    print("(2) Use the Wild Magic table?")
    print("(3) Exit?")

    inp = input("~ ")

    #Preparing and getting the program ready
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

        #Preparation complete
        stop = False
        
        while stop == False:
        
            print("(1) Select an effect")
            print("(2) Random effect")
            print("(3) See effects applied to a character/object/area")
            print("(4) Exit")
            
            inp = input("~ ")
            if inp == "1" or inp == "2":
                if inp == "1":
                    obtainEffect(False, effects, maxNo, categoryConversion, usingDefault)
                else:
                    obtainEffect(True, effects, maxNo, categoryConversion, usingDefault)
                               
            elif inp == "3":
                getAppliedEffectsFromFile(maxNo, categoryConversion)

            elif inp == "4":
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
    
    targetName = takeInAndConfirmUserInput()
    
    try:
        #Test whether the input is a shortcut
        shortcutNo = int(targetName)
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

def takeInAndConfirmUserInput():
    """
    After taking in input from a user, confirm whether there are no mistakes

    INPUT:
        NONE
    
    OUTPUT:
        returns a String, containing what the user wrote
    """
    validInput = False
    userInput = ""
    while validInput != True:
        userInput = input("~ ")

        print(f"you have written {userInput}, is this correct? y/[n]")

        confirmation = input("~ ")

        if confirmation.lower() == "y":
            validInput = True

    return userInput

def obtainEffect(choseRandom, effects, maxNo, categoryConversion, usingDefault):
    """
    Based upon the user input, get an effect, then determine whether to save it to a .csv

    INPUT:
        :param choseRandom: Boolean, whether the user wishes to randomly get an effect or select one specifically
        :param effects: List of Strings, the entire effects table
        :param maxNo: Integer, the last number within the magic table
        :param categoryConversion: Dictionary, used to convert single characters into their full names
        :param usingDefault: Boolean, whether the normal effects table is being used
    
    OUTPUT:
        returns nothing, but prints to the command line and can save to a .csv

    """    

    effectNo = ""

    if choseRandom:
        effectNo = wildTable.getNumber(maxNo)
    
    else:
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
        if usingDefault == True and (categoryOfEffectInteger == 1 or categoryOfEffectInteger == 2):
            print("Who is the effect being applied to?")
            print("(C)haracter")
            print("(O)bject (e.g. a building, chair, etc.)")
            validInput = False
            while validInput != True:
                inp = input("~ ")
            
                if inp.lower() == "c" or inp.lower() == "o": 
                    validInput = True
                    targetOfEffect = categoryConversion[inp]
                else:
                    print("Invalid input, please try again")
                
            

        elif usingDefault == False or categoryOfEffectInteger == 3:
            print("Does the effect specify effecting specific people (not a general area or object)?")
            print("Type either:")
            print("(A)rea - Where it effects the world, settlement, or region in some way.")
            print("(O)bject - Where it effects an object (e.g. the next weapon to do...)")
            print("(C)haracter - Where it impacts one or more characters")

            targetOfEffect = ""

            inp = input("~ ")
            
            while inp.lower() not in categoryConversion:
                print("Invalid input, please try again")
                inp = input("~ ")

            targetOfEffect = categoryConversion[inp]

            
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

def getAppliedEffectsFromFile(maxNo, categoryConversion):
    """
    Get the name and location of a .csv file, then display all effects in an easy to read manner

    INPUT:
        :param maxNo: Integer, the last number within the magic table
        :param categoryConversion: Dictionary, used to convert single characters into their full names
    
    OUTPUT:
        returns nothing, but prints the contents of a .csv file to the command line
    """
    print("Which would you like to access?")
    print("(A)rea")
    print("(O)bject")
    print("(C)haracter")

    inp = input("~ ")

    if inp.lower() in categoryConversion:
        folder = categoryConversion[inp.lower()]

        csvFiles = wildTable.getEffectedFiles(folder, True)

        if len(csvFiles) == 0:
            print("Sorry, but no effects have been saved for this category.")

        else:
            print("Within the category, the following files were found:")
            i = 1

            for currFile in csvFiles:
                print(f"{i}) {currFile}")
                i += 1

            print("Which one would you like to see?")
            print("Please enter the corresponding number")
            validInput = False

            while validInput != True:
                fileNumber = takeInAndConfirmUserInput()

                try:
                    fileNumber = int(fileNumber)
                    validInput = True
                except:
                    print("The value that you entered, was not a number, please try again")
            
            #Adjust for list indexs
            fileNumber -= 1
            fileName = csvFiles[fileNumber]

            fileContents = wildTable.getEffectedCSV(folder, fileName, True)
            print("")
            for currRow in fileContents:
                #Format the number so that it remains a consistent size
                formattedNumber = len(str(maxNo)) *["0"]
                splitNumber = [number for number in currRow["number"]]

                i = 1
                for currNumber in splitNumber[::-1]:
                    formattedNumber[-i] = currNumber
                    i+=1

                formattedNumber = "".join(formattedNumber)    
                
                date = currRow["date&time"]
                effect = currRow["effect"]

                print(f"{formattedNumber} | {date} | {effect}")
            print("")

    else:
        print("Invalid input, only the options listed above are valid")


print("Hello, and welcome to my D&D program!")
print("Please enter the bracketed character to select:")

print("(W)ild Magic")
print("(E)xit")

inp = input("~ ")

if inp.lower() == "w":
    wildMagicMenu()
