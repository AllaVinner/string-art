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


# Line image creator 
mean_image_intensity = 10.

x1 = 245
y1 = 23

x2 = 23,
y2 = 23

ribon_radius = 4.
picture_radius = 50
picture_center = (50, 60)

def is_in_picture_circle(x, y, radius, center_x, center_y):
    return (x-center_x)**2+(y-center_y)**2 < radius **2

def is_in_ribon(x, y, radius, pixel_1, pixel_2):
    v = pixel_2-pixel_1
    a = np.array([x,y])
    w = x-(pixel_1+ np.inner(a-pixel_1, v)/np.inner(v,v)*v)
    return np.inner(w,w) < radius **2

def get_neighbours(x,y):
    return [[x+1, y],
            [x, y+1]
            [x-1, y]
            [x, y-1]]

pixels_to_visit = [[x1, y1]]
approved_pixels = set()
while len(pixels_to_visit) > 0:
    x, y = pixels_to_visit.pop()
    approved_pixels.add((x, y))
    for nx, ny in get_neighbours(x, y):  
        if not is_in_picture_circle(nx,ny, picture_radius, picture_center[0], picture_center[1]):
            continue
        if not is_in_ribon(nx,ny, picture_radius, picture_center[0], picture_center[1]):
            continue
        if (nx. ny) in approved_pixels:
            continue
        pixels_to_visit.append((nx. ny))


a = set()
v = np.array([1,2,3])




    












