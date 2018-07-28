# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    ret = []
    ret.append(0)
    ret.append(1)
    for i in range(2,n+1):
        ret.append((ret[i-1]+ret[i-2])%10)
    return ret[-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
