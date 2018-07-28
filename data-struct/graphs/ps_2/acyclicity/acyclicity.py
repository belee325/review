# Uses python3

import sys


def reach(adj, x, visited,stack):
    # write your code here
    if not visited[x]:
        visited[x] = True
        stack[x] = True
        for nbrs in adj[x]:
            if not visited[nbrs] and reach(adj, nbrs, visited, stack):
                return True
            elif stack[nbrs]:
                return True
    stack[x] = False
    return False


def acyclic(adj):
    for x in range(len(adj)):
        visited =[False] * len(adj)
        stack =[False] * len(adj)
        if reach(adj, x, visited, stack):
            return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    visited = [False] * n
    cycle = []
    print(acyclic(adj))
