Quant Option Pricing Project
Overview
This project implements option pricing using:
- Black-Scholes analytical model
- Monte Carlo simulation
- Variance reduction techniques
- Greeks computation

Features
- European call and put options
- Stochastic simulation of asset paths
- Real market volatility estimation
- Advanced visualization (paths, distributions, 3D surface)

Models
Black-Scholes
Closed-form solution for European options.

Monte Carlo
Simulation of stochastic differential equation:
ds = rSdt + σSdW

Results
- Comparison between analytical and numerical pricing
- Convergence analysis
- Sensitivity (Delta)

Tech Stack
- Python
- NumPy
- SciPy
- Matplotlib
- yfinance

How to run
Bash
{pip install -r requirements.txt}
{python main.py}

Author 
Emanuele Venetucci

## Example Output
<img width="1800" height="500" alt="plots" src="https://github.com/user-attachments/assets/909ace95-d6f6-4c98-8534-b0e5264263c5" />

