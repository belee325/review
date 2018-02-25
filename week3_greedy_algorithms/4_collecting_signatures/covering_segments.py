# Uses python3
import sys
import operator
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments.sort(key = operator.itemgetter(1))
    points = []
    points.append(segments[0].end)
    i = 1
    while(i < len(segments)):
        if segments[i].start > points[-1]:
            points.append(segments[i].end)
        i = i + 1
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
