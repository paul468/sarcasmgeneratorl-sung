import re

#filename = input("Unter Welchen filenamen möchtest du deinen fertigen Satz speichern")
answer = input("Möchtest du mit einem Grossbuchstaben starten?")
satz = input()
word = ''

text = re.findall("/w", satz)
#f = open(filename + "txt", "w+")
def converter():
    choice = 2
    global satz, word
    counter = 0
    if answer == "ja":
        choice = 1
    elif answer == "nein":
        choice = 0

    for i in range(len(satz)):
        if satz[i] in text:
            
            counter = counter + 1
            if satz[i].isupper():
                word += satz[i]
            elif satz[i] == 'i':
                word += 'i'
            elif satz[i] == 'l':
                word += 'l'
            elif ((counter % 2) == choice):  
                word += satz[i].swapcase()
            else:
                word += satz[i].lower()
        else:
            word += satz[i]
    print("Die umformatierte Version ist: " + word)
        
 #   f.write(word)
    return word 

test = converter()
