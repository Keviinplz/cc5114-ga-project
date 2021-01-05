import random
import numpy as np
import string


class Word:
    """
    Define the Word class 

    Attributes
    -----------

    value: configuration array
    target: target word to match
    w_s: word size
    """
    def __init__(self, value: str, target: str, w_s: int):
        self.value = value
        self.w_s = w_s
        self.target = target
    
    def getFitness(self):
        """Returns the fitness function of a word. 
            The fitness value is the quantity of different 
            letters with respect to the target. 

        Returns:
            int: fitness value
        """
        fitness = 0
        for i, l in enumerate(self.value):
            if  l != self.target[i]:
                fitness += 1
        return  fitness
    
    def getValue(self):
        """Returns the value of the word

        Returns:
            str: value of the actual string
        """
        return self.value

    def mutate(self, mutation_prob: float):
        """Mutate the genetic of the individual by changing an aleatory position with a random letter

        Args:
            mutation_prob (float): mutation change derivate from the GA atributes
        """
        random_float= random.random()
        if(random_float<= mutation_prob):
            random_letter = random.choice(string.ascii_lowercase)
            random_index = random.randint(0, self.w_s-1)
            new_word = list(self.value)
            new_word[random_index] = random_letter
            self.value = "".join(new_word)
    
    def intercourse(self, anotherWord):
        """
            Create two new Word based on the actual Word and another one.
            Using the crossover methodology.

        Args:
            anotherWord (Word): another Word

        Returns:
            list: list of generated words
        """
        cross_point = random.randint(1, self.w_s-1)
        firstChild = Word(self.getValue()[:cross_point]+ anotherWord.getValue()[cross_point:], self.target, self.w_s)
        secondChild = Word(anotherWord.getValue()[:cross_point] + self.getValue()[cross_point:], self.target, self.w_s)
        return [firstChild, secondChild]