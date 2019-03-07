import plotly.offline as py
import plotly.graph_objs as go

from vector2d import Vector2D


class PlotManager:
    colors = {'Red': '#e6194B', 'Green': '#3cb44b', 'Yellow': '#ffe119', 'Blue': '#4363d8', 'Orange': '#f58231',
              'Purple': '#911eb4', 'Cyan': '#42d4f4', 'Magenta': '#f032e6', 'Lime': '#bfef45', 'Pink': '#fabebe',
              'Teal': '#469990', 'Lavender': '#e6beff', 'Brown': '#9A6324', 'Beige': '#fffac8', 'Maroon': '#800000',
              'Mint': '#aaffc3', 'Olive': '#808000', 'Apricot': '#ffd8b1', 'Navy': '#000075', 'Grey': '#a9a9a9'}

    def __init__(self):
        pass


    def get_shapes(self, path, color):
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

    def draw_path_plot(self, circles, path):
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

    def draw_fitness_plot(self, settings, result):
        trace = go.Scatter(
            x=[x for x in range(settings['generations'])],
            y=[x.position.distance(Vector2D(1, 1)) for x in result],
            mode='lines'
        )

        layout = go.Layout(
            xaxis=dict(
                title=f'Population<br>'
                      f'Population: {settings["population_size"]}, Mutate rate: {settings["mutate_rate"]}, Generations: {settings["generations"]}',
            ),
            yaxis=dict(
                title='Distance to (1, 1)',
                range=[0, 1]
            )
        )

        fig = go.Figure(data=[trace], layout=layout)
        py.plot(fig, filename='fitness_plot.html')