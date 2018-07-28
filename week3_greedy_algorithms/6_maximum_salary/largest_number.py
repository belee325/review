#Uses python3

import sys

def get_max(digit, max_digit):
    if int(digit+max_digit) >= int(max_digit+digit):
        return digit
    else:
        return max_digit


def largest_number(a):
    #write your code here
    res = ""
    while len(a) >0:
        max_digit = '0'
        for x in a:
            max_digit = get_max(x, max_digit)
        res += max_digit
        a.remove(max_digit)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
