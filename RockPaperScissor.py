
# 2 players
from random import randint


def  game(p1,PC):
    if((p1==1 and PC==2) or (p1==2 and PC ==3) or (p1==1 and PC ==3)):
        result = print("PLAYER 1 WON !")
        return  result
        
    elif((p1==1 and PC==1) or (p1==2 and PC==2) or (p1==3 and PC==3)):
        result = print("DRAW !")
        return  result
    elif((p1==2 and PC==1) or (p1==3 and PC ==1) or (p1==2 and PC ==3)):
        result = print("PLAYER 1 LOST !")
        return  result

Choices = ''' 1 = Rock       2 = Paper      3 = Scissor '''
print(Choices)

p1 = int(input("Player 1: Slect Your Choice: "))
PC = randint(1,3)


game(p1,PC)
    