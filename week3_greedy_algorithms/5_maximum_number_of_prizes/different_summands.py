# Uses python3
import sys

# problem 5
'''
we want the maximum amount of integers that sum up to n
note that we can decompose as follows:
for a given n, n = 1 + 2 + 3 ... + m + r
thus we want the greatest m such that r > m
suppose n = 8
m    sum    r
0    0      8
1    1      7
2    1+2    5
3    1+2+3  2

Thus the greatest m st r>m is 2 and the summand should be 1 + 2 + 5
We can generalize as follows. An arithmetic series has the formula k(k+1)/2. Thus n = m(m+1)/2 + r, and since r>m we have
m(m+1)/2 + m < n ==> m^2 + 3m -2n <0 ==> m<-3+sqrt(1+8n)/2
''' 
import math

def optimal_summands(n):
    if n<=2:
        return [n]
    summands = []
    #we should floor divide since we know m should be an integer
    m = int((-3 + math.sqrt(1 + 8*n))//2)
    for i in range(1,m+1):
        summands.append(i)
    n = n - (m*(m+1))//2
    summands.append(int(n))
    return summands
	
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
