file = open("../../text/WildMagicEffects.txt", "r")

currentLine = file.readline()
#Stop when reached end of file
#while currentLine != "":

currentLine =  currentLine.split(None, 1)

try:
    int(currentLine[0])

except:
    print("An error within the text file has been discovered")
    print(f"Resulting in {currentLine[0]} existing where a number was expected")

print(currentLine[0])
print(currentLine[1])  
            


