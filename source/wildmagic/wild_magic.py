import csv
import os

from random import randint
from datetime import datetime

SPREADSHEET_PATH = "../../spreadsheets/wildmagic/"
SOUND_EFFECT_PATH = "../../audio/wildmagic/"

CURRENT_TABLE = "WildMagicEffects"

def readEffectsFile(fileName, calledFromParentFolder=False):
    """
    Read in a CSV file, and prepares the data to be in an easy and quickly referenceable format.

    Worth noting, the presumption is that the csv file is in order and the numbers are positive.
    If this is not the case, then either consider altering your input file, or change the logic used within this file.
    
    INPUT:
        :param fileName: String, the name of the file
        :param calledFromParentFolder: Boolean, whether the function is being called from one level above

    OUTPUTS:
        returns, dictionary containing all effects and the number of the last effect

    """
    spreadsheetPath = getSpreadsheetPath(calledFromParentFolder)

    wildMagic = {}
    effectNo = 0
    with open(spreadsheetPath + fileName + ".csv", "r") as dataFile:
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

def saveOutcome(name, targetOfEffect, effectNo, effect, calledFromParentFolder=False):
    """
    After the retrival of an effect, save the effect to the corresponding character's spreadsheet

    INPUTS:
        :param name: String, the name upon which the effect is being applied
        :param targetOfEffect: String, determine which folder to save it to
        :param effectNo: Integer, the corresponding number of the effect
        :param effect: String, the description of what the effect does
        :param calledFromParentFolder: Boolean, whether the function is being called from one level above

    OUTPUT:
        returns nothing, but saves the effect to a csv
    """
    spreadsheetPath = getSpreadsheetPath(calledFromParentFolder)
    
    filePath = spreadsheetPath + "applied_effects/" + targetOfEffect + "/" + name + ".csv"
    
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

