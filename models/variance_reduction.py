import numpy as np

def antithetic_paths(S0, r, sigma, T, steps, n_sim):
    dt = T/steps
    
    Z = np.random.standard_normal((steps, n_sim))
    Z2 = -Z
    
    def simulate(Z):
        paths = np.zeros((steps+1, n_sim))
        paths[0] = S0
        
        for t in range(1, steps+1):
            paths[t] = paths[t-1]*np.exp(
                (r-0.5*sigma**2)*dt+sigma*np.sqrt(dt)*Z[t-1]
            )
        return paths
    
    return (simulate(Z)+simulate(Z2))/2
