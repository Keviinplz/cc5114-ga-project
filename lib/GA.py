import random
import numpy as np
import string

from .Binary import Binary
from .Word import Word
from .BoardSet import BoardSet


class GA:
    """
    Define a Genetic Algorithm class to find a word

    Attributes
    -----------

    p_s: int
        Size of the Population
    problem: string
        Problem to solve
    population: list
        List of all individual
    mut_chance: float
        mutation chance indicate how likely an individual is to be mutated, 0.8 bu default
    """
    population = []
    ready = False

    def __init__(self, p_s: int, problem: str, s_f: float, mut = 0.8):
        """
        Parameters
        -----------
        p_s: int
            The size of the Population, in this case, the GA Class will have
            a constant population size
        problem: int
            The problem to solve
        s_f: float
            Selection factor
        mut: float 
            Mutation chance 
        """
        self.p_s = p_s
        self.problem = problem
        self.s_f = s_f
        self.mut = mut
        
    
    def createPopulation(self, b_s: int=0, target_word: str = "", target_number: int =0, genes_number: int = 0) -> None:
        """
        Create a population of p_s boards with b_s size

        """
        if (self.problem == "n-queen"):
            pop = np.random.randint(b_s, size = (self.p_s, b_s))
            for i in range(self.p_s):
                i_board = BoardSet(pop[i].tolist(), b_s)
                self.population.append(i_board)
        
        if (self.problem == "random_word"):
            pop = []
            for i in range(self.p_s):
                i_word = ""
                for j in range(len(target_word)):
                    i_word += random.choice(string.ascii_lowercase)
                i_word = Word(i_word, target_word, len(target_word))
                self.population.append(i_word)
        
        if (self.problem == "to_binary"):
            pop = []
            for i in range(self.p_s):
                i_binary = ""
                for j in range(genes_number):
                    i_binary += str(random.randint(0, 1)) 
                i_binary = Binary(i_binary, target_number, genes_number)
                self.population.append(i_binary)
    
    def getPopulation(self) -> list:
        """
        Getter population
        """
        return self.population

    def setPopulation(self, population: list):
        """Set the population of the GA

        Args:
            population (list): [description]
        """
        self.population = population
        
    def sortPopulation(self):
        """Sort the population in ascending order of fitness function


        """
        fitness_arr = []
        for i in range(self.p_s):
            fitness_arr.append(self.population[i].getFitness())
        
        sort_index = np.argsort(fitness_arr)
        np_population = np.array(self.population)
        self.population = np_population[sort_index].tolist()

    def selectParents(self)->list:
        """Order the population and select two parents such as
            the better fitness function are priorizated 

        Returns:
            parents: list of parents
        """
        self.sortPopulation()
        rand = np.random.uniform(0, 1, 2) # two parents
        random_index = (self.p_s * rand**(self.s_f)).astype(int) # function to priorizate small values

        np_population = np.array(self.population)
        parents = np_population[random_index].tolist()
        return parents
        
    def reproduce(self, parents:list)->list:
        """ Taking two given parents generate two children
            using the cross over process and the mutation of
            genes

        Args:
            parents: list of parents, every parent is an instance of BoardSet

        Returns:
            children: list of children 
        """
        firstParent = parents[0]
        secondParent = parents[1]
        children = firstParent.intercourse(secondParent)
        firstChild = children[0]
        secondChild = children[1]        
        firstChild.mutate(self.mut)
        secondChild.mutate(self.mut)
        children = [firstChild, secondChild]
        return children

    def isReady(self):
        """Tells if the solution was reached

        Returns:
            boolean: true if the solution was reached 
        """
        self.sortPopulation()
        if self.population[0].getFitness() ==0:
            self.ready = True
        return self.ready
    

