import math
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

def neg(a):
    ret = []
    for x in a:
        ret.append(-x)
    return ret


def dot(a, b):
    ret = 0
    for x, y in zip(a, b):
        ret += x * y
    return ret

def norm(a):
    return math.sqrt(dot(a, a))

def norm2(a):
    return dot(a, a)

def mid(a, b):
    x1, y1 = a
    x2, y2 = b
    return (x1+x2)/2, (y1+y2)/2


def angle(a, b):
    ang = math.acos(dot(a, b) / norm(a) / norm(b))
    if ang > math.pi:
        return 2 * math.pi - ang
    return ang

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

def find_area(points):
    """
    Algorithm for calculating the area of a polygon represented as a list of ccw points in Cartesian plane
    """
    points = sort_ccw(points)
    area = 0
    for p1, p2 in zip(points[:-1], points[1:]):
        area += 0.5 * (p1[1] + p2[1]) * (p1[0] - p2[0])
    return area