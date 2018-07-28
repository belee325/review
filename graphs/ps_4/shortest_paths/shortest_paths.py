# Uses python3

import sys
import queue

def bfs(adj, s, visited):
    #write your code here
    queue = []
    queue.append(s)
    ret=[]
    while len(queue)>0:
        curr = queue.pop(0)
        for nbrs in adj[curr]:
            if not visited[nbrs]:
                visited[nbrs]=True
                queue.append(nbrs)
                ret.append(nbrs)
    return ret

def shortest_paths(adj, cost, s, distance, reachable, shortest):
    # write your code here
    distance[s] = 0
    for i in range(len(adj)):
        for j, edges in enumerate(adj):
            for k, nbr in enumerate(edges):
                if distance[nbr] > distance[j] + cost[j][k]:
                    distance[nbr] = distance[j] + cost[j][k]
    curr_distance = distance.copy()
    negative_nodes = []

    for j, edges in enumerate(adj):
        for k, nbr in enumerate(edges):
            if distance[nbr] > distance[j] + cost[j][k] or shortest[j] == 0:
                shortest[nbr] = 0
                negative_nodes.append(nbr)
                for x in adj[nbr]:
                    negative_nodes.append(x)
                distance[nbr] = distance[j] + cost[j][k]
    visited = [False]*len(adj)
    for node in negative_nodes:
        if not visited[node]:
            lst = bfs(adj,node,visited)
            for negative in lst:
                shortest[negative] = 0

    for i in range(len(distance)):
        if distance[i] == float('inf'):
            #no paths to node i
            reachable[i]=0
        elif curr_distance[i] == distance[i]:
            #no neg cycle, reachable
            reachable[i] = 1
        elif curr_distance[i] != distance[i]:
            #negative cycle
            reachable[i]=1
    return

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
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortest_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
