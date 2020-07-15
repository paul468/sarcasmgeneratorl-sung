answer = input("Möchtest du mit einem grossbuchstaben starten?")
satz = input()
word = ''

f = open("output.txt", "w+")
def converter():

    global satz, word
    counter = 0

    for i in range(len(satz)):

        counter = counter + 1
        if satz[i].isupper():
            word += satz[i]
        elif answer == "ja" and satz[i] == satz[0]:
            word += satz[i].upper()
        elif answer == "nein" and satz[i] == satz[0]:
            word += satz[i].lower()
        elif satz[i] == 'i':
            word += 'i'
        elif satz[i] == 'l':
            word += 'l'
        elif ((counter % 2) == 0):  

            word += satz[i].swapcase()
        else:
            word += satz[i].lower()
    print("Die umformatierte Version ist: " + word)
        
    f.write(word)
    return word 

test = converter()
