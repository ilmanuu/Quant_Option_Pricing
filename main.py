from models.black_scholes import BlackScholes
from models.monte_carlo import MonteCarloSimulator
from models.variance_reduction import antithetic_paths
from greeks.greeks import delta_call
from analysis.error_analysis import compute_price
from analysis.convergence import convergence_test
from utils.plotting import plot_paths, plot_distribution
from utils.plotting_advanced import plot_all
from data.market_data import get_volatility

import numpy as np

def get_input(prompt, default, cast=float):
    val = input(f'{prompt} [default={default}]: ')
    try:
        return cast(val) if val else default
    except:
        print('Invalid input, using default')
        return default

def get_choice(prompt, default):
    val = input(f'{prompt} [default={default}]: ').lower()
    return val if val else default

print('\n=== QUANT OPTION PRICER ===\n')

option_type = get_choice('Option type (call/put):', 'call')

S0 = get_input('Price:', 100)
K = get_input('Strike:', 100)
T = get_input('Duration (years):', 1)
r = get_input('Risk-free rate:', 0.05)
sigma = get_input('Volatility:', 0.2)

n_sim = int(get_input('N° simulations:', 10000))
steps = int(get_input('N° time steps:', 252))

show_plot = get_choice('Plots? (y/n)', 'y')

#Black-Scholes
if option_type == 'call':
    bs_price = BlackScholes.call_price(S0, K, T, r, sigma)
else:
    call = BlackScholes.call_price(S0, K, T, r, sigma)
    bs_price = call-S0+K*np.exp(-r*T)

#Monte Carlo
mc = MonteCarloSimulator(S0, r, sigma, T, steps, n_sim)
paths = mc.simulate_paths()

S_T = paths[-1]

if option_type == 'call':
    payoff = np.maximum(S_T-K, 0)
else:
    payoff = np.minimum(K-S_T, 0)

mc_price, error = compute_price(payoff, r, T)

#Variance reduction
paths_vr = antithetic_paths(S0, r, sigma, T, 252, 5000)

#Greeks
delta = delta_call(S0, K, T, r, sigma)

#Real volatility
real_vol = get_volatility('AAPL')

print('\n=== RESULTS ===\n')
print(f'Option type: {option_type}')
print(f'Black-Scholes: {bs_price:.4f}')
print(f'Monte Carlo: {mc_price:.4f} +/- {error:.4f}')
print(f'Delta: {delta:.4f}')

#Plots
if show_plot == 'y':
    plot_all(paths, S0, K, T, r)

#Export MATLAB
np.savetxt('matlab/paths.csv', paths, delimiter=',')