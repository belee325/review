# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    fib_list = []
    fib_list.append(0)
    fib_list.append(1)
    for i in range(2,n+1):
        fib_list.append(fib_list[i-1]+ fib_list[i-2])
    return sum(fib_list) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
