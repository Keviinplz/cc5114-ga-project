import numpy as np
import matplotlib.pyplot as plt

from lib.GA import GA

if __name__ == '__main__':
    board_size =  8
    pop_size = 60
    selection_factor = 5
    ga = GA(pop_size, board_size, selection_factor)
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

