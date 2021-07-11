import csv
import os

from random import randint
from datetime import datetime

"""


4. Have a feature that keeps track of the effects that have been triggered

    4.4 Give a prompt so that the characters name can be written, if it returns blank, ask for confirmation (with a second blank).
        4.4.1 If still blank, then don't add it to the csv

"""
SPREADSHEET_PATH = "../../spreadsheets/wildmagic/"
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
    with open(SPREADSHEET_PATH + fileName + ".csv", "r") as dataFile:
        myReader = csv.DictReader(dataFile)

        for row in myReader:
            effectNo = int(row["number"])
            wildMagic[effectNo] = row["effect"]

    return wildMagic, effectNo

def getNumber(maxNo):
    """
    Provide a valid number within range

    INPUTS:
        :param maxNo: Integer, the number of the last effect
    
    OUTPUT:
        returns an Integer, within range of the effects table
    """
    try:
        number = randint(1, maxNo)
    except:
        print("Invalid max number provided, please check your effects spreadsheet is correct.")
    return number

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
        return effects[desiredNo]
    else:
        print("Invalid number, please check what you have entered")

def randomlySelectEffect(effects, maxNo):
    """
    Provide an effect at random
    
    INPUTS:
        :param effects: Dictionary, where the keys are Integers and all potential effects are Strings
        :param maxNo: Integer, the number of the last effect
    
    OUTPUTS:
        returns the effect number (Integer), and the effect description (String)
    """

    number = getNumber(maxNo)
    effect = getEffect(effects, maxNo, number)

    return number, effect

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
    filePath = SPREADSHEET_PATH + "characters/" + characterName + ".csv"

    #Check whether file already exists
    fileExists = False
    if os.path.isfile(filePath):
        fileExists = True

    fieldNames = {
        "number"    : "number", 
        "effect"    : "effect", 
        "date&time" : "date&time"
        }

    with open(filePath, "a") as dataFile:
        myAppender = csv.DictWriter(dataFile, fieldNames)

        if fileExists == False:
            myAppender.writerow(fieldNames)

        newRow = {
            "number" : effectNo,
            "effect" : effect,
            "date&time" : datetime.now().strftime('%d_%m_%Y_%H_%M_%S'), 
        }
        myAppender.writerow(newRow)