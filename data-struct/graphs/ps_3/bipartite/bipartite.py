#Uses python3

import sys
import queue

def bipartite(adj):
    #write your code here
    visited = [False] * len(adj)
    color = [-1] * len(adj)
    queue = [0]
    flag = 1
    for i in range(len(adj)):
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            color[i] = flag
            while len(queue) > 0 :
                curr = queue.pop(0)
                flag = (flag + 1) % 2
                for nbr in adj[curr]:
                    if not visited[nbr]:
                        queue.append(nbr)
                        visited[nbr] = True
                        color[nbr] = (color[curr]+1) %2
    for i in range(len(adj)):
        for nbr in adj[i]:
            if color[i] == color[nbr]:
                return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
