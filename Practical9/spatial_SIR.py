import numpy as np
import matplotlib.pyplot as plt
# 2D spatial SIR model
size = 100
population = np.zeros((size, size), dtype=int)
# Random initial infection
outbreak = np.random.choice(size, 2)
population[outbreak[0], outbreak[1]] = 1
beta = 0.3
gamma = 0.05
time_steps = 100
# Neighbors 8-directional
def get_neighbors(i, j):
    neighbors = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni = i + di
            nj = j + dj
            if 0 <= ni < size and 0 <= nj < size:
                neighbors.append((ni, nj))
    return neighbors
for step in range(time_steps):
    new_infections = []
    # Find infected
    infected_positions = np.argwhere(population == 1)
    # Infect neighbors
    for (i, j) in infected_positions:
        for (ni, nj) in get_neighbors(i, j):
            if population[ni, nj] == 0:
                if np.random.rand() < beta:
                    new_infections.append((ni, nj))
    # Apply new infections
    for (ni, nj) in new_infections:
        population[ni, nj] = 1
    # Recover
    infected_indices = np.argwhere(population == 1)
    for (i, j) in infected_indices:
        if np.random.rand() < gamma:
            population[i, j] = 2
    # Plot every 10 steps
    if step % 10 == 0:
        plt.clf()
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title("Time = " + str(step))
        plt.pause(0.1)
plt.show()