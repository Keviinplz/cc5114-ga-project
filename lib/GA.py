import random

import numpy as np


class GA():
    """
    Define a Genetic Algorithm class to find a word

    Attributes
    -----------

    p_s: int
        Size of the Population
    i_l: int
        Length of an individual word
    spanish: bool
        Use the Spanish alphabet
    population: list
        List of all individual
    """
    population = None

    def __init__(self, p_s: int, i_l: int, spanish=False):
        """
        Parameters
        -----------
        p_s: int
            The size of the Population, in this case, the GA Class will have
            a constant population size
        i_l: int
            The Length of an Individual Word, remeber that an individual is
            constant respect to his length, but it can be mutated
        spanish: bool
            Determine if we use the Spanish Alphabet instead of English Alphabet
        """
        self.p_s = p_s
        self.i_l = i_l
        self.spanish = spanish
    
    @staticmethod
    def getAlphabet(spanish=False) -> str:
        """
        Return a string with the alphabet that we gonna use
        
        Parameters
        ----------
        spanish: bool
            If if true, the Alphabet gonna be spanish, by default the alphabet gonna be in english
        """
        spanish_alphabet = "abcdefghijklmnñopqrstuvwxyzáéíóúäëïöü"
        english_alphabet = "abcdefghijklmnopqrstuvwxyz"
        return spanish_alphabet if spanish else english_alphabet
        

    def createPopulation(self) -> None:
        """
        Create a population of p_s individuals with length i_l

        """
        alphabet = self.getAlphabet(spanish=self.spanish)
        tempPopulation = []
        for i in range(self.p_s):
            tempIndividual = []
            for j in range(self.i_l):
                tempIndividual.append(random.choice(alphabet))
            tempPopulation.append(np.array(tempIndividual))
        self.population = np.array(tempPopulation)
    
    def getPopulation(self) -> list:
        """
        Getter population
        """
        return self.population

    

