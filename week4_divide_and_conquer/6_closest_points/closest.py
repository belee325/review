#Uses python3
import sys
import math

def minimum_distance(points):
    #write your code here
    return 10 ** 18

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    points = [(x,y) for x,y in zip(data[1::2],data[2::2])] 
    points.sort(key = lambda tup: tup[0])
    print("{0:.9f}".format(minimum_distance(points)))
