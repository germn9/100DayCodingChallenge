#German Krugkov
# 100 days of coding project 4
# Rock Paper Scisors

import random


#r = random.randint(0, 10)
#r = random.random()*5


computer_selection = ["rock", "paper", "scissors"]

r = random.randint(0,2)
if r==0 :
    print(computer_selection[0])
elif r==1 :
    print(computer_selection[1])
else:
   print(computer_selection[2])

