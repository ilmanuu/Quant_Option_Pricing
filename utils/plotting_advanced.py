import numpy as np
import matplotlib.pyplot as plt
from models.black_scholes import BlackScholes

def plot_all(paths, S0, K, T, r):
    
    print('Dentro plot_all') #debug
    
    fig = plt.figure(figsize=(18,5))
    
    ax1 = fig.add_subplot(1,3,1)
    for i in range(min(20, paths.shape[1])):
        ax1.plot(paths[:,i])
    ax1.set_title('Simulated Paths')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Price')
    
    ax2 = fig.add_subplot(1,3,2)
    ax2.hist(paths[-1], bins=50)
    ax2.set_title('Final Distribution')
    
    ax3 = fig.add_subplot(1,3,3,projection='3d')
    
    S_range = np.linspace(80,120,20)
    sigma_range = np.linspace(0.1,0.5,20)
    
    Sg, sg = np.meshgrid(S_range, sigma_range)
    Z = np.zeros_like(Sg)
    
    for i in range(Sg.shape[0]):
        for j in range(Sg.shape[1]):
            Z[i,j] = BlackScholes.call_price(Sg[i,j], K, T, r, sg[i,j])
    
    ax3.plot_surface(Sg, sg, Z)
    
    ax3.set_title('Price Surface')
    ax3.set_xlabel('S')
    ax3.set_ylabel('Volatility')
    ax3.set_zlabel('Price')
    
    plt.tight_layout()
    plt.show()
