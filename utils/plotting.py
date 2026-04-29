import matplotlib.pyplot as plt

def plot_paths(paths):
    plt.figure()
    for i in range(20):
        plt.plot(paths[:,i])
    plt.title('Simulated Paths')
    plt.show()
    
def plot_distribution(S_T):
    plt.figure()
    plt.hist(S_T, bins=50)
    plt.title('Final Distribution')
    plt.show()
