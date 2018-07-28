# Uses python3
import sys

def get_pisano(m):
    a=0
    b=1
    c= (a + b)
    for i in range(0, m**2):
        c = (a+b)%m
        a=b
        b=c
        if a == 0 and b == 1:
            return i+1
        
def get_fib(n):
    ret = []
    ret.append(0)
    if n <=1:
        return n
    ret = []
    ret.append(0)
    ret.append(1)
    for i in range(2,n+1):
        ret.append(ret[i-1]+ret[i-2])
    return ret[-1]

def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    else:    
        return (get_fib((n+2)%get_pisano(10))-1)%10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
