from circle import Circle
from individual import Individual
from population import Population
from vector2d import Vector2D

'''

'''


def create_primary_population(population_size, max_force):
    population = Population()
    for i in range(population_size):
        indiv = Individual()
        for j in range(10):
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
        #self.circles = []
        self.progress = []

    def next_generation(self):
        #ranked_population = self.current_population.get_ranked(self.circles)
        #selection_results = ranked_population.selection(self.elite_size, self.circles)
        #mating_pool = Population.create_mating_pool(selection_results)
        #children = Population.breed_population(mating_pool)
        #children = selection_results.breed_population()
        #hildren.mutate_population(self.mutation_rate, self.max_force)
        children = self.current_population.selection_breed_mutate(self.circles, self.mutation_rate)
        return children

    def start_algorithm(self):
        self.current_population = self.primary_population

        for i in range(self.max_generations):
            self.current_population = self.next_generation()
            self.progress.append(self.current_population.get_ranked(self.circles).population[0])
            if i % 100 == 0:
                print(f'Generation: {i}')
            #print(self.current_population.get_ranked(self.circles).population[:5])

        return self.progress

