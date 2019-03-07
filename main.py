import time
from genetic_algorithm import GeneticAlgorithm
from circle import Circle
from plot_manager import PlotManager


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

    with open('info/times_of-execution.txt', 'a') as file:
        print(times_of_execution, file=file)



    '''
    Circle(0.5, 0.5, 0.1), Circle(0.7, 0.7, 0.1), Circle(0.3, 0.7, 0.1),
            Circle(0.3, 0.3, 0.1), Circle(0.7, 0.3, 0.1),
            
    Circle(0.5, 0.5, 0.2), Circle(0.7, 0.3, 0.2), Circle(0.3, 0.7, 0.2)
    
    Circle(0.5, 0.5, 0.1), Circle(0.7, 0.7, 0.15), Circle(0.3, 0.7, 0.15),
            Circle(0.3, 0.3, 0.15), Circle(0.7, 0.3, 0.15),
    
    Circle(0.5, 0.5, 0.2), Circle(0.7, 0.3, 0.2), Circle(0.3, 0.7, 0.2),
    
    gigant
    Circle(0.5, 0.4, 0.45)
    
    
    harder
    Circle(0.9686732292175293, 0.5127896666526794, 0.22724536061286926), 
    Circle(0.5128470063209534, 0.5292640328407288, 0.20050999522209167),
    Circle(0.012142913416028023, 0.752185046672821, 0.3144221603870392),
    Circle(0.2146744728088379, 0.06266354769468307, 0.15026962995529175),
    Circle(0.709238588809967, 0.1207527220249176, 0.20471514761447906),
    Circle(0.5442208647727966, 0.9810458421707153, 0.23059172928333282),
    '''

