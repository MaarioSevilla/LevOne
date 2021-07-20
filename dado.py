import random
from numpy import *
from sympy import true, false

players = array([0, 0, 0, 0, 0, 0])
turno=0
someoneWin = true
print('turno',turno)

def tira_dado():
    dado = random.randint(1,6)
    print('dado result', dado)
    return dado

while someoneWin:
    for player in range(0, 6, 1):
        dado=tira_dado()
        print('player ', player, 'result actual ',players[player])
        players[player]=players[player]+dado
        print('player ', player, 'suma result ', players[player])
        if(int(players[player]) >= 50):
            someoneWin = false
            break
        else:
            someoneWin = true