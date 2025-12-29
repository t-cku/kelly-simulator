#Set the variables - how many trades, % win rate
#Loop: a script that creates different traders (full kelly, half kelly, fixed bet), and runs them through the same simulation
#Output and reporting the final results - print to terminal / frontend / file input

#Step Logic - a method that simulates a single coin flip and updates the bankroll
import matplotlib.pyplot as plt
from engine import Simulator, kellyFormula
import numpy as np


#1 define the "market" - win prob (p), odds (b), starting cash, duration
win_prob = 0.55 #slightly above 0.5 so theres an "edge"
odds = 1.0
starting_cash = 10000
duration = 100 #how many bets
n_sims = 100 #number of simulations for monte carlo

#2 calculate the benchmark f* - ie the perfect bet size. call the kelly formula fn and store the reuslt in a variable
#self check - print this value. 

optimal_f = kellyFormula(win_prob, odds)
print("Optimal f: ", optimal_f)

#3 run the scenarios
#instantiate the simulator class once, call the run_sim three times for full kelly, fractional/half kelley and overbetting
#for storage
all_fullKelly =[]
all_halfKelly = []
all_overbet =[]

#instantiate: Variable_Name = Class_Name(arguments...)
simulation = Simulator(win_prob, odds, starting_cash)


for i in range(n_sims):
    fullKelly = simulation.run_sim(frac=optimal_f, trials = 100)[:]
    all_fullKelly.append(fullKelly)
    halfKelly = simulation.run_sim(frac=optimal_f * 0.5, trials = 100)[:]
    all_halfKelly.append(halfKelly)
    overBetting = simulation.run_sim(frac=optimal_f * 2.0, trials = 100)[:]
    all_overbet.append(overBetting)

avg_full = np.mean(all_fullKelly, axis=0)
avg_half = np.mean(all_halfKelly, axis=0)
avg_overbet = np.mean(all_overbet, axis=0)
#4 visualisation using matplotlib.pyplot

#create a figure plt.figure(figsize =...)
plt.figure(figsize=(10,6))
#plot lines plt.plot() for each simulation - give them diff colours and add label 
plt.plot(avg_full, label="Full Kelly", color="green")
plt.plot(avg_half, label="Half Kelly", color="blue")
plt.plot(avg_overbet, label="Over Betting", color="red")
plt.title("Kelly Criterion Simulation - Monte Carlo Analysis: 100 Runs")
plt.xlabel("Number of Bets")
plt.ylabel("Account Balance($)")

plt.legend()

#plt.show()
plt.show()





