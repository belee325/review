#Uses python3

import sys
from numpy import zeros
def lcs2(a, b):
    rows = len(a)
    cols = len(b)
    if rows == 0 or cols == 0:
        return 0
    lcs_grid = zeros((rows+1,cols+1))
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            if a[i-1]==b[j-1]:
                lcs_grid[i,j]= lcs_grid[i-1,j-1]+1
            else:
                #up = lcs_grid[i-1,j]
                #left = lcs_grid[i,j-1]
                lcs_grid[i,j] = max(lcs_grid[i-1,j],lcs_grid[i,j-1])
    #print(lcs_grid)
    return int(lcs_grid[rows,cols])
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))