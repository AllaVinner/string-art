import numpy as np


def fibonacci_points(num_points: int, num_lines: int):
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



