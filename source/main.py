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
        
        print("Use default (WildMagicEffects) table? (y/n)")

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
                print("-----------------")

                validInput = False
                while validInput == False:
                    inp = input("Who is the effect being applied to? ")
                    if inp == "":
                        print("You have entered nothing, do you not want to save the result? (y/n)")
                        
                        inp = input("~ ")

                        if inp == "y":
                            validInput = True
                    else:
                        print(f"You have written '{inp}'")
                        print("Is this correct? (y/n)")
                        
                        if input("~ ").lower() == "y":
                            validInput = True
                            """
                            NEEDS WORK ON:
                                see point 2)
                            """
                            wildTable.saveOutcome(inp, True, effectNo, currEffect, True)
    

            elif inp == "3":
                stop = True



print("Hello, and welcome to my D&D program!")
print("Please enter the bracketed character to select:")

print("(W)ild Magic")
print("(E)xit")

inp = input("~ ")

if inp.lower() == "w":
    wildMagicMenu()
