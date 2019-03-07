import random

from src.genetic_logic.individual import Individual


class Population:
    def __init__(self):
        self.population = []
        self.max_size = 100
        self.size = 0

    def add_individual(self, individual):
        self.population.append(individual)
        self.size += 1

    def add_individuals(self, individs):
        for individ in individs:
            self.add_individual(individ)

    def get_ranked(self, circles):
        ranked_population = Population()
        sorted_individs = sorted(self.population, key=lambda x: x.get_fitness(circles), reverse=True)
        ranked_population.add_individuals(sorted_individs)
        return ranked_population

    def selection(self, elite_size, circles):
        selected_population = Population()
        selected_population.add_individuals(self.get_ranked(circles).population[:elite_size])
        return selected_population

    def selection_breed_mutate(self, circles, mutate_rate):
        ranked_population = self.get_ranked(circles).population
        elite_size = int(self.max_size * 0.2)
        best_popul = ranked_population[:elite_size]
        changing_popul = []
        for i in range(4):
            changing_popul.extend(best_popul[:])
        new_popul = Population()
        new_popul.add_individuals(best_popul)
        new_popul.add_individuals(changing_popul)
        children = new_popul.breed_population()
        children.mutate_population(mutate_rate, 1)


        return children

    def selection_breed_mutate2(self, circles, mutate_rate):
        ranked_population = self.get_ranked(circles).population
        sum_fitness = 0
        for indiv in ranked_population:
            sum_fitness += indiv.get_fitness(circles)
        probabilities = [0 + (ranked_population[0].fitness / sum_fitness)]
        for i in range(1, len(ranked_population)):
            probabilities.append(probabilities[i - 1] + ((ranked_population[i].fitness / sum_fitness)))
        selection_size = len(ranked_population) // 2
        selected_population = []
        for i in range(selection_size):
            rand = random.random()
            for j in range(len(probabilities)):
                if rand < probabilities[j]:
                    selected_population.append(ranked_population[j])
                    break
        children = Population()
        mutate_popul = selected_population[:]
        children.add_individuals(mutate_popul)
        children = children.breed_population()
        children.mutate_population(mutate_rate, 1)
        new_population = Population()
        new_population.add_individuals(selected_population)
        new_population.add_individuals(children.population)
        return new_population

    def mutate_population(self, mutate_rate, max_force):
        for individual in self.population:
            if random.random() < mutate_rate:
                mutate_type = random.randint(0, 2)
                if mutate_type == 0:
                    individual.mutate_change_step(max_force)
                elif mutate_type == 1:
                    individual.mutate_add_step(max_force)
                elif mutate_type == 2:
                    individual.mutate_delete_step()

    def breed_population(self):
        new_population = Population()
        for i in range(self.size):
            parent1, parent2 = random.choice(self.population), random.choice(self.population)
            new_individual = Individual.breed(parent1, parent2)
            new_population.add_individual(new_individual)
        return new_population



