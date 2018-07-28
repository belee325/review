# Uses python3

import sys

sys.setrecursionlimit(200000)
time = 1


def dfs(x, rev_adj, pre, post):
    global time
    pre[x] = time
    time += 1
    for nbrs in rev_adj[x]:
        if len(rev_adj[x]) > 0 and pre[nbrs] == 0:
            dfs(nbrs, rev_adj, pre, post)
    time += 1
    post.append((x, time))


def number_of_strongly_connected_components(adj, rev_adj):
    pre = [0] * len(adj)
    post = []
    result = 0
    for i in range(len(adj)):
        if pre[i] == 0:
            dfs(i, rev_adj, pre, post)
    post = sorted(post, key=lambda tup: tup[1], reverse=True)
    pre_scc = [0] * len(adj)
    post_scc = []
    for sink, _ in post:
        if pre_scc[sink] == 0:
            result += 1
            dfs(sink, adj, pre_scc, post_scc)
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # rev_edge= list(zip(data[1:(2 * m):2], data[0:(2 * m):2]))
    adj = [[] for _ in range(n)]
    rev_adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        rev_adj[b - 1].append(a - 1)

    print(number_of_strongly_connected_components(adj, rev_adj))
