import os

import wildmagic.wild_magic as wildTable

from wildmagic.wild_text_to_spreadsheet import converter

"""
1. Store the names of player characters in a .csv
    1.1 Use these player characters so that only a number (rather than a full name) needs to be typed to store effects that are effecting them
2. For the default table, using the known split in categories of effects (effects caster, target, etc.) add useful information to help with determining who the effect should be applied to
3. Since some effects, effect the world add a separate outcome category so that these can be noted

"""

def wildMagicMenu():
    """
    The menu system for the Wild Magic part of the program

    INPUT:
        None
    
    OUTPUT:
        returns nothing
    """
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
                currEffect = wildTable.getEffect(effects, maxNo, effectNo)

                categoryOfEffect, categoryOfEffectInteger = wildTable.getCategory(effectNo, True)

                print(f"Type of Effect: {categoryOfEffect}")

                print(f"{effectNo} - {currEffect}")
                print("-----------------")

                inp = input("Would you like to save the result? [y]/n")

                if inp.lower() != "n":
                    """
                    Implement for categoryOfEffectInteger 3

                    This needs to handle apply the effect to areas, ranging from the world or moon, to a small area. 
                    Along with applying an effect to multiple people
                    """

                    #Based upon which category is in effect, it will require different manners of book keeping
                    if categoryOfEffectInteger == 1 or categoryOfEffectInteger == 2:
                        print("Who is the effect being applied to?")
                        print("(C)haracter - default option")
                        print("(O)bject (e.g. a building, chair, etc.)")

                        inp = input("~ ")
                        
                        targetOfEffect = ""
                        if inp.lower() == "o":
                            targetOfEffect = "objects"
                        else:
                            targetOfEffect = "characters"

                        names = wildTable.readShortCuts(targetOfEffect, True)

                        namesList = list(names.keys())

                        print("After reading your shortcut folder...")
                        print(names.keys())
                        if len(namesList) > 0:
                            print("I found the following options:")
                            i = 1
                            for currName in namesList:
                                print(f"{i}) {currName}")

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

                        wildTable.saveOutcome(targetName, targetOfEffect, effectNo, currEffect, True)

                        #
                               

            elif inp == "3":
                stop = True



print("Hello, and welcome to my D&D program!")
print("Please enter the bracketed character to select:")

print("(W)ild Magic")
print("(E)xit")

inp = input("~ ")

if inp.lower() == "w":
    wildMagicMenu()
