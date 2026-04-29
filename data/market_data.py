import yfinance as yf
import numpy as np

def get_volatility(ticker='AAPL'):
    data = yf.download(ticker, period="1y")
    
    prices = data['Close'].values.flatten()
    returns = np.log(prices[1:]/prices[:-1])
    
    volatility = np.std(returns)*np.sqrt(252)
    
    return float(volatility)