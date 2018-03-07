# Uses python3
import sys

def optimal_sequence(n):
    mins = [0]
    ret = [n]
    #prev_nums =[1]
    for i in range(2,n+1):
        #prev_nums.append(i)
        #for subtraction
        min_idx = i - 2
        min_ops=mins[min_idx]+1
        if i % 2 == 0:
            min_idx = i//2 - 1
        if i % 3 == 0:
            min_idx = i//3 - 1
        if mins[min_idx] + 1 <= min_ops:
            min_ops = mins[min_idx] + 1
        #print(min_ops)
        mins.append(min_ops)
        #print(mins)
    num_seq = mins[n-1]
    while(n > 1):
        curr_n = n-1
        curr_ops = mins[curr_n-1]
        #print(curr_n, curr_ops)
        if n%2==0:
            if mins[int(n//2)-1]<= curr_ops:
                curr_n = n//2
                curr_ops = mins[int(n//2)]
        if n%3==0:
            if mins[int(n//3)-1] <= curr_ops:
                curr_n = n//3
                curr_ops = mins[int(n//3)]
        #print(curr_n,min_ops)
        ret.append(curr_n)
        n = curr_n
    return reversed(ret)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
