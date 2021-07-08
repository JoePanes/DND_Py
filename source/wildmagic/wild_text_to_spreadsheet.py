import csv

file = open("../../text/WildMagicEffects.txt", "r")
effects = []
currentLine = file.readline()
#Stop at end of file
while currentLine != "":

    #Separate number from text
    currentLine =  currentLine.split(None, 1)

    #Check whether actually a number
    try:
        int(currentLine[0])
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

print(effects)            


