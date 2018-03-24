# Uses python3

import sys


def reach(adj, x, visited):
    # write your code here
    visited[x] = True
    for nbrs in adj[x]:
        if not visited[nbrs]:
            reach(adj, nbrs, visited)


def number_of_components(adj, visited):
    result = 1
    visited[0] = True
    for i in range(len(adj)):
        if not visited[i]:
            result += 1
        for nbrs in adj[i]:
            reach(adj, nbrs, visited)
            # write your code here
    return result


if __name__ == '__main__':
    input = sys.stdin.readlines()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    visited = [False] * n
    print(number_of_components(adj, visited))
