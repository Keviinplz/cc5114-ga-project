import numpy as np
import matplotlib.pyplot as plt

from GA import GA

if __name__ == '__main__':
    board_size =  8
    pop_size = 100
    selection_factor = 5
    GAlg = GA(pop_size, board_size, selection_factor)
    GAlg.createPopulation()

    while not GAlg.isReady():
        next_generation = []
        for i in range(int(pop_size/2)):
            parents = GAlg.selectParents()
            children = GAlg.reproduce(parents)
            next_generation.append(children[0])
            next_generation.append(children[1])       
        GAlg.setPopulation(next_generation)

c_winner = GAlg.getPopulation()[0].getConfig()
print(c_winner)
