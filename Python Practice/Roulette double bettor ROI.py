import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import random

samplesize = 1000
starting_funds = 10000
wager_size = 100
wager_count = 10000

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
    global double_broke
    global double_profits
    global double_ret
    
    wX = []
    vY = []
    
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
                    print ("Double broke afer",current_wager, "bets")
                    double_broke += 1
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
                    print ("Double broke afer",current_wager, "bets")
                    double_broke += 1
                    break   
            
                #print (value)
                previousBet = "loss"
                previous_bet_amount = wager
                wX.append(current_wager)
                vY.append(value)
            
        current_wager += 1
        
        #print (value)
    #plt.plot(wX, vY, 'c')
    if value > funds:
        double_profits += 1
        
    print (value)
    double_ret += 1
    
 
counter_d = 0


double_samplesize = 1000
starting_funds = 10000

wager_size = 100
wager_count = 10000
    


double_broke = 0.0
double_profits = 0.0
double_ret = 0.0



while counter_d < double_samplesize:
        loss_double(starting_funds,wager_size,wager_count)
        counter_d += 1
    

print ("Total Return double:",double_ret)
print ("ROI", double_ret-(double_samplesize*starting_funds))