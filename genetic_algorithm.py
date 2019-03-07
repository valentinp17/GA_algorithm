from individual import Individual
from population import Population


def create_primary_population(population_size, max_force):
    population = Population()
    for i in range(population_size):
        indiv = Individual()
        for j in range(100):
            indiv.add_step(indiv.create_random_step(max_force))
        population.add_individual(indiv)
    return population


class GeneticAlgorithm:
    def __init__(self, population_size, elite_size, mutation_rate, max_generations, max_force, circles):
        self.primary_population = create_primary_population(population_size, max_force)
        self.population_size = population_size
        self.current_population = None
        self.elite_size = elite_size
        self.mutation_rate = mutation_rate
        self.max_generations = max_generations
        self.max_force = max_force
        self.current_gen = 0
        self.circles = circles
        self.progress = []

    def next_generation(self):
        children = self.current_population.selection_breed_mutate(self.circles, self.mutation_rate)
        return children

    def start_algorithm(self):
        self.current_population = self.primary_population

        for i in range(self.max_generations):
            self.current_population = self.next_generation()
            self.progress.append(self.current_population.get_ranked(self.circles).population[0])
            #if i % 100 == 0:
            #    print(f'Generation: {i}')

        return self.progress

