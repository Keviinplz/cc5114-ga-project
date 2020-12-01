import numpy as np
import matplotlib.pyplot as plt

from lib.GA import GA

if __name__ == '__main__':
    board_size =  8
    pop_size = 100
    selection_factor = 5
    ga = GA(pop_size, board_size, selection_factor)
    ga.createPopulation()

    while not ga.isReady():
        next_generation = []
        for i in range(int(pop_size/2)):
            parents = ga.selectParents()
            children = ga.reproduce(parents)
            next_generation.append(children[0])
            next_generation.append(children[1])       
        ga.setPopulation(next_generation)

c_winner = ga.getPopulation()[0].getConfig()
print(c_winner)
