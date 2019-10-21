import random
from Item import Item
from Individual import Individual


class Algorithm():

    population = []
    populationSize = 50
    maxNumberOfGeneration = 500

    def __init__(self, items, size):
        self.items = items
        self.size = size
        self.length = len(items)
        self.generateIntialPopulation()

    def generateIntialPopulation(self):
        self.population = list(
            map(lambda _: Individual(self.items, self.size),
                range(self.populationSize))
        )
        self.bestEver = self.population[0]

    def fitness(self):
        return list(map(lambda i: i.fitness(), self.population))

    def selection(self):
        fitness = self.fitness()
        sumFitness = sum(fitness)
        rand = random.random() * sumFitness
        # print(sumFitness, rand)

        partialSum = 0
        for i in range(self.populationSize):
            partialSum += fitness[i]
            if partialSum >= rand:
                return self.population[i]

    def next(self):
        nextGeneration = []
        for i in range(self.populationSize):
            parentOne = self.selection()
            parentTwo = self.selection()

            child = parentOne.crossOver(parentTwo)
            child.mutate()
            nextGeneration.append(child)

        self.population = nextGeneration

    def evolve(self):
        for i in range(self.maxNumberOfGeneration):
            self.next()
            self.setBest()

        # print(self.bestEver.fitness())
        # print(len(self.bestEver.toItems()))
        # for i in self.bestEver.toItems():
        #     print(i.weight, i.value)

    def setBest(self):
        bestFit = self.bestEver.fitness()
        for i in self.population:
            if(bestFit < i.fitness()):
                self.bestEver = i
                bestFit = i.fitness()
        return self.bestEver

    def __str__(self):
        return str(",".join(str(x) for x in self.population))


# al = Algorithm([Item(4, 4), Item(7, 6), Item(5, 3)], 7)
# al.evolve()
# print(al.bestEver.fitness())
