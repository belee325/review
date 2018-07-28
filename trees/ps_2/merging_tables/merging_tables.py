# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(idx):
    # find parent and compress path
    if idx != parent[idx]:
        parent[idx] = getParent(parent[idx])
    return parent[idx]

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)
    curr_max = 0
    if realDestination == realSource:
        return lines[realDestination]
    
    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    #attach lower rank tree to higher rank tree
    if rank[realDestination] >= rank[realSource]:
        lines[realDestination]+=lines[realSource]
        lines[realSource] =0
        parent[realSource] = realDestination
        curr_max= lines[realDestination]
    else:
        lines[realSource]+=lines[realDestination]
        lines[realDestination] =0
        parent[realDestination] = realSource
        curr_max = lines[realSource]
    if rank[realDestination] == rank[realSource]:
        rank[realDestination] +=1

    return curr_max

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    curr_max = merge(destination - 1, source - 1)
    ans = max(curr_max,ans)
    print(ans)