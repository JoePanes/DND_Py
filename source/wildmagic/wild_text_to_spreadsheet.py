import csv

INPUT_PATH = "../../text/"
OUTPUT_PATH = "../../spreadsheets/"

currentFileName = "WildMagicEffects"

file = open(f"{INPUT_PATH}{currentFileName}.txt", "r")
effects = []
currentLine = file.readline()
#Stop at end of file
while currentLine != "":

    #Separate number from text
    currentLine =  currentLine.split(None, 1)

    try:
        #Check whether a number, and convert 0000 into 10000
        if int(currentLine[0]) == 0:
            currentLine[0] = "1" + currentLine[0]

    except:
        print("An error within the text file has been discovered where a number should be")
        print(f"What was found:\n{currentLine[0]}")
        exit()

    #remove new line character
    if currentLine[1][-1:] == "\n":
        
        currentLine[1] = currentLine[1][:-1]

    currentEffect = {"number":currentLine[0], 
                    "effect":currentLine[1]} 

    effects.append(currentEffect)

    currentLine = file.readline()
    
with open(OUTPUT_PATH + "wildmagic/"+ currentFileName+".csv", "w") as optFile:
    #Get field names
    fieldNames = list(currentEffect.keys())
    fieldNameDict = {}
    for currField in fieldNames:
        fieldNameDict[currField] = currField

    myWriter = csv.DictWriter(optFile, fieldNames)
    
    #Add field names to file
    myWriter.writerow(fieldNameDict)

    for newRow in effects:
        myWriter.writerow(newRow)
    
