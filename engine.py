import random

#The Kelly Formula - function that takes p, b, and returns the optimal f*
#p = probablity of wining, b = decimal odds that is always equal to 1, f = output (kelly percentage - the fraction of the portfolio bet)
def kellyFormula(p, b):
    q = 1 - p
    f = (b*p - q) / b
    return f



#Simulation Class - create a class the holds the state of a Trader (current bankroll/supply, history, betting strategy)

class Simulator:
    #ctor to set up initial state
    def __init__(self, p, b, initial_wealth=10000):
        #invariants:
        self.p = p
        self.b = b
        self.initial_wealth = initial_wealth
        #initialise the state variables
        self.current_wealth = initial_wealth
        self.history = []

    def reset(self):
        self.current_wealth = self.initial_wealth
        self.history = [self.initial_wealth]

    def run_sim(self, frac, trials):
        #arguments: fraction of wealth to bet, number of times to bet
        #float frac, int trials 

        # 1. generate a random outcome
        self.reset()

        for _ in range(trials):
            bet_size = frac * self.current_wealth
            #generate random outcome
            is_win = random.random() < self.p #if outcome is smaller than the probability of winning return true. random.random() returns a float between 0 and 1.0

            if is_win:
                self.current_wealth += self.b * bet_size
            else:
                self.current_wealth -= bet_size #you lose what you bet

            #record the new history 
            self.history.append(self.current_wealth)

            # Safety Check: Stop if broke (Ruin)
            if self.current_wealth <= 0.01: # Use a small epsilon, not exactly 0
                self.current_wealth = 0
                # Fill the rest of the history with 0s so graphs look correct
                remaining_steps = trials - len(self.history) + 1 # +1 for initial
                self.history.extend([0] * remaining_steps)
                break
        
        return self.history[:]

