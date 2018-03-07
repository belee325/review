#Uses python3

import sys

from numpy import zeros
def lcs3(a,b,c):
    rows = len(a)
    cols = len(b)
    depth = len(c)
    if rows == 0 or cols == 0 or depth == 0:
        return 0
    lcs_grid = zeros((rows+1,cols+1,depth+1))
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            for k in range(1,depth+1):
                if a[i-1]==b[j-1] and b[j-1]==c[k-1]:
                    lcs_grid[i,j,k] = lcs_grid[i-1,j-1,k-1]+1
                else:
                    lcs_grid[i,j,k]= max(lcs_grid[i-1,j,k],lcs_grid[i,j-1,k],lcs_grid[i,j,k-1])
    #print(lcs_grid)
    return int(lcs_grid[rows,cols,depth])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