def getCategory(effectNo, calledFromParentFolder=False):
    """
    The default magic table is organised in sections, each section effects a different person(s) or area
    
    INPUT:
        :param effectNo: Integer, the number of the effect to be looked up
        :param calledFromParentFolder: Boolean, whether the function is being called from one level above

    OUTPUT:
        returns a string and integer pertaining to which category
    """  
    if effectNo == 9894 or effectNo == 9918 or effectNo == 9927:
        print("Apocalyptic")
    
    elif effectNo == 10000:
        print("P̴̢̢̧̨̢̳̞̫͓͕̻͍̫̬͎̺̖͓͓̲͈̙͉̗̟̻͓̮̮̠͙̹̥̰̿̾͛̊́͛̃̅̈́̐̈͐͐̽̀͋̐͌̆́̈͋̋̀̆̾̽̏͌͛̓̍̆͌̉̽̈̅͊́̾́̌̕̚̕̚̚̕͜͜ͅh̷̨̛͚̮͍̥̹̺̯͍̪̝̠̥̗̝͎̦̩͌͐͊̐͐̍̆̉͗̑̈́̈́͌͊͊̏̏̓͑̈͋̃̅̑͊͛̐̐̐́̈́̒̎̌͂̈́̚͘͝͝͠͠'̷̛͎͗͋́̏͐̈́̑̄̈͑̊̓͑̔͐̐̐̊̄̏́͊͆̎͋́̋̀̅̎̌̽̇̈̈́̚̕̚͝n̷̡̡̡̢͕̯͎̩̟̙̣̳͖̼͉̲̯̥͖͙̭̻͓͕̘̠͖͓͕͈͍̖̜͍͈̦̖͎̖̺̦̈̍̅̽͗͑͛̊̇̀̿̓̀̀͆́͛͋͋͐̐̀̊̈́̒̊̌̾͛͗͜͜͠ͅͅg̶̢̡̨̨̛̲̞͍̣̪̫͉̝͎̞͓̹̳̼͖͉͎̲̪̭͍̮̟̫̜̠̲͈̹̗̠̲̭̯̼̥͗̇̊̉́͌̔̌͊̓̂̀̌̈́̀͋͊͛̇̐̈́͋̒̈́̅̀̇̄͒̐͜͝͝͠ļ̶̧̡̨̧͖̫̤͓͍̝͙̫̫͉̭͉͚̝̬͈̫̼̜̟̱͇̫̟͇͍̯̱͎̻͔̠̙̊̈́̈͂̾̌̈́͋͐̒̈̑͆̒̃̆͆͋͒̽̿́́͆̽͑͊̍͘̕͝͝ͅư̶̢̨̢̢̧̖̱̹͇̭̱͇͚̮̫̫͎̼̟͇̰̹̹͖̰̣̮̰͔̮͙̥̲͓̬̓̀͆̈́̇̑͒̃̈́̉͂́̿̾̎̒͗͘͜͜͜͜͝͝͝i̸̢̡̱͉̩̩̜͕͓̭̫̤̋͋́̎̓̑̽͊̒͌͛͋̈́͋̀̋̌̀́̉̈́́̔͒̑͑̾͂̌̃̅͘̚̚͠͝͝͝ ̷̢͉͓̦̗̞̗͔̬̬̘̮̬́̾͒m̴̧̧̨̧̬̳̪̭̠̬͚̹̩̩̮̯͈̰̗̞̦̲̗̞̺̹͔̟̫̼̭̫̦̠̗̗͓̤̙̪̈̃͊̂̆͂̔ͅg̴̛͙̳̽̎̓̒̍̒͂͂̔̉͐͠ļ̷̥̟̹̙̤̹̞̜͔̑̍̈́̅͌͗̃̊̊͐̇̎̉̃̎̀̐͑̎͒͌̍̈́̇́̀̽̿͆͂̔͋͘̕͘̕̕͜͝͝ͅw̸̡͎̩͓͌̊̿̌̓̓͐͒̅͛̇̍́̍̇̌̓̏̈́̑̏̈́͐͆̃́͌̂̈́͒̀̕̚͘̕̕͝͝͝͠'̷̧̢̢̢̛̛̟͎̙̻͈̗̬̲̰̤̹̤͕͓̣̪̫̣̼̓̀͂̔̌̓͒̍̈̉̓͒̃̉̆̓̔͗́͑͊̀̊̇͘͘͘͜͠ͅṇ̷̨̡̡̛̘̣̫̳̙̤͍̘͈̝̯̱̣̲̗͕̣͍̖̗̬̯̺̗̟̯̰̙̠̩̻̦̎̎̒́̇͛̉̀̾̈́͗̆̓͊̽̉̓̍́̕͜͝͝͠ä̶̡̢̢̻͙̜̻̯̟̺̲̥̦̥̞̙̗̩̤̯͓̱͚͓̝̠̠͙̭̞̮̫͈͎̬̝͚̜͍̘̭̩̱̼̹̹̉̈́͒̒̓͗̔͆̏̓͆́͛͛̉̚͘̕͜f̷̨̡̛̤̤͎̻͍̣̤͓̱̤̜̘̞̝̰̘̼̗͖̳̻̘̗̲̯̥̜͕̮̋̈́͑̓̾̊̊̔͊̍͛̓͛͌͒͑̈́̀͆̊̔̍̍́́̿̒̅̋̕̕̚͜͝h̷̢̡̡̡̛̛̛̥͈͇̯̮͍̯̮̯̘͖͈͈̼͙̹̜̪̜̝̯̼̫̫̥͍͖͖̺̖̰̙̠̟̥̰͉̥̹̘̣̩͓̳͊͛̉͌̒͒̃̄́͂͌̀̈́̊͋̔̈͌͛̈́͆̚͘͜͝ͅ ̵̢̢͓̘̫͇͍͓̯͎̠̙͕͙̤̣̙̱̦͆́͆̑̉͂̇̽̒̉̓̕̚͝C̷̢̨̡̢̧̡̢̠̙̭̱͈̺͓͚̞͔̻̥̫͍̹̣̅́̑͐͑͝ͅt̶̠̜̝͓̽͌͐͊̽͑͌͘͠h̶̡̨̛̛͔͍͓̺̜̞̜͚̯̜̜͎̻̮͈̹̖̝̰̗͙͙̫̖͐̇͆̔̓̓͑́̏́͋̐̐̾̒̄̀̓̔͐̾̂̔͋̄̆̒̎̑̓͐̈́͑͗́̿̂̍̓̆̓̚̚̚͝͝͝ͅͅử̶̧̡̢̛̯̩͔͇̻̘̭̟̝͕͉̯̟͕̮̻̺̲̫̻̺̙͈̠̯̀̐̇̎̈́͐͑͒̀͋̃̆̄̃̅̒̅̂̂̓̂͋̅̅̇̾͒̃̆͊̈́͌̎̾͗̈́͆̌̃̀͘̚͘̕͜͠l̸̨̨̨̢͎̗͚̟͕͎͚͚̦̮̱̱̝̭͖̪͚̙̰̯̞̬̺̭̟̽́̂̆̈̎̆̇͌̽́̀̃̉̽̇̉̽̅͜͝͝h̴̨̧̛̻̺̙̪̣̲̣̺̜͍͉͖̪̖̪̯̟̭̤̲̻̟͙̙̞͙̗̹͋̾̏̀̂̄̈͌̂̅̍́͛̑̂̀͐̾͗̒͗̅͌̾̋́̈́̇̓̒͐͂̊͌͛̉̑̓̉̌̾̏͘͘̚͜͠͝͠u̵̡̧̢̥̞̥̩͖̝̰̖̼͚̰̘͙̹̺̭̫̥̟̤͎̯̳̰͎̭̺̩̳͎̘̰͖̯͔͉̦̔̾̍͗̓̓͋̒̔̎͛̍͂͑͌̈́̇̌͐̅̈̚̕̕͜ ̸̡̧̡̡̨̮̻̗̮͙̰͎̖̣̫̘̟̞̳̣̜̙̙̝̜̪̩̭̖͍̻̘̥̯̜̜̝̠̹̲͕̮͎͋͌̀͐͂̐̈͛͋͊̒͂̇̍͑̄̾͆̍͆̒̄̓́̒̀́͊͋͋̒̐͗̍̓͗̕͘͘̚͜͠͝͝͠ͅR̶̢̡̨̗͚̰̙̞̫̺̼̥̙̙̯͇͇̯̭̬̮̟̤͎̘͍̘͖̪̮̙͚͓̬̦̙͈̮̥̙̟̼͊̇̀́̒̐̽͑̓͜ͅ'̴̢̧̛͓͙̙͔͙̠̼̭̣̘͍̱̼̳̜̪̣͓͐̃̌̉̊̈͌̓̌̐͂̑͆̓͌͆̎̀̾͊̋̉͐̎̓́̈́̈̔̀̾̏̉́͗̌̈́̈͆̉͝ͅl̴̨̨̨̛̰͈̭͇̭͕͕̟͊̂́͌̏͐͌̅̆̈́͌͒̅̂̓̎̃͐̂̑̂͆͊̀̾͛̈́́̊̈́̿̿̒͐͌̚̕̚͠ỹ̶̢̡̧̡̧̝̯̼͎̮̭̥̙͕̣̤̠̹͖̜̩̟̒̅̄ę̷̧̟̮͙̙̺͓͉͙̫̱͓͇̟̟̠̗̭̪͕̰̖̱̮̫̹̣͙̗̠͖̼̲̘̻̰̣̬̜̻̺̤̦̖̖̈́͊̾̄͗͒̅̔̈͑̀̉͌̈́̓͒̈́͒̎̌́̈́̀͋̌̈́̽̇͛͑͂̋̂̐͛͛̂͛͛͐̕͘̕̚̕̕͜͜͜ͅḧ̶̡̡̧̢̛͔͖̬̱̻̺̗͕͔͍͇͔͓̳̬̣̺̟́̌̎̄̀̾̒̃̓̐̿̇̄̈̒͒̌̇̆̾͝ ̴̧̢̨̢͎̤̥̺̣̘̭͉͇̫͙̭̥͓̳̫̝͚̟̠͇̱̲̻̭̳͈̪͔̣̙̩͙͚̦̼̰̱̩̳̟̬̔̇̅͂̉͒̈́͐́͛̈́̊̅̄̌̓̆̆̃̃͑͑̽̿̋̀̈̀͆̑͆̒̐̈́̽̾̚͜͜͝͝ͅͅw̷̡̨̧̗͍̹̗̩͔̦͓̱̑̅́́̈͛̋̑́͑̓̓̉̕̕ģ̸̛̝͇̹͈̤̣̊̈́̊̀̒̂͒́̉̂͐́̒͊͊̈́̑̄̋̐̏̓͊̌̋̃̀̿͐̕͘͘ą̵̖͖̯̠̭̳͇̼̗͙̭̠̺̄̋͜h̷̨̡̤̗̭͈̤͚͎̟̿͆͐͆̔̃͛́͋̐͋̓̃̎̀̇̎̂̾̈́͐͐͛̏̌̈̀͛̿͗̐͂̈̀̽̆̇̓̕̕̚͜͝'̷̡̢̡̥̟͈͕̼̘͙͔͌ͅņ̸̨̨̢̧̛͖̹̠͍̟̼̭̬̤̫̰͚̻̘̲̖͇̯̭͖͇̲͚̞̟̘̻̀̔͂̈̀̓̽̉̒̇͑̊̇̾̈̅͋̏̿̓͒̃͊̌̄̏͒̈́̊̉̋̿͊̀̚̚͜͠͝͝͠a̴̧̯̥̼̪̫̅̋̐̾͌̒̓́̈́̓̂͌̒́̆͝͝g̵̢̧̢̨̢̛̖̟͚̲̗̞̩͈̱̟̞͇͖͚̣̞̟̰̘̝̥̗͈̤̬̲͉̜͎̫͚͍̞͖̟̙͚̭͓̯͚̍̌̂̔̓͂̍̇̎̌̐̋̐̆̍̎͋̐̋͒͋̉́́͆̃̄̅͊̍͋͘͜͠͝ͅͅͅĺ̴̢̢̧̰͙͉̼͕̠̲̰͓͖͈͔̣̺̩̘̬̱͓̱̣͍̭̫̖͍̪̤͙̦̻͚̝̹̗͔̦͚̞̮̼͎̤̠̈̔̃̏̒̋͆͂̾͗͘͘ͅ ̴̨̢̡̘̥͙͓̪͖̤͖̜̘͖͚̼̬̖̹̗̯̼̪̗̭̘͖͎̠͍̟̯̤̱͙͈͍̪̠̉͜͜͝f̶̢̢̡̣̭͇̣̪̼̩̥̥̬̱̬̼̮̝̫̯̪̰̰̠͈͎̪̭̩̝̦̾̒̒͂̓̕͜h̷̛̼͂̀̈́̓̈́̈̎͗̀̕̕͠ț̸̮̩̱̳̓̈̀͗̑͌̈̀͌͐̀̌̊͂̓̾̀̔̔̇̇̋̽̇̈͗̉̓̋̓̚̚͘͘͝͝a̶̢̧̡̨̛͓̣̞̞͔̯̳̩̜̯̮̰͇̥̳͈͓̬͇̪̟͂̽͐̈́̽̃̂̽͋͛̋͑͌̈́̑͑̇͐̑͂̈́̑͑̀̌̎̚̚͘̕͝ͅͅg̶̨̢̛̝͈̘̣̫̝̹̫̜͔̯̪̮̃͆̎̓̓̉͊͆̈́̐̐̈̊͆̀͊͒̈́͛̽̈́̏͂́̊́̈̈́͠͝ņ̸͕͔̟̺̫̮̞͔̳̦͛͌͛͌̀̌͊́̏͒̍͝")
        
        
    if 1 <= effectNo <= 4000:
        return "caster", 1
    
    elif 4001 <= effectNo <= 8000:
        return "target", 2
    
    elif 8001 <= effectNo <= 10000:
        return "area", 3

