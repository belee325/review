#Uses python3

import sys
import heapq
import math

def distance(adj, cost, s, t):
    #write your code here
    q = [(0,s)]
    dist = [10**10] * len(adj)
    prev = [None] * len(adj)
    dist[s] = 0
    heapq.heapify(q)
    while len(q) > 0:
        _,curr_node = heapq.heappop(q)
        for i,nbrs in enumerate(adj[curr_node]):
            if dist[nbrs] >= dist[curr_node] + cost[curr_node][i]:
                dist[nbrs]=dist[curr_node] + cost[curr_node][i]
                prev[nbrs] = curr_node
                heapq.heappush(q, (dist[nbrs],nbrs))
    if dist[t]==10**10:
        return -1
    else:
        return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
