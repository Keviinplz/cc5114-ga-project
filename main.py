import sys

import numpy as np
import matplotlib.pyplot as plt

from lib.GA import GA

def handleInputs():
    if len(sys.argv) != 5:
        raise ValueError("""
        Bad parameters, usage:
        python3 main.py <board_size> <population> <selection_factor> <mutation>
        """)
    if int(sys.argv[1]) % 2 != 0:
        raise ValueError("""
        Board Size has to be even.
        """)

    mutation = float(sys.argv[4])
    if not (0 <= mutation and mutation <= 1):
        raise ValueError("""
        Mutation is a probability parameter, must to be between [0, 1]
        """)

if __name__ == '__main__':
    handleInputs()
    board_size = int(sys.argv[1])
    pop_size = int(sys.argv[2])
    selection_factor = int(sys.argv[3])
    mutation = float(sys.argv[4])
    ga = GA(pop_size, board_size, selection_factor, mutation)
    ga.createPopulation()
    best_fitness = []
    while not ga.isReady():
        next_generation = []
        for i in range(int(pop_size/2)):
            parents = ga.selectParents()
            children = ga.reproduce(parents)
            next_generation.append(children[0])
            next_generation.append(children[1])       
        ga.setPopulation(next_generation)
        ga.sortPopulation()
        best_fitness.append(ga.getPopulation()[0].getFitness())
c_winner = ga.getPopulation()[0].getConfig()
# printing the board that solves the n-queen problem
print(c_winner)
# plotting the results
generations = len(best_fitness)
print(generations)
plt.plot(np.arange(generations), best_fitness)
plt.xlabel('Generations')
plt.ylabel('Best fitness value')
plt.title("Generations vs fitness")
plt.show()

