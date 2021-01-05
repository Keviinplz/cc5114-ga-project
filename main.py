import sys

import numpy as np
import matplotlib.pyplot as plt

from lib.GA import GA

def handleInputs():
    
    if sys.argv[1] != "n-queen" and sys.argv[1] != "random_word" and sys.argv[1] !="to_binary" :
        raise ValueError("""
        You did not give a valid option. Remember you have to choose between: 
                "n-queen", "random_word" or "to_binary".
        """)
    
if __name__ == '__main__':
    handleInputs()
    option = sys.argv[1]

    ## GENERAL PARAMETERS FOR GENETIC ALGORITHM
    pop_size = 60
    selection_factor = 5
    mutation = 0.2

    ##### N-QUEEN PARAMETERS
    board_size =  8

    ##### RANDOM WORD PARAMETERS
    target_word = "kakaroto" 
    
    ### TO BINARY PARAMETERS
    number_to_convert = 724
    number_of_genes =  10
    GEN = []
    for k in range(10):
        if(option == "n-queen"):
            ga = GA(pop_size, "n-queen", selection_factor, mutation)
            ga.createPopulation(b_s = board_size)
        
        if(option == "random_word"):    
            ga = GA(pop_size, "random_word", selection_factor, mutation)
            ga.createPopulation(target_word=target_word)

        if(option == "to_binary"):

            ga = GA(pop_size, "to_binary", selection_factor, mutation)
            ga.createPopulation(target_number=number_to_convert, genes_number=number_of_genes)
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
        c_winner = ga.getPopulation()[0].getValue()
        # printing the board that solves the n-queen problem
        print(c_winner)
        # plotting the results
        generations = len(best_fitness)
        GEN.append(generations)
        print(generations)
        plt.plot(np.arange(generations), best_fitness)
plt.text(0, 0, "Mean generations = "+str(round(np.mean(np.array(GEN)))))
plt.xlabel('Generations')
plt.ylabel('Best fitness value')
plt.title("Generations vs fitness")
plt.show()

