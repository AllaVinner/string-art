import plotly.graph_objects as go
import numpy as np

theta = np.linspace(0, 1, 6)
x = np.cos(np.pi*2*theta)
y = np.sin(np.pi*2*theta)

def create_circle(radius: float = 1., num_points: int = 100):
    theta = np.linspace(0, 1, num_points+1)
    x = radius * np.cos(np.pi*2*theta)
    y = radius * np.sin(np.pi*2*theta)
    return x, y


def create_lines(num_points: int, point_order):
    x = np.cos(np.pi*2*point_order/num_points)
    y = np.sin(np.pi*2*point_order/num_points)
    return x, y  


def fibonacci_points(num_points: int, num_lines):
    fibs = 1
    fibs_passed = 0
    points = [0]
    for i in range(num_lines):
        new_point = (points[-1] + fibs) % num_points
        new_fib = fibs + fibs_passed
        fibs_passed = fibs 
        fibs = new_fib
        points.append(new_point)
    return np.array(points, dtype=float)

def factor_points(num_points: int, factor: int):
    points = []
    for i in range(num_points):
        points.extend([i, (factor*i) % num_points, None])
    return np.array(points, dtype=float)

num_points = 400
x, y = create_circle(1., num_points)
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x = x,
        y = y,
        mode='markers'
    )
)

points = np.array([0, num_points/2, 3*num_points/4, num_points/4], dtype=float)
points = fibonacci_points(num_points, 500)
points = factor_points(num_points, 5)
px, py = create_lines(num_points, points)
fig.add_trace(
    go.Scatter(
        x = px,
        y = py,
        mode='lines'
    )
)
fig.update_layout(
    width = 1500,
    height = 1500
)

fig.show()



