#SNAKE WATER AND GUN GAME
#CODER:Muhammad Saliq
#SIMILAR TO ROCK PAPER AND SCISSOR GAME
import random
#computer will choice random no from it
comp=random.choice([0,1,2])
dic={
    "s":0,
    "w":1,
    "g":2,
}
#Telling the user what to select among
print(""" select the letter, 
      s=snake
      w=water
      g=gun """)
#taking user input in string 
your_choice=input("enter your choice among them:").lower()
#preventing program from crash if user input wrong
if your_choice not in dic:
    print("invalid letter select among (s/w/g):")
    exit()
#now string is converting back to number 
your_no=dic[your_choice]
#showing them thier output in string
dic_reverse={
    0:"snake",
    1:"water",
    2:"gun",
}
print("comp choose: ",dic_reverse[comp])
print( "you choose: ",dic_reverse[your_no])
#now doing logic and check whats the result
if(your_no==comp):
    print("MATCH IS DRAW")
else:
    if(your_no==0 and comp==1):
        print("you win!")
    elif(your_no==0 and comp==2):
        print("you lose!")
    elif(your_no==1 and comp==0):
        print("you lose!")
    elif(your_no==1 and comp==2):
        print("you win!")
    elif(your_no==2 and comp==0):
        print("you win!")
    elif(your_no==2 and comp==1):
        print("you lose!")


 
