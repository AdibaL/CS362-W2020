# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 20:35 2020

@author: baligaa
"""

import Dominion
import random
from collections import defaultdict

#Get player names
player_names = testUtility.get_player_names()

nV = testUtility.get_numberVCards(len(player_names))

# nC = testUtility.get_numberCCards(len(player_names))
# Test Bug #2: number of curse cards changed to +10 + 10 * len(player_names)
nC = 10 + 10 * len(player_names)


box = testUtility.getBoxes(nV)

supply_order = testUtility.getSupply_Order()

#Pick 10 cards from box to be in the supply.
boxSupply = testUtility.get_boxSupply(box)

#The supply always has these cards
supply = testUtility.getSupply(player_names, nV, nC)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.getPlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)