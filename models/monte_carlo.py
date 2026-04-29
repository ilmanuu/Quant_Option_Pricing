import numpy as np

class MonteCarloSimulator:
    def __init__(self, S0, r, sigma, T, steps, n_sim):
        self.S0 = S0
        self.r = r
        self.sigma = sigma
        self.T = T
        self.steps = steps
        self.n_sim = n_sim
        
        self.dt = T/steps
        
    def simulate_paths(self):
        Z = np.random.standard_normal((self.steps, self.n_sim))
        
        paths = np.zeros((self.steps+1, self.n_sim))
        paths[0] = self.S0
        
        for t in range(1, self.steps+1):
            paths[t] = paths[t-1]*np.exp(
                (self.r-0.5*self.sigma**2)*self.dt+self.sigma*np.sqrt(self.dt)*Z[t-1]
                )
        
        return paths
    
    def price_call(self, K):
        paths = self.simulate_paths()
        S_T = paths[-1]
        payoff = np.maximum(S_T-K, 0)
        return payoff