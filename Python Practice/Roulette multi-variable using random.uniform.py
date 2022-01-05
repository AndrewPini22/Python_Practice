import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import random


lower_broke = 33.5
higher_profit = 61.7

samplesize = 1000
starting_funds = 10000
wager_size = 100
wager_count = 100

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
    
def multiple_bettor(funds, initial_wager, wager_count):
    global multiple_broke
    global multiple_profits
        
    value = funds
    wager = initial_wager       

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
                    #print ("Multiple broke afer",current_wager, "bets")
                    multiple_broke += 1
                    break
                    
        elif previousBet == "loss":
            if SpinWheel():
                wager = previous_bet_amount * random_multiple
                if (value - wager) < 0:
                    wager = value
               
                value += wager
                #print (value)
                wager = initial_wager
                previousBet = "win"
                wX.append(current_wager)
                vY.append(value)
            
            else:
                wager = previous_bet_amount * random_multiple
                 
                value -= wager
                if value <= 0:
                    #print ("Multiple broke afer",current_wager, "bets")
                    multiple_broke += 1
                    break   
            
                #print (value)
                previousBet = "loss"
                previous_bet_amount = wager
                wX.append(current_wager)
                vY.append(value)
            
        current_wager += 1
        
        #print (value)
    #plt.plot(wX, vY, 'r')
    if value > funds:
        multiple_profits += 1

def loss_double (funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    global double_broke
    global double_profits
    
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
                    #print ("Double broke afer",current_wager, "bets")
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
                    #print ("Double broke afer",current_wager, "bets")
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
        
 #Simple Bettor

def simple_bettor (funds, initial_wager, wager_count):
    global simple_broke
    global simple_profits
    
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
        print ("Simple broke afer",current_wager, "bets")
        value = 0
        simple_broke += 1
        
    #print ("Funds:" , value)

    #plt.plot (wX,vY, 'k')
    if value > funds:
        simple_profits += 1


while True:
    multiple_broke = 0.0
    multiple_profits = 0.0

    multiple_sample_size = 100000
    current_sample = 1
    random_multiple = random.uniform(0.1,10.0)
    
    while current_sample <= multiple_sample_size:
        multiple_bettor(starting_funds,wager_size,wager_count)
        current_sample += 1
    
    if (((multiple_broke/multiple_sample_size)*100.00) < lower_broke) and (((multiple_profits/multiple_sample_size)*100.00) > higher_profit):
       print ("***")    
       print ("Found Winning Strategy:",random_multiple)
       print ("Lower Bust to beat: ",lower_broke)
       print ("Higher profit rate to beat: ",higher_profit)
       print ("Bust rate: ",(multiple_broke/multiple_sample_size)*100.00)
       print ("Profit Rate: ",(multiple_profits/multiple_sample_size)*100.00)
       print ("***")  
    

    
#print ("Simple Bettor broke chances:",(simple_broke/samplesize)*100)
#print ("doubler broke chances:",(double_broke/samplesize)*100)
#print ("Multiple Broke Chances:",(multiple_broke/samplesie)*100)
#print ("Simple Bettor profits chance:",(simple_profits/samplesize)*100)
#print ("Double Bettor profits chance:",(double_profits/samplesize)*100)
#print ("Multiple Bettor profits chance:",(multiple_profits/samplesize)*100)

#plt.axhline (0,color = "g")
#plt.ylabel("Account Value")
#plt.xlabel("Wager Count")
#plt.show()