def readShortCuts(fileName, calledFromParentFolder=False):
    """
    Read in the .csv file of those that have previously had effects applied to them

    INPUT:
        :param fileName: String, the category of target
        :param calledFromParentFolder: Boolean, whether the function is being called from one level above
    
    OUTPUT:
        returns, a dictionary containing the contents of the .csv
    """
    spreadsheetPath = getSpreadsheetPath(calledFromParentFolder)
    names = {}

    try:
        with open(spreadsheetPath + "shortcuts/" + fileName + ".csv", "r") as dataFile:
            myReader = csv.DictReader(dataFile)

            for row in myReader:
                currName = row["name"]
                names[currName] = currName
    except:
        print("There was an error while reading the file category")
        print("If this is the first time it is being running and your shortcut files")
        print("are empty, then feel free to ignore this problem.")

    return names

def getSpreadsheetPath(calledFromParentFolder):
    """
    Determine the directory path that needs to be taken from the origin of where the function is being called

    INPUT:
        :param calledFromParentFolder: Boolean, whether the function is being called from one level above

    OUTPUT:
        returns a String, containing how to get to the spreadsheet folder
    """
    if calledFromParentFolder:
        return SPREADSHEET_PATH[3:]
    else:
        return SPREADSHEET_PATH

def saveShortcut(fileName, targetName, calledFromParentFolder = False):
    """
    Add new strings to the corresponding shortcut file for ease of access

    INPUT:
        :param fileName: String, the category of the target
        :param targetName: String, the name/descriptor of the target
        :param calledFromParentFolder: Boolean, whether the function is being called from one level above
    
    OUTPUT:
        returns nothing but add on to .csv
    """
    spreadsheetPath = getSpreadsheetPath(calledFromParentFolder)

    with open(spreadsheetPath + "shortcuts/" + fileName + ".csv", "a") as dataFile:
        myAppender = csv.DictWriter(dataFile, ["name"])
        myAppender.writerow({"name":targetName})

