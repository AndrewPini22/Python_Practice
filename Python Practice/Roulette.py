import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import random


def SpinWheel():
    spin = random.randint(1,37)
    if spin == 37:
        #print (spin, ("House Wins"))
        return False
    elif spin <= 18:
        #print (spin, ("Red you Lose"))
        return False
    elif 37 > spin > 18:
        #print (spin, ("Black you win"))
        return True
    
def loss_double (funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    
    wX = []  #w ="wager"
    vY = []  #v ="value"
    
    current_wager = 1  
    
    previousBet = "win"
    previous_bet_amount = initial_wager
    
    while current_wager <= wager_count:
        if previousBet == "win":
            if SpinWheel():
                value += wager
                #print (value)
                wX.append(current_wager)
                vY.append(value)
            else:
                value -= wager
                previousBet = "loss"
                previous_bet_amount = wager
                wX.append(current_wager)
                vY.append(value)
                if value < 0:
                    #print ("Double broke afer",current_wager, "bets")
                    
                    break
                    
        elif previousBet == "loss":
            if SpinWheel():
                wager = previous_bet_amount *2
                if (value - wager) < 0:
                    wager = value
               
                value += wager
                #print (value)
                wager = initial_wager
                previousBet = "win"
                wX.append(current_wager)
                vY.append(value)
            
            else:
                wager = previous_bet_amount *2
                 
                value -= wager
                if value <= 0:
                    #print ("Double broke afer",current_wager, "bets")
                   break   
                #print (value)
                previousBet = "loss"
                previous_bet_amount = wager
                wX.append(current_wager)
                vY.append(value)
            
        current_wager += 1
        
    plt.plot(wX, vY, 'c')
    
xx = 0

while xx < 1000:
    loss_double(10000,100,1000)
    xx += 1

plt.axhline (0,color = "r")
plt.ylabel("Account Value")
plt.xlabel("Wager Count")
plt.show()
        
 #Simple Bettor

def simple_bettor (funds, initial_wager, wager_count):
   
    value = funds
    wager = initial_wager
    
    wX = []
    vY = []
    
    current_wager = 1

    while current_wager <= wager_count:
        if SpinWheel():
            value += wager
            wX.append(current_wager)
            vY.append(value)
        else:
            value -= wager
            wX.append(current_wager)
            vY.append(value)

        current_wager += 1

    if value <= 0:
        #print ("Simple broke afer",current_wager, "bets")
        value = 0
        
    #print ("Funds:" , value)

       
    plt.plot (wX, vY, 'k')
        
x = 0
simple_broke = 0

while x < 1000:
    simple_bettor(10000,100,1000)
    x += 1

plt.axhline (0,color = "r")
plt.ylabel("Account Value")
plt.xlabel("Wager Count")
plt.show()


