# Uses python3
import sys

def get_change(m):
    # safe move would be to get most change from largest denomination first
    num_10 = m//10
    m = m % 10
    num_5 = m // 5
    m = m % 5
    return num_10 + num_5 + m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
