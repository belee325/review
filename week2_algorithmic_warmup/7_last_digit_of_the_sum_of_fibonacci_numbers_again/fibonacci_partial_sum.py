# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    fib_list = []
    fib_list.append(0)
    fib_list.append(1)
    for i in range(2, to + 1):
        fib_list.append(fib_list[i-1]+ fib_list[i-2])
    return sum(fib_list[from_:to+1])%10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))