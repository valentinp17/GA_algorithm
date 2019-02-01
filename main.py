import random

import matplotlib.pyplot as plt
from plotly import tools

from genetic_algorithm import GeneticAlgorithm
from vector2d import Vector2D
import time
import plotly.offline as py
import plotly.graph_objs as go
from circle import Circle


def get_shapes(path, color):
    shapes = []
    for i in range(len(path) - 1):
        shapes.append({
            'type': 'line',
            'x0': path[i].x,
            'y0': path[i].y,
            'x1': path[i + 1].x,
            'y1': path[i + 1].y,
            'line': {
                'color': f'rgb({color[0]}, {color[1]}, {color[2]})',
                'width': 4,
                'dash': 'dashdot',
            },
        })
    return shapes

def draw_path_plot(circles, path):
    trace1 = go.Scatter()

    shapes = []
    for circle in circles:
        shapes.append({
            'type': 'circle',
            'xref': 'x',
            'yref': 'y',
            'fillcolor': 'rgba(255, 80, 80, 0.7)',
            'x0': circle.position.x - circle.radius,
            'y0': circle.position.y - circle.radius,
            'x1': circle.position.x + circle.radius,
            'y1': circle.position.y + circle.radius,
            'line': {
                'color': 'rgba(255, 80, 80, 1)',
            },
        },
    )

    for i in range(len(path) - 1):
        shapes.append({
            'type': 'line',
            'x0': path[i].x,
            'y0': path[i].y,
            'x1': path[i + 1].x,
            'y1': path[i + 1].y,
            'line': {
                'color': 'rgb(50, 171, 96)',
                'width': 1,
                'dash': 'dot',
            },
        })



    layout1 = {
        'title': 'Robot Path',
        'xaxis': {
            'range': [0, 1],
            'zeroline': False,
        },
        'yaxis': {
            'range': [0, 1]
        },
        'width': 800,
        'height': 800,
        'shapes': shapes,
    }



    data = [trace1]
    fig = go.Figure(data=data, layout=layout1)
    py.plot(fig, filename='shapes-circle.html')

def draw_fitness_plot(settings, result):
    trace = go.Scatter(
        x=[x for x in range(settings['generations'])],
        y=[x.position.distance(Vector2D(1, 1)) for x in result],
        mode='lines'
    )

    layout = go.Layout(
        xaxis= dict(
            title= f'Population<br>'
                   f'Population: {settings["population_size"]}, Mutate rate: {settings["mutate_rate"]}, Generations: {settings["generations"]}',
        ),
        yaxis= dict(
            title= 'Distance to (1, 1)',
        )
    )

    fig = go.Figure(data=[trace], layout=layout)
    py.plot(fig, filename='fitness_plot.html')


if __name__ == '__main__':

    settings = {
        'population_size': 1000,
        'elite_size': 200,
        'mutate_rate': 0.2,
        'generations': 1000,
        'max_force': 1,
        'circles': [
            Circle(0.5, 0.5, 0.1), Circle(0.7, 0.7, 0.1), Circle(0.3, 0.7, 0.1),
            Circle(0.3, 0.3, 0.1), Circle(0.7, 0.3, 0.1),
        ]
    }


    start_time = time.time()
    genetic_algo = GeneticAlgorithm(settings['population_size'], settings['elite_size'],
                                    settings['mutate_rate'], settings['generations'],
                                    settings['max_force'], settings['circles'])
    result = genetic_algo.start_algorithm()
    end_time = time.time()
    print(f'TIME OF EXECUTION: {(end_time-start_time) / 60}')

    print(result)
    print(result)
    print(result[-1].route)
    print(result[-1].path)



    draw_path_plot(genetic_algo.circles, result[-1].path)
    draw_fitness_plot(settings, result)

    '''
    Circle(0.5, 0.5, 0.1), Circle(0.7, 0.7, 0.1), Circle(0.3, 0.7, 0.1),
            Circle(0.3, 0.3, 0.1), Circle(0.7, 0.3, 0.1),
            
    Circle(0.5, 0.5, 0.2), Circle(0.7, 0.3, 0.2), Circle(0.3, 0.7, 0.2)
    
    Circle(0.5, 0.5, 0.1), Circle(0.7, 0.7, 0.15), Circle(0.3, 0.7, 0.15),
            Circle(0.3, 0.3, 0.15), Circle(0.7, 0.3, 0.15),
    
    '''

