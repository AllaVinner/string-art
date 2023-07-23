import numpy as np
import plotly.graph_objects as go

def create_circle(num_points: int = 100, radius: float = 1.):
    theta = np.linspace(0, 1, num_points+1)
    x = radius * np.cos(np.pi*2*theta)
    y = radius * np.sin(np.pi*2*theta)
    return x, y

def create_lines(point_order, num_points: int = 100, radius: float = 1.):
    x = radius * np.cos(np.pi*2*point_order/num_points)
    y = radius * np.sin(np.pi*2*point_order/num_points)
    return x, y  


def get_spikes_go(num_points: int = 100, radius: float = 1.) -> go.Scatter:
    x, y = create_circle(num_points, radius)
    return go.Scatter(
        x = x,
        y = y,
        mode='markers'
    )



