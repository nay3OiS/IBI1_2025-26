import numpy as np
import matplotlib.pyplot as plt
N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000
# Try vaccination rates from 0% to 100%
vacc_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
results = []
for v in vacc_rates:
    S = int((1 - v) * N) - 1
    I = 1
    R = 0
    V = int(v * N)
    S_list = [S]
    I_list = [I]
    for t in range(time_steps):
        infection_prob = beta * (I / N)
        new_infected = np.random.choice([0,1], size=S, p=[1-infection_prob, infection_prob]).sum()
        new_recovered = np.random.choice([0,1], size=I, p=[1-gamma, gamma]).sum()
        S -= new_infected
        I = I + new_infected - new_recovered
        R += new_recovered
        I_list.append(I)
    results.append(I_list)
# Plot all infected curves
plt.figure(figsize=(6,4), dpi=150)
for i, v in enumerate(vacc_rates):
    plt.plot(results[i], label=f'{int(v*100)}%')
plt.xlabel('Time')
plt.ylabel('Infected')
plt.title('SIR with Vaccination')
plt.legend(title='Vaccination rate')
plt.savefig('SIR_vaccination.png')
plt.show()