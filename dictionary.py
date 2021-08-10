import json
import difflib 

from difflib import get_close_matches 

data = json.load(open("data.json"))

def wordlookUp(word):
    
    word = word.lower()
    
    if word in data:
        if word != 'e':
            for i in  data[word]:
                print("-" + i)
    else :
        if word != 'e':
            alter = difflib.get_close_matches(word, data.keys(), n=1, cutoff=0.8)
            answer = input("are you sure you spelled that right ? or did you mean " + alter[0] + "d? Y/N  ")
            if answer == "Y":
                wordlookUp(alter[0])
    


task = 'start'

while task != "e" :
    print("\n---------------------------------------------------------------------")
    task = input("\nwhat word would you like to translate [ type e to exist ] ... ")
    print(" ")
    wordlookUp(task)


print("Thank you for using my Code >> ")
    

