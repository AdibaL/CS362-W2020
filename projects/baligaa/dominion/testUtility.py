# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:17 2020

@author: baligaa
"""

import Dominion
import random
from collections import defaultdict

#Get player names
def get_player_names():
    player_names = ["Annie","*Ben","*Carla"]
    return player_names

#number of curses and victory cards

def get_numberVCards(player_names):
    if len(player_names)>2:
        nV=12
    else:
        nV=8
    return nV

def get_numberCCards(player_names):
    nC = -10 + 10 * len(player_names)
    return nC

#Define box
def getBoxes(nV):
    box = {}
    box["Woodcutter"]=[Dominion.Woodcutter()]*10
    box["Smithy"]=[Dominion.Smithy()]*10
    box["Laboratory"]=[Dominion.Laboratory()]*10
    box["Village"]=[Dominion.Village()]*10
    box["Festival"]=[Dominion.Festival()]*10
    box["Market"]=[Dominion.Market()]*10
    box["Chancellor"]=[Dominion.Chancellor()]*10
    box["Workshop"]=[Dominion.Workshop()]*10
    box["Moneylender"]=[Dominion.Moneylender()]*10
    box["Chapel"]=[Dominion.Chapel()]*10
    box["Cellar"]=[Dominion.Cellar()]*10
    box["Remodel"]=[Dominion.Remodel()]*10
    box["Adventurer"]=[Dominion.Adventurer()]*10
    box["Feast"]=[Dominion.Feast()]*10
    box["Mine"]=[Dominion.Mine()]*10
    box["Library"]=[Dominion.Library()]*10
    box["Gardens"]=[Dominion.Gardens()]*nV
    box["Moat"]=[Dominion.Moat()]*10
    box["Council Room"]=[Dominion.Council_Room()]*10
    box["Witch"]=[Dominion.Witch()]*10
    box["Bureaucrat"]=[Dominion.Bureaucrat()]*10
    box["Militia"]=[Dominion.Militia()]*10
    box["Spy"]=[Dominion.Spy()]*10
    box["Thief"]=[Dominion.Thief()]*10
    box["Throne Room"]=[Dominion.Throne_Room()]*10
    return box

def getSupply_order():
    supply_order = {0:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
                    3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                    4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                    5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                    6:['Gold','Adventurer'],8:['Province']}
    return supply_order

#Pick 10 cards from box to be in the supply.
def get_boxSupply(box):
    boxlist = [k for k in box]
    random.shuffle(boxlist)
    random10 = boxlist[:10]
    supply = defaultdict(list,[(k,box[k]) for k in random10])
    return boxSupply

#The supply always has these cards
def getSupply(player_names, nV, nC):
    supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
    supply["Silver"]=[Dominion.Silver()]*40
    supply["Gold"]=[Dominion.Gold()]*30
    supply["Estate"]=[Dominion.Estate()]*nV
    supply["Duchy"]=[Dominion.Duchy()]*nV
    supply["Province"]=[Dominion.Province()]*nV
    supply["Curse"]=[Dominion.Curse()]*nC
    return supply

#initialize the trash
trash = []

#Costruct the Player objects
def getPlayers(player_names):
    players = []
    for name in player_names:
        if name[0]=="*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0]=="^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))
    return players
 