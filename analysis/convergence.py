def convergence_test(simulator, K, sims):
    results = []
    for n in sims:
        simulator.n_sim = n
        payoff = simulator.price_call(K)
        price = payoff.mean()
        results.append((n, price))
    return results
