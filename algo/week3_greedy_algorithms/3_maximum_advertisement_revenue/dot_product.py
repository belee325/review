#Uses python3

import sys

def max_dot_product(a, b):
    #grouping problem
    #safe move would be to always group the max of a with max of b
    #we can just sort a and b 
    a.sort()
    b.sort()
    c = [x*y for x,y in zip(a,b)]
    res=0
    for x in c:
        res = res + x
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
