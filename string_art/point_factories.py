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

def pixel_neighbours(p):
    return [
        p + np.array([1,0]),
        p + np.array([-1,0]),
        p + np.array([0,1]),
        p + np.array([0,-1]),
        p + np.array([1,1]),
        p + np.array([-1,1]),
        p + np.array([-1,-1]),
        p + np.array([1,-1])
    ]


def is_in_ribon(p, p1, p2, r):
    v = p2 - p1
    w = p-p1- np.inner(p-p1, v)/np.inner(v,v)*v
    return np.inner(w,w) < r**2

def get_line_pixels(p1, p2, r, height, width):
    center = np.array([height//2, width//2])
    image_radius = min(height//2, width//2)
    pixels_to_visit = [ np.array(((p2+p1)/2).round(), dtype=int)]
    pixels = []
    while len(pixels_to_visit) > 0:
        p = pixels_to_visit.pop()
        print('currently checking out ', p)
        pixels.append(p)
        for pn in pixel_neighbours(p):
            if np.inner(pn-center, pn-center) > image_radius**2:
                continue
            if not is_in_ribon(pn, p1, p2, r=r):
                continue
            if any([(pn == vp).all() for vp in pixels]):
                continue

            if pn[0] < 0 or height <= pn[0] or pn[1] < 0 or width <= pn[1]:
                continue 
            pixels_to_visit.append(pn)
    return pixels



get_line_pixels(p1, p2, 1., 7,5)
