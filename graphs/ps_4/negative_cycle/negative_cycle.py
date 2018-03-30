# Uses python3

import sys
import math


def negative_cycle(adj, cost):
    # write your code here

    dist = [10**8] * len(adj)
    prev = [None] * len(adj)
    dist[len(adj)-1] = 0
    for i in range(len(adj)):
        for j, edges in enumerate(adj):
            for k, nbr in enumerate(edges):
                if dist[nbr] >= dist[j] + cost[j][k]:
                    dist[nbr] = dist[j] + cost[j][k]
                    prev[nbr] = j
    dist_curr = dist.copy()
    for j, edges in enumerate(adj):
        for k, nbr in enumerate(edges):
            if dist[nbr] >= dist[j] + cost[j][k]:
                dist[nbr] = dist[j] + cost[j][k]
                prev[nbr] = j
    if sorted(dist_curr) != sorted(dist):
        return 1
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    last_adj = [i for i in range(n)]
    last_cost= [0 for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    adj.append(last_adj)
    cost.append(last_cost)
    print(negative_cycle(adj, cost))
