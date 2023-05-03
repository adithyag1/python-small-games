#hangman
#rules
print("""Welcome to Hangman! The rules of the game are as mentioned below:
1. A word or a phrase is given.
2. Enter alphabets one at a time to fill the word.
3. If the alphabet is present in the word, it will reveal itself; Else, you lose a life.
4. You have 7 lives.
5. Enter only one alphabet at a time.
7. Too many invalid inputs can lead to disqualification.

Good Luck!
""")
#some requisties
from random import choice
lives=7
warning=3
warn=3
lirep=[]
licat=["FICTION","THE OUTER SPACE","THE ANIMAL KINGDOM","STATUES, MONUMENTS, HERITAGE SITES AND ARTECRAFTS","GEOGRAPHY AND FAMOUS PLACES","FAMOUS PERSONS"]
liword=[["RUMPELSTILTSKIN","CINDERELLA","HARRY POTTER","THE WIZARD OF OZ","KING MIDAS","GERONIMO STILTON",""],\
        ["THE BIG BANG THEORY","ANDROMEDA","JUPITER","MANGALYAAN","LAIKA THE SPACE DOG","URSA MINOR","KEPLER BELT"],\
        ["EASTERN GREAT EGRET","THE NILGIRI TAHR","DUCK BILLED PLATYPUS","LION TAILED MACAQUES"],\
        ["JATAYU","THE DANCING GIRL","THE PYRAMIDS OF GIZA","KONARK SUN TEMPLE","MOAI","AJANTA AND ELLORA CAVES"],\
        ["SIERRA LEONE","THE DOMINICAN REPUBLIC","THE GREAT BARRIER REEF","KANCHENJUNGA","THE PAMBAN BRIDGE","MAUNA LOA"],\
        ["ARVIND KEJRIWAL","NICOLAS TESLA","SAROJINI NAIDU","SOCRATES","AZIM PREMJI","EDWIN ALDRIN"]]
playagain="yes"
#play again
while True:
    playagain=input("Press E to play hangman: ")
    print()
    if warn>0:
        if playagain in "eE":
            lirep.clear()
            lives=7
#selecting category and word
            print("Choose the category: ")
            for i in licat:
                print("    ",licat.index(i)+1,".",i)
            print()
            cat=input("Enter ONLY THE NUMBER corresponding to the category: ")
#making the question mark
            if True:#not actually necessary but have to correct the indent for ALL the following lines
                if len(cat)==1 and "1"<=cat<=str(len(licat)):
                    print("Category chosen: ",licat[int(cat)-1])
                    print()
                    word=choice(liword[int(cat)-1])
                    l=list(word)
                    for i in l:
                        if "A"<=i<="Z":
                            l[l.index(i)]="?"
                    x="".join(l)
                    print("The word is: ",x)
#main body
#conditions for winning, losing and warning
                    while "?" in l:
                        if(lives>0)and(warning>0):
#getting input and checking if valid
                            inp=input("Enter the alphabet: ")
                            inp=inp.upper()
                            if len(inp)==1 and "A"<=inp<="Z" and inp not in lirep:
                                lirep.append(inp)
#checking if alphabet in word
                                if inp in word:
                                    l[word.index(inp)]=inp
                                    h="".join(l)
                                    if word.count(inp)==1:
                                        print("The word is",h)
                                        print("Lives left: ",lives)
                                        print()
                                    elif word.count(inp)>1:
                                        for j in word:
                                            if inp==j:
                                                for k in range(1,len(word)-word.index(j)):
                                                    if word.find(j,word.index(j)+k)!=-1:
                                                        l[word.find(j,word.index(j)+k)]=inp
                                                        h="".join(l)
                                        print("The word is",h)
                                        print("Lives left: ",lives)
                                        print()
#wrong alphabet -- take a life away
                                else:
                                    lives-=1
                                    print("Wrong alphabet!")
                                    print("Lives left: ",lives)
                                    print()
#invalid input conditions
                            elif len(inp)!=1:
                                warning-=1
                                print("Invalid input: Enter exactly one alphabet.")
                                print("You have",warning,"warnings left.")
                                print()
                            elif not("A"<=inp<="Z"):
                                warning-=1
                                print("Invalid input: Do not enter numbers or special characters.")
                                print("You have",warning,"warnings left.")
                                print()
                            elif inp in lirep:
                                warning-=1
                                print("Invalid input: You have already entered this alphabet.")
                                print("You have",warning,"warnings left.")
                                print()
#losing the game
                        elif lives==0:
                            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
                            print("You lose!!")
                            print("The word was",word)
                            print()
                            break
#invalid warning -- alphabet
                        elif warning==0:
                            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
                            print("You have entered too many invalid inputs!")
                            break
#winning the game
                    else:
                        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        print("Congratulations! You win.")
                        print("The word was",word)
                        print()
#invalid warning -- category
                else:
                    warn-=1
                    print("Invalid input: enter numbers from 1 to",len(licat),"only.")
                    print("You have",warn,"warnings left.")
                    print()            
        else:
           print("Goodbye!")
           print()
           break
    else:
        print("DISQUALIFIED: You have entered too many invalid inputs!")
        break
