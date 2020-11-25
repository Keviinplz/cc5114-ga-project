import random
import numpy as np

from BoardSet import BoardSet


class GA():
    """
    Define a Genetic Algorithm class to find a word

    Attributes
    -----------

    p_s: int
        Size of the Population
    b_s: int
        Length of an individual word
    population: list
        List of all individual
    mut_chance: float
        mutation chance indicate how likely an individual is to be mutated
    """
    population = None
    ready = False

    def __init__(self, p_s: int, b_s: int, s_f: float, mut = 0.8):
        """
        Parameters
        -----------
        p_s: int
            The size of the Population, in this case, the GA Class will have
            a constant population size
        b_s: int
            The size of the chessboard

        s_f: float
            Selection factor 
        """
        self.p_s = p_s
        self.b_s = b_s
        self.s_f = s_f
        self.mut = mut
        
    
   
        

    def createPopulation(self) -> None:
        """
        Create a population of p_s boards with b_s size

        """
        pop = np.random.randint(8, size = (self.p_s, self.b_s))
        for i in range(self.p_s):
            i_board = BoardSet(pop[i].tolist(), self.b_s)
            self.population.append(i_board)

    
    def getPopulation(self) -> list:
        """
        Getter population
        """
        return self.population

    def sortPopulation(self) -> list:
        """Sort the population in ascending order of

        Returns:
            list: [description]
        """
        fitness_arr = []
        for i in range(self.p_s):
            fitness_arr.append(self.population[i].getFitness())
        
        sort_index = np.argsort(fitness_arr)
        self.population = self.population[sort_index]

    def selectParents(self)->list:
        """Order the population and select a parents such as
            the better fitness function are priorizated 

        Returns:
            list: [description]
        """
        
        self.sortPopulation()
        rand = np.random.uniform(0, 1, 2) # two parents
        random_index = self.p_s * rand**(self.s_f)
        random_index.astype(int)
        parents = self.population[random_index]
        return parents
        
    def reproduce(self, parents:list)->list:
        cross_point = random.randint(1, self.b_s-1)
        firstParent = parents[0]
        secondParent = parents[1]
        firstChild = BoardSet(firstParent.getConfig()[:cross_point].append(secondParent.getConfig()[cross_point:]), self.b_s)
        secondChild = BoardSet(secondParent.getConfig()[:cross_point].append(firstParent.getConfig()[cross_point:]), self.b_s)
        firstChild.mutate(self.mut)
        secondChild.mutate(self.mut)
        children = [firstChild, secondChild]
        return children

    def isReady(self):
        return self.ready
    

