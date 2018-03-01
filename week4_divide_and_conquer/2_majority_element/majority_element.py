# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    A = get_majority_element(a,left, right//2)
    B = get_majority_element(a,left + right//2,right)
    if a[left:right].count(A)/(right-left) > 0.5 or B<0:
        return A
    elif a[left:right].count(B)/(right-left)>0.5 or A<0:
        return B
    else:
        return -1
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
