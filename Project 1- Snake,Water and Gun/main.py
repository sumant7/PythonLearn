#rules
# s= snake, w=water, g=gun
# gun kills snake
# gun sinks in water
# snake drinks water

import random   #exteral module


def game(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        if you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        if you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        if you=='w':
            return True
        



print("Computer: Snake(s), Water(w) or Gun(g)?")
rand= random.randint(1,3)   #this function randomly chooses between numbers ranging from 1 to 3
if rand==1:
    comp='s'
elif rand==2:
    comp='w'
elif rand==3:
    comp='g'
print("Computer has Chosen")
you= input("Player: Snake(s), Water(w) or Gun(g)?\n")
result= game(comp,you)

if result==True:
    print("You Won!")
    print("Your Choice:",you)
    print("Computer's Choice:",comp)
elif result==False:
    print("You Lose!")
    print("Your Choice:",you)
    print("Computer's Choice:",comp)
elif result is None:
    print("Tie!")
    print("Your Choice:",you)
    print("Computer's Choice:",comp)