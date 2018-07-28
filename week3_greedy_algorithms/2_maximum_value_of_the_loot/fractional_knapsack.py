# Uses python3
import sys

import operator
def get_optimal_value(capacity, weights, values):
    #standard knapsack prob
    #safe move would be to choose the most we can of the item that has max val/weight ratio
    ratio = [x/y for x,y in zip(values,weights)]
    ratio = [(x,y,z) for x,y,z in zip(ratio, weights, values)]
    ratio.sort(key = operator.itemgetter(0), reverse=True)
    value = 0.
    i=0
    while(capacity > 0 and i < len(ratio)):
        amt = min(capacity, ratio[i][1])
        value = value + amt*ratio[i][0]
        capacity = capacity - amt
        i = i + 1
    
    # write your code here

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
