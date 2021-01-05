import random
import collections
import numpy as np

class BoardSet:
    """
    Define the board set that contains the queen's position

    Attributes
    -----------

    conf: configuration array
    b_s: board size
    """
    def __init__(self, conf: list, b_s: int):
        self.conf = conf
        self.b_s = b_s
    
    def getFitness(self)->int:
        """Returns the fitness function of a chessboard
            using a collector diccionary take the frequency
            of the numbers in the configuration array and after 
            that, the function calculate if there is some a 
            diagonal menace

        Returns:
           fitness: an int that tells how many attacks are in the board
        """
        
        fitness = 0
        collection = collections.Counter(self.conf)
        for key in collection:
            fitness += collection[key]-1
        
        for i in range(self.b_s):
            for j in range(i+1, self.b_s):
                diff_index=j-i
                diff_pos=abs(self.conf[j]-self.conf[i])
                if diff_index==diff_pos: fitness+=1
        return fitness             
        
    def getValue(self)->list:
        """ Returns array of queens position

        Returns:
            list: config array
        """

        return self.conf

    def mutate(self, mutation_prob: float):
        """Mutate the genetic of the individual by changing an aleatory position with a random number

        Args:
            mutation_prob (float): mutation change derivate from the GA atributes
        """
        random_float= random.random()
        if(random_float<= mutation_prob):
            random_index= random.randint(0, self.b_s-1)
            random_position = random.randint(0, self.b_s-1)
            self.conf[random_index] = random_position
     
    def intercourse(self, anotherBoard):
        """
        Create two new boards based on the actual board and another one.
            Using the crossover methodology.

        Args:
            anotherBoard (BoardSet): other board set
            

        Returns:
            list: a list that contains the two children after doing cross over
        """
        cross_point = random.randint(1, self.b_s-1) #cross over point
        firstChild = BoardSet(self.getValue()[:cross_point] + anotherBoard.getValue()[cross_point:], self.b_s)
        secondChild = BoardSet(anotherBoard.getValue()[:cross_point] + self.getValue()[cross_point:], self.b_s)

        return [firstChild, secondChild]
         