dicA = {
    'Abandon':'To give up completely, leave permanently, lack of inhibition.',
    'Abase':"To humiliate or degrade",
    "Abashed":"Embarrassed or ashamed",
    "Abate"	:"Become less severe or widespread",
    "Assiduous"	:	"Diligent, showing great care and thoroughness",
    "Assuage"	:	"To calm, make less severe, soothe, satisfy a desire",
    "Astute"	:	"Shrewd, crafty",
    "Asunder"	:	"Literally apart, into pieces",
    "Atone"	:	"Make amends for",
    "Attenuate"	:	"Make thin or weaker, to lessen",
    "Attrition"	:	"Gradual wearing down, wearing away by or as by friction",
    "Atypical"	:	"Not typical",
    "Audacious"	:	"Bold, daring",
    "Augment"	:	"To increase, to make large in number",
    "Avarice"	:	"Greed for wealth, greed for money",
    "Aver"	:	"To declare to be true, to assert, to declare to be the case",
    "Axiom"	:	"A statement universally accepted as true",
    "Apprehend"	:	"Grasp the meaning of, arrest",
    "Apostrophe"	:	"Used to indicate either possession or the omission of letters or numbers",
    "Avuncular"	:	"Kind and friendly towards an younger person",
    "Awry"	:	"Away from the expected course or position"
}

dicB={
    "Babble":"Talk rapidly in a foolish or confused way",
    "Backlog":"A build up of work, an accumulation or reserve",
    "Badger":"To nag, annoy, pester",
    "Baleful":"Menacing, deadly, harmful",
    "Banal":"Predictable and unoriginal, trite, commonplace",
    "Banter":"Playful teasing, friendly teasing",
    "Baritone":	"A man's singing voice between tenor and bass",
    "Barrage":"Large number of questions or complaints, heavy attack",
    "Bashful":	"Shy, easily embarrassed",
    "Baulk":"Hesitate to accept, thwart or hinder",
    "Bawdy"	:"Indecent, obscene"
}

dic = {
    'A':dicA,
    'B':dicB
}

         


def mydic2():
    ask = input("From which letter you want to search: (A_Z)  ").upper()
    if(ask):
        askWord = input("enter the word: ").capitalize()
        key = dic[ask]
        if(askWord not in key):
            print('You enter the wrong word, Try some other words ')
            mydic2()
        else:
            searched = key[askWord]
            print(askWord+" "+ ":" +" "+searched)
            askagain = input('You Want To Search Again : y or n  ').casefold()
            if(askagain == 'y'):
                mydic2()
            else:
                print('''
                    Bye Bye pocket dictionary see you later !!
                ''')
                

                
 
 
 
 
 
 
mydic2()



