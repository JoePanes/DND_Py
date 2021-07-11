from wildmagic.wild_text_to_spreadsheet import converter
import wildmagic.wild_magic as wildTable


def wildMagicMenu():
    print("You are currently in the Wild Magic Menu")
    print("(1) Would you like to update the spreadsheet?")
    print("(2) Use the Wild Magic table?")


    inp = input("~ ")

    if inp == "1":
        converter(False)
    
    elif inp == "2":
        pass


print("Hello, and welcome to my D&D program!")
print("Please enter the bracketed character to select:")

print("(W)ild Magic")
print("(E)xit")

inp = input("~ ")

if inp.lower() == "w":
    wildMagicMenu()
