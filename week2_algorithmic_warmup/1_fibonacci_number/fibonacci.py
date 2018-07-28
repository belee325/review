# Uses python3
def calc_fib(n):
    if n <=1:
        return n
    ret = []
    ret.append(0)
    ret.append(1)
    for i in range(2,n+1):
        ret.append(ret[i-1]+ret[i-2])
    return ret[-1]
n = int(input())
print(calc_fib(n))
