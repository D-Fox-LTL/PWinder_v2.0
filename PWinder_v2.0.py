import sys
import os
from collections import Counter


lsWL: list = []     #list WordList
strWL: str = ""
lsPW: list = []
strPath: str = ""
intCheck: int = 0
numberOfPasswds: int = 0
filtered_pw = []
showNumberOfPasswds: str = ""       #y or n 
keepOpen: bool = True
numberOfPasswdsToScan: int = 1_000_000
batchScan: int = 0


def CountLetters(wordList, position):
    first_letters = [word[position].upper() for word in wordList if word]  # Extracting letters and converting to uppercase
    letter_counts = Counter(first_letters)
    return letter_counts

while(keepOpen):
    #Logo
    print("|-\\ \\            /\n|-/  \\    /\\    /\n|     \\  /  \\  /\n|      \\/    \\/   INDER")

    lsWL: list = []     #list WordList
    strWL = ""
    lsPW = []
    strPath = ""
    intCheck = 0
    numberOfPasswds = 0
    filtered_pw = []
    showNumberOfPasswds = ""       #y or n 




    #Defining path, for more experienced users change it in the code directly

    print("\n\nPATH SHOULD LOOK LIKE THIS:\n         c:\\Windows\\System32\\system.ini\n")
    strPath = str(input('Type WordList path (WL has to be .txt)(Write only one \\ here): '))

    #OR

    #strPath = "c:\\CHANGE\\THOSE\\THINGS.txt"          #Note we use double \\ here, that's bcs of syntax, without it this line won't work
    
    if strPath=="":
        print("Path not defined!")
        sys.exit()
    
    try:
        intPW = int(input('\nType how long is the password: '))
    except:
        print("Should be a number stupid...")
        sys.exit()

    try:
        with open(strPath, "r", encoding="utf8") as file:
            for line in file:
                # Split the line into words and add them to the list
                if len(line) == intPW+1:
                    words = line.split()
                    lsWL.extend(words)
                        
    except FileNotFoundError:
        print("File not found!")
        sys.exit()
    
    
    for strPW in lsWL:
            if(len(strPW)==intPW):
                lsPW.append(strPW)


    print("\nWill ask about characters on position, if you don't know then click enter else write the known char")
    while(intCheck!=intPW):
        numberOfPasswds = 0
        A: str = ""
        A = input('\nDo you know char on position ' + str(intCheck+1) + '?: ')
        if str(A)=="":
            intCheck+=1
        elif len(str(A)) == 1:
            filtered_pw = [strPW for strPW in lsPW if strPW[intCheck] == str(A)]
            lsPW = filtered_pw
            intCheck += 1
        else:
            print("an error occured, please try again")
        







    print("POSSIBLE PASSWORDS:\n")
    for strPW in lsPW:
        print(strPW + '\n')
        numberOfPasswds += 1

    print(f"Number of passwords: {numberOfPasswds}")

    intCheck = 0

    while(intCheck!=intPW):
        # Count occurrences of first letters
        letterOccurrences = CountLetters(lsPW, intCheck)
    
        #sorting by num of occurences
        sortedOccurrences = sorted(letterOccurrences.items(), key=lambda x: x[1], reverse=True)
    
        # Display the occurrences
        print(f"\nNumber of occurences of certain numbers on position {intCheck+1}:")
    
        for letter, count in sorted(sortedOccurrences):
            print(f"{letter}: {count}")
        
        del(letterOccurrences)
        del(sortedOccurrences)
        intCheck+=1




    A = str(input('To continue write "y" else it will close: '))
    if(A!="y"):
        keepOpen = False
        
    print("\n\n\n\n")
