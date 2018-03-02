# Uses python3
import sys

def merge(left,right):
    inv = left[0] + right[0]
    left_arr = left[1]
    right_arr = right[1]
    a_prime=[]
    
    while(len(left_arr) > 0 and len(right_arr) > 0):
        if left_arr[0] > right_arr[0]:
            a_prime.append(left_arr[0])
            inv += len(right_arr)
            del(left_arr[0])
        else:
            a_prime.append(right_arr[0])
            del(right_arr[0])
    a_prime = a_prime + left_arr
    a_prime = a_prime + right_arr
    return inv, a_prime

def get_number_of_inversions(a):
    if len(a) == 1:
        return 0,[a[0]]
    m = len(a) // 2
    left = get_number_of_inversions(a[0:m])
    right = get_number_of_inversions(a[m:])
    tot_inv, a_prime = merge(left,right)
    return tot_inv,a_prime

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a)[0])