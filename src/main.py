import time
from src.genetic_logic.genetic_algorithm import GeneticAlgorithm
from src.models.circle import Circle
from src.utils.plot_manager import PlotManager


if __name__ == '__main__':
    settings = {
        'population_size': 1000,
        'elite_size': 200,
        'mutate_rate': 0.1,
        'generations': 2000,
        'max_force': 0.1,
        'circles': [
            Circle(0.5, 0.4, 0.45)
        ]
    }

    plot_manager = PlotManager()
    times_of_execution = []
    for i in [200]:
        start_time = time.time()
        genetic_algo = GeneticAlgorithm(settings['population_size'], settings['elite_size'],
                                        settings['mutate_rate'], i,
                                        settings['max_force'], settings['circles'])
        result = genetic_algo.start_algorithm()
        plot_manager.draw_path_plot(genetic_algo.circles, result[-1].get_path(settings['circles']))
        plot_manager.draw_fitness_plot(settings, result)
        end_time = time.time()
        times_of_execution.append((i, (end_time - start_time) / 60))
        print('Population: ', i, ' Time:', times_of_execution)

