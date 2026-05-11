# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# Initial parameters
N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000
S = N - 1
I = 1
R = 0
# Lists to store history
S_list = [S]
I_list = [I]
R_list = [R]
for t in range(time_steps):
    # Infection probability depends on infected proportion
    infection_prob = beta * (I / N)
    # New infections
    new_infected = np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob]).sum()
    # New recoveries
    new_recovered = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma]).sum()
    # Update
    S = S - new_infected
    I = I + new_infected - new_recovered
    R = R + new_recovered
    # Save
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)
# Plot
plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of individuals')
plt.title('SIR Model')
plt.legend()
plt.savefig('SIR.png')
plt.show()