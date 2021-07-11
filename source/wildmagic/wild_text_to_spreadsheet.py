import csv

INPUT_PATH = "../../text/"
OUTPUT_PATH = "../../spreadsheets/"


def converter(calledFromParentFolder=True):
    """
    Takes in a .txt and converts it to a more usable .csv
    
    INPUTS:
        :param calledFromParentFolder: Boolean, whether the function is being called from one level above
    OUTPUT:
        returns nothing, but creates/modifies the spreadsheet at within 
                         the OUTPUT_PATH constant
    """
    #If this function is being called from anywhere else,
    #then the constants are invalid
    inputPath = INPUT_PATH
    outputPath = OUTPUT_PATH

    if calledFromParentFolder != True:
        inputPath = inputPath[3:]
        outputPath = outputPath [3:]

    print("Would you like to:")
    print("(S)pecify a filename")
    print("(D)efault")
    print("(E)xit")

    currentFileName = ""
    
    validInput = False
    choseExit = False

    while validInput == False:
        inp = input("~ ")
        if inp.lower() == "s":
            currentFileName = input("Please enter the name of the text file...")
            validInput = True

        elif inp.lower() == "d":
            print("Default option selected... using 'WildMagicEffects'")
            currentFileName = "WildMagicEffects"
            validInput = True
        elif inp.lower() == "e":
            validInput = True
            choseExit = True
        else:
            print("You have entered an invalid command, please enter either S, D or e")
    
    if choseExit == False:
        file = open(f"{inputPath}{currentFileName}.txt", "r")
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
            
        with open(outputPath + "wildmagic/"+ currentFileName+".csv", "w") as optFile:
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