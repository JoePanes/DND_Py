import csv

"""

2. Be able to randomly select one of the effects
3. Be able to find one of the effects by entering a number
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
    with open(SPREADSHEET_PATH + fileName + ".csv", "r") as dataFile:
        myReader = csv.DictReader(dataFile)

        for row in myReader:
            effectNo = int(row["number"])
            wildMagic[effectNo] = row["effect"]

    return wildMagic, effectNo

wildTable, maxNo = readEffectsFile(CURRENT_TABLE)

print(wildTable)
print(maxNo)