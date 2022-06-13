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
debug = False

import math
from fractions import Fraction
if debug:
    import matplotlib.pyplot as plt
def add(a, b):
    ret = []
    for x, y in zip(a, b):
        ret.append(x + y)
    return ret

def sub(a, b):
    ret = []
    for x, y in zip(a, b):
        ret.append(x - y)
    return ret

def dot(a, b):
    ret = 0
    for x, y in zip(a, b):
        ret += x * y
    return ret

def norm(a):
    return math.sqrt(dot(a, a))


def mid(a, b):
    x1, y1 = a
    x2, y2 = b
    return (x1+x2)/2, (y1+y2)/2


def angle(a, b):
    angle = math.acos(min(1, max(-1, dot(a, b) / norm(a) / norm(b))))
    if angle > math.pi:
        return 2 * math.pi - angle
    return angle

def slope(a, b):
    x1, y1 = a
    x2, y2 = b
    return (y2 - y1)/(x2 - x1)

def sort_ccw(points):
    p_x = sorted(points, key=lambda p: p[0])
    cw = []
    cw.extend([p for p in p_x if p[1] <= p_x[0][1]])
    cw.extend(reversed([p for p in p_x if p[1] > p_x[0][1]]))
    return cw

def test_sort_clockwise():
    points = [[0, 0], [1, 1], [0, 1]]
    assert sort_ccw(points) == [[0, 0], [0, 1], [1, 1]]


def main():
    points = []
    for _ in range(3):
        points.append([float(s) for s in input().split(" ")])

    center, r = solve_circle(*points)
    if debug:
        visualize(points, center, r)

    angles = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            p1, p2 = points[i], points[j]
            angles.append(angle(sub(p1, center), sub(p2, center)))
    
    angles.sort()
    a_arc_est = computeGCD(angles[0], angles[1])
    n_est = 2*math.pi / a_arc_est
    n = Fraction(n_est).limit_denominator(100).numerator
    a_arc = (n - 2) * math.pi / n # actual possible a_arc
    return 0.5 * n * r * r * math.sin(a_arc)
        


def computeGCD(x, y):
    while(y):
       x, y = y, x % y
       if round(y, 5) == 0:
            y = 0
    return x

def solve_circle(p1, p2, p3):
    """
    Given three points in 2d, finds the center and radius of the corresponding circle
    """
    m1_x, m1_y = mid(p1, p2)
    m2_x, m2_y = mid(p2, p3)
    s1 = slope(p1, p2)
    s2 = slope(p2, p3)

    if s1 != 0:
        s1_p = -1/s1
        a1 = -s1_p
        b1 = 1
        c1 = m1_y - s1_p * m1_x
    else:
        a1 = 1
        b1 = 0
        c1 = m1_x

    if s2 != 0:
        s2_p = -1/s2
        a2 = -s2_p
        b2 = 1
        c2 = m2_y - s2_p * m2_x
    else:
        a2 = 1
        b2 = 0
        c2 = m2_x

    # Equations
    # c_y - m1_y = s1_p * (c_x - m1_x)
    # c_y - m2_y = s2_p * (c_x - m2_x)

    # c_y - s1_p * c_x = m1_y - s1_p * m1_x
    # c_y - s2_p * c_x = m2_y - s2_p * m2_x
    
    center = cramers(a1, b1, a2, b2, c1, c2)
    r = norm(sub(center, p1))
    return center, r

    
def cramers(a1, b1, a2, b2, c1, c2):
    x = (c1 * b2 - b1 * c2) / (a1 * b2 - b1 * a2)
    y = (a1 * c2 - c1 * a2) / (a1 * b2 - b1 * a2)
    return x, y
    

def visualize(points, center=None, r=None):
    x, y = [a for a, _ in points], [b for _, b in points]
    plt.plot(x, y, 'ro')
    plt.axis('equal')

    cw = sort_ccw(points)
    for p1, p2 in zip(cw, cw[1:] + [cw[0]]):
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'ro-')
    plt.axis('equal')

    circle = plt.Circle(center, r, color='r', fill=False)
    plt.gca().add_patch(circle)
    plt.show()



if __name__ == '__main__':
    print(main())