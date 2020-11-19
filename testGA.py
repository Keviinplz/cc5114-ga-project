from lib.GA import GA

expected_spanish_alphabet = "abcdefghijklmnñopqrstuvwxyzáéíóúäëïöü"
expected_english_alphabet = "abcdefghijklmnopqrstuvwxyz"

p_s = 100
i_l = 3

ga = GA(p_s, i_l, True)

# Testing static method
assert(GA.getAlphabet() == expected_english_alphabet)
assert(GA.getAlphabet(spanish=True) == expected_spanish_alphabet)

# Testing the population creation has the length expected
assert(ga.getPopulation() == None)
ga.createPopulation()
assert(len(ga.getPopulation()) == p_s)
assert(len(ga.getPopulation()[0]) == i_l)