def getEffectedFiles(folder, calledFromParentFolder = False):
    """
    Get the names of the .csv files within the specified folder

    INPUT: 
        :param folder: String, the name of the folder to look within
        :param calledFromParentFolder: Boolean, whether the function is being called from one level above
    
    OUTPUT:
        returns a List of Strings, containing each of the existing files
    """


    spreadsheetPath = getSpreadsheetPath(calledFromParentFolder)

    files = os.listdir(spreadsheetPath + "applied_effects/" + folder + "/")

    csvFiles = []

    for currFileName in files:
        if currFileName[-4:] == ".csv":
            csvFiles.append(currFileName)

    return csvFiles

def getEffectedCSV(folder, fileName, calledFromParentFolder = False):
    """
    Retrieve the contents of the .csv

    INPUTS:
        :param folder: String, the name of the folder to access
        :param fileName: String, the name of the .csv file
        :param calledFromParentFolder: Boolean, whether the function is being called from one level above

    OUTPUT:
        returns a List of Dictionaries, containing the contents of the .csv
    """

    spreadsheetPath = getSpreadsheetPath(calledFromParentFolder)

    csvContents = []
    try:
        with open(spreadsheetPath + "applied_effects/" + folder+ "/" + fileName, "r") as dataFile:
            myReader = csv.DictReader(dataFile)


            for row in myReader:
                csvContents.append(row)
    except:
        print("While trying the read the .csv, and an error has occured.")
        print("Chances are this occured, due to the file not existing.")

    return csvContents
