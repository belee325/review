# Uses python3
from numpy import zeros
def edit_distance(s, t):
    rows = len(s)
    cols = len(t)
    edit_grid = zeros((rows+1,cols+1))
    for i in range(1,rows+1):
        edit_grid[i,0]=i
    for i in range(1,cols+1):
        edit_grid[0,i]=i
    #print(edit_grid)
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            ins = edit_grid[i,j-1] + 1
            deletion = edit_grid[i-1,j] + 1
            match = edit_grid[i-1,j-1]
            if s[i-1]!=t[j-1]:
                match+=1
            edit_grid[i,j] += min(ins, deletion, match)
    #print(edit_grid)
    return int(edit_grid[i,j])

if __name__ == "__main__":
    print(edit_distance(input(), input()))