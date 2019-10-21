from Item import Item
import random


class Individual():
    def __init__(self, items, max):
        self.items = items
        self.max = int(max)
        self.length = len(items)
        self.gens = list(map(lambda _:  0 if random.random()
                             > 0.5 else 1, range(self.length)))

    def fitness(self):
        fit = []
        weights = []
        for i in range(self.length):
            gene = self.gens[i]
            value = self.items[i].value
            weight = self.items[i].weight
            fit.append(gene * value)
            weights.append(gene * weight)
        return sum(fit) if sum(weights) <= self.max else 1

    def crossOver(self, parent):
        child = Individual(self.items, self.max)
        child.gens = []
        intHalfLength = int(random.random() * self.length)+1

        firstPart = parent.gens[0:intHalfLength]
        secondPart = self.gens[intHalfLength-1:]

        child.gens = firstPart + secondPart
        return child

    def mutate(self, rate=0.1):
        if(random.random() < rate):
            ramdomIndex = int(random.random() * self.length)
            self.gens[ramdomIndex] = 0 if self.gens[ramdomIndex] == 1 else 1

    def __str__(self):
        return "".join(str(x) for x in self.gens)

    def toItems(self):
        items = []
        for i in range(self.length):
            if self.gens[i] == 1:
                items.append(self.items[i])
        return items
