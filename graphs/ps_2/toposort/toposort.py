#Uses python3

import sys
time = 0

def dfs(adj, pre, post, x):
    #write your code here
    global time
    time += 1
    pre[x] = time
    for nodes in adj[x]:
        if pre[nodes]==0:
            dfs(adj,pre, post,nodes)
    time +=1
    post.append((x,time))




def toposort(adj):
    used = [False] * len(adj)
    pre = [0] * len(adj)
    post = []
    for i in range(len(adj)):
        if pre[i] == 0:
            dfs(adj,pre, post,i)
    #write your code here
    return sorted(post, key = lambda tup : tup[1], reverse =True)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x, _ in order:
        print(x+1, end=' ')

