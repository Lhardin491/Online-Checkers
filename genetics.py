import itertools
import random
import collections

class MovementStrategy:
    def __init__(self):
        self.mapping = collections.OrderedDict() 
        self.score = 0

    def generate(self):
        for checker in itertools.product(range(8), range(8), [True, False]):
            self.mapping[checker] = random.randrange(12)

    def get_move(self, checkers):
        move = sum(map(lambda c: self.mapping[c], checkers)) % 48
        name = move % 12
        vector = move // 12
        return (name, vector)

    def breed(self, other):
        crosspoint = random.randrange(len(self.mapping))
        new_strat = MovementStrategy()
        for tie in zip(self.mapping.items(), other.mapping.items(), range(len(self.mapping))):
            if tie[2] < crosspoint:
                inherited = tie[0]
            else:
                inherited = tie[1]
            new_strat.mapping[inherited[0]] = inherited[1]
        return new_strat

    def mutate(self, mutation_chance):
        for value in self.mapping.values():
            if random.random() < mutation_chance:
                value += 1


if __name__ == '__main__':
    ms1 = MovementStrategy()
    ms1.generate()
    ms2 = MovementStrategy()
    ms2.generate()
    print(ms1.breed(ms2).mapping)
    

