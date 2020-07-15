answer = input("Möchtest du mit einem grossbuchstaben starten?")
satz = input()
word = ''

f = open("output.txt", "w+")
def converter():
    etwas = 2
    global satz, word
    counter = 0
    if answer == "ja":
        etwas2 = 1
    elif answer == "nein":
        etwas2 = 0

    for i in range(len(satz)):

        counter = counter + 1
        if satz[i].isupper():
            word += satz[i]
        elif satz[i] == 'i':
            word += 'i'
        elif satz[i] == 'l':
            word += 'l'
        elif ((counter % 2) == etwas2):  

            word += satz[i].swapcase()
        else:
            word += satz[i].lower()
    print("Die umformatierte Version ist: " + word)
        
    f.write(word)
    return word 

test = converter()
