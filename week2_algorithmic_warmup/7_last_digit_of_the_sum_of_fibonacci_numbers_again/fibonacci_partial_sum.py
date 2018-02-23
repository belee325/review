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
    if n <=1:
        return n
    a=0
    b=1
    c=0
    for i in range(2,n+1):
        c = a+b
        a=b
        b=c
    return c

def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to
    m = get_pisano(10)
    if from_==to:
        return get_fib((to)%m)%10
    else:
        return (get_fib((to+2)%m) - get_fib((from_+1))%m)%10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))