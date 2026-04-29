import numpy as np

def compute_price(payoff, r, T):
    discounted = np.exp(-r*T)*payoff
    price = np.mean(discounted)
    error = np.std(discounted)/np.sqrt(len(payoff))
    return price, error
