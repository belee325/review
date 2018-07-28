# Uses python3
import sys

def get_majority_element(a):
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        if a[0] == a[1]:
            return a[0]
        else:
            return -1
    #write your code here
    A = get_majority_element(a[0:len(a)//2])
    B = get_majority_element(a[len(a)//2:])
    #print(A, B)
    #print(a.count(A)/len(a), a.count(B)/len(a))
    if a.count(B)/len(a)>0.5:
        return B
    elif a.count(A)/len(a)>0.5:
        return A
    elif A == B:
        return A
    else:
        return -1
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
