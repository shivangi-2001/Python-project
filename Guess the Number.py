# guesss the number

from random import random
from tabnanny import check



        
                        
ask = input("ready to play yes or no : ")


def guessFun():
            guessNum = int(random()*100)
            print(guessNum)

            def check(enterNum):
                    if(enterNum>guessNum):
                        return " HINT:  enter less than entered Number" 
                    else:
                        return "HINT:  enter greater than entered Number"
                        
            def askagain():
                ask = input("ready to play yes or no : ")
                guessFun()

            print('''
                    you get 5 guess each time for wrong answer 
                    you get the HINT
                    All The Best 

                    Ready GO!!
            ''')
            g=5
            while (g > 0):
                fg = int(input('First guess :'))
                g-1
                print(g-1)
                if(fg == guessNum):
                    print("you guess the right number: ",fg)
                    print(askagain())
                else:
                    print(check(fg))  
                    sg = int(input('Second guess :'))
                    g-2
                    print(g-2)
                    if(sg == guessNum):
                        print("you guess the right number: ",sg)
                        break
                    else:
                        print(check(sg))
                        tg = int(input('Third guess :'))
                        g-3
                        print(g-3)
                        if(tg == guessNum):
                            print("you guess the right number: ",tg)
                            break
                        else:
                            print(check(tg))  
                            fog = int(input('Forth guess :'))
                            g-4
                            print(g-4)
                            if(fog == guessNum):
                                print("you guess the right number: ",fog)
                                break
                            else:
                                print(check(fog)) 
                                lc = int(input('last chance :'))
                                g-5
                                print(g-5)
                                if(lc != guessNum):
                                        print('''
                                        OOPS!!!!!!!!!!!!!!!!!!!
                                        play again 
                                        write number is 
                                        ''',guessNum)
                                else:
                                    print("you guess the right answer")
        
      

if(ask=="yes"):
    print(guessFun())
else:
    print("play some times later")
    





