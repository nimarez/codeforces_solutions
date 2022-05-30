"""
Nowadays all circuses in Berland have a round arena with diameter 13 meters, but in the past things were different.

In Ancient Berland arenas in circuses were shaped as a regular (equiangular) polygon, the size and the number of angles could vary from one circus to another. In each corner of the arena there was a special pillar, and the rope strung between the pillars marked the arena edges.

Recently the scientists from Berland have discovered the remains of the ancient circus arena. They found only three pillars, the others were destroyed by the time.

You are given the coordinates of these three pillars. Find out what is the smallest area that the arena could have.

Input
The input file consists of three lines, each of them contains a pair of numbers –– coordinates of the pillar. Any coordinate doesn't exceed 1000 by absolute value, and is given with at most six digits after decimal point.

Output
Output the smallest possible area of the ancient arena. This number should be accurate to at least 6 digits after the decimal point. It's guaranteed that the number of angles in the optimal polygon is not larger than 100.
"""

import math

from utils import sub, angle, dot, norm, find_area, sort_ccw
import matplotlib.pyplot as plt

def main():
    points = []
    while True:
        try:
            points.append([float(s) for s in input().split(" ")])
        except EOFError:
            break

    ccw = sort_ccw(points)
    visualize_polygon(ccw)
    max_angle = 0
    triple = None
    length = None
    for p, pp, ppp in zip(ccw[:-2], ccw[1:], ccw[2:]):
        vec1 = sub(pp, p)
        vec2 = sub(ppp, pp)
        line_angle = angle(vec1, vec2)
        if line_angle > max_angle:
            max_angle = line_angle
            triple = [p, p, ppp]
            length = min(norm(vec1), norm(vec2))
    num_sides = int(2 / (1 - max_angle / math.pi))

    recovered_polygon = triple
    for i in range(num_sides - 2):
        vec = sub(recovered_polygon[-1], recovered_polygon[-2])
        ang = math.atan(vec[1] / vec[0]) 
        x, y = length * math.cos(ang + max_angle), length * math.sin(ang + max_angle)
        recovered_polygon
        


    return num_sides

def make_equiangle_polygon(n):
    theta = 2 * math.pi / n
    points = []
    for i in range(n):
        points.append([math.cos(i * theta), math.sin(i * theta)])
    return points


def visualize_polygon(points):
    x, y = [a for a, _ in points], [b for _, b in points]
    plt.plot(x, y, 'ro')
    plt.axis('equal')

    cw = sort_ccw(points)
    for p1, p2 in zip(cw, cw[1:] + [cw[0]]):
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'ro-')
    plt.axis('equal')
    plt.show()
    
def test_visualization():
    shape = make_equiangle_polygon(3)
    visualize_polygon(shape)


if __name__ == '__main__':
    test_visualization()
    # print(main())