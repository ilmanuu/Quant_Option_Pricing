from models.black_scholes import BlackScholes

def delta_call(S, K, T, r, sigma):
    eps = 1e-4
    return (BlackScholes.call_price(S+eps, K, T, r, sigma)-BlackScholes.call_price(S-eps, K, T, r, sigma)) / (2*eps)
