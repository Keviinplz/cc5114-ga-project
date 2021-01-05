import random


class Binary:
    """
    Define the Binary class 

    Attributes
    -----------

    value: configuration array
    target_number: target number to convert
    genes_number: quantity of bits
    """

    def __init__(self, value: str, target_number: int, genes_number: int):
        self.value = value
        self.target_number =  target_number
        self.genes_number = genes_number

    def getFitness(self):
        """Returns the fitness function of a binary expresion. 
            The fitness value is the decimal diference between the 
            decimal equivalence of the actual value with the target
            number.

        Returns:
            int: fitness value
        """
        result = 0
        exp = 1
        for i in self.value[::-1]:
            result += int(i)*exp 
            exp *=2
        return abs(self.target_number-result)
    
    def geneFactory(self):
        """Generate randomly an 1 or a 0 and returns it as string.

        Returns:
            str: 0 or 1
        """
        if(random.random()>=0.5):
            return "1"
        else:
            return "0"
    
    def getValue(self):
        """Returns the value of the Binary representation

        Returns:
            str: value of the actual binary number
        """
        return self.value
    
    def mutate(self, mutation_prob:float):
        """Mutate the genetic of the individual by changing an aleatory position with a random bit

        Args:
            mutation_prob (float): mutation change derivate from the GA atributes
        """
        random_float= random.random()
        if(random_float<= mutation_prob):
            random_gen = self.geneFactory()
            random_index = random.randint(0, self.genes_number-1)       
            new_value = list(self.value)
            new_value[random_index] = random_gen
            self.value = "".join(new_value)
    
    def intercourse(self, anotherWord):
        """
            Create two new Binary numbers based on the actual Binary and another one.
            Using the crossover methodology.

        Args:
            anotherWord (Binary): another Binary number

        Returns:
            list: list of generated binary numbers as strings
        """
        cross_point = random.randint(1, self.genes_number-1)
        firstChild = Binary(self.getValue()[:cross_point]+ anotherWord.getValue()[cross_point:], self.target_number, self.genes_number)
        secondChild = Binary(anotherWord.getValue()[:cross_point] + self.getValue()[cross_point:], self.target_number, self.genes_number)
        return [firstChild, secondChild]