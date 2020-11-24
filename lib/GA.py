import random

import numpy as np


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
    """
    population = None

    def __init__(self, p_s: int, b_s: int):
        """
        Parameters
        -----------
        p_s: int
            The size of the Population, in this case, the GA Class will have
            a constant population size
        b_s: int
            The size of the chessboard

        """
        self.p_s = p_s
        self.b_s = b_s
        
    
   
        

    def createPopulation(self) -> None:
        """
        Create a population of p_s boards with b_s size

        """

        self.population = np.random.randint(8, size = (self.p_s, self.b_s))
    
    def getPopulation(self) -> list:
        """
        Getter population
        """
        return self.population

    

