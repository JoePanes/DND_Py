import csv
from random import randint
"""


4. Have a feature that keeps track of the effects that have been triggered
    4.1 Create a CSV file for it
    4.2 Have each row contain the date and time that this was selected
    4.3 Store the number and effect, so that it is not dependent on looking elsewhere
    4.4 Give a prompt so that the characters name can be written, if it returns blank, ask for confirmation (with a second blank).
        4.4.1 If still blank, then don't add it to the csv

"""
SPREADSHEET_PATH = "../../spreadsheets/"
CURRENT_TABLE = "WildMagicEffects"

def readEffectsFile(fileName):
    """
    Read in a CSV file, and prepares the data to be in an easy and quickly referenceable format.

    Worth noting, the presumption is that the csv file is in order and the numbers are positive.
    If this is not the case, then either consider altering your input file, or change the logic used within this file.
    
    INPUT:
        :param fileName: String, the name of the file

    OUTPUTS:
        returns, dictionary containing all effects and the number of the last effect

    """ 
    wildMagic = {}
    effectNo = 0
    with open(SPREADSHEET_PATH + "wildmagic/" + fileName + ".csv", "r") as dataFile:
        myReader = csv.DictReader(dataFile)

        for row in myReader:
            effectNo = int(row["number"])
            wildMagic[effectNo] = row["effect"]

    return wildMagic, effectNo

def randomlySelectEffect(effects, maxNo):
    """
    Provide a effect from the list

    INPUTS:
        :param effects: Dictionary, where the keys are Integers and all potential effects are Strings
        :param maxNo: Integer, the number of the last effect
    
    OUTPUT:
        returns nothing, but prints the effect
    """
    number = randint(1, maxNo)

    print(f"{number} - {effects[number]}")

def getEffect(effects, maxNo, desiredNo):
    """
    If valid, returns the effect of the specified number

    INPUTS:
        :param effects: Dictionary, where the keys are Integers and all potential effects are Strings
        :param maxNo: Integer, the number of the last effect
        :param desiredNo: Integer, the number to be returned
    OUTPUT:
        returns nothing, but prints the effect
    """

    if 1 <= desiredNo <= maxNo:
        print(f"{desiredNo} - {effects[desiredNo]}")
    else:
        print("Invalid number, please check what you have entered")

def saveOutcome(characterName, effectNo, effect):
    """
    After the retrival of an effect, save the effect to the corresponding character's spreadsheet

    INPUTS:
        :param characterName: String, the name of the character upon which the effect is being applied
        :param effectNo: Integer, the corresponding number of the effect
        :param effect: String, the description of what the effect does

    OUTPUT:
        returns nothing, but saves the effect to a csv
    """

    pass
wildTable, maxNo = readEffectsFile(CURRENT_TABLE)

getEffect(wildTable, maxNo, 100)