# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# In chess, the Elo rating system is used to calculate player strengths based on game results.
#
# A simplified description of the Elo system is as follows. Every player begins at the same score.
# For each subsequent game, the loser transfers some points to the winner, where the amount of points t
# ransferred depends on how unlikely the win is. For example, a 1200-ranked player should gain much more po
# ints for beating a 2000-ranked player than for beating a 1300-ranked player.
import random

def elo(Ra, Rb, K, win): #Ra and Rb denotes the ratings of Players A and B respectively
    E_a = 1/(1 + 10**((Rb-Ra)/400)) #E_a, E_b denote the expected score (or probability) of each one.
    E_b = 1 - E_a

    # Now we update the score depending on Player A wins or lose win = 1 if A wins and 0 otherwise
    Ra += K*(win - E_a)
    Rb += K*(1 - win - E_b)
    #print(f'New ratings for A and B are {round(Ra,3), round(Rb,3)}')
    return Ra, Rb
Ra = 1200
Rb = 1000
K = 30

for i in range(30000):
    d = random.randint(1,10)
    Ra, Rb = elo(Ra, Rb, K, d%2)
print(Ra, Rb)
