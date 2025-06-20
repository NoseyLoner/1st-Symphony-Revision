import json
from time import sleep
import os

with open("/workspaces/1st-Symphony-Revision/Src/1st Symphony/Data.json","r") as File:
    Terms:dict = json.load(File)

def Clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def PrintDict(Dict:dict,Indent:int = 0):
    for Key,Value in Dict.items():
        if isinstance(Value,dict):
            print(" " * Indent,f"{Key}:")
            PrintDict(Value,Indent + 4)
        elif isinstance(Value,list):
            print(" " * Indent,f"-{Key}:")
            for Item in Value:
                if isinstance(Item,dict):
                    PrintDict(Item,Indent + 4)
                else:
                    print(" " * (Indent + 4),f"-{Item}")
        else:
            print(" " * Indent,f"{Key}:{Value}")

def PrintList(List:list):
    for Item in List:
        print(f"-{Item}")

def Main():
    print("1st Symphony Revision!")
    Parts = {1:"Introduction",2:"Exposition",3:"Development",4:"Recapitulation",5:"Coda"}
    while True:
        sleep(1)
        print("Which you want elements from?: ")
        sleep(1)
        for Key in Parts:
            print(f"{Key}. {Parts[Key]}")
        while True:
            try:
                Part = int(input("> "))
                if Part not in Parts:
                    raise ValueError
                break
            except ValueError:
                print("Invalid Input",end = "")
        Part = Parts[Part]
        Elements = list(Terms[Part].keys())
        Clear()
        print(f"You chose the '{Part}'")
        sleep(1)
        print(f"In the {Part}, what Element would you like to look at?: ")
        for AElement in Elements:
            print(f"{Elements.index(AElement) + 1}. {AElement}")
        while True:
            try:
                ElementIndex = int(input("> "))
                if ElementIndex not in range(1,len(Elements) + 1):
                    raise ValueError
                break
            except ValueError:
                print("Invalid Input",end = "")
        Clear()
        Element:str = Elements[ElementIndex]
        print(f"{Element} in the {Part}:\n")
        sleep(1)
        PrintList(Terms[Part][Element])
        break

if __name__ == "__main__":
    Main()        