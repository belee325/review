# Uses python3
import sys

def merge(left,right):
    i = 0
    j = 0
    inv = 0
    a_prime=[]
    while(i < len(left) and j < len(right)):
        if left[i] > right[j]:
            a_prime.append(right[j])
            j+=1
            inv+=1
        elif left[i]<= right[j]:
            a_prime.append(left[i])
            i+=1
    #print(i, left[i:], j ,right[j:])
    if i >= j:
        for x in right[j:]:
            a_prime.append(x)
    else:
        for x in left[i:]:
            a_prime.append(x)
    return inv, a_prime

def get_number_of_inversions(a):
    tot_inv = 0
    if len(a) == 1:
        return [a[0]], tot_inv
    m = len(a) // 2
    left, temp = get_number_of_inversions(a[0:m])
    tot_inv += temp
    right, temp = get_number_of_inversions(a[m:])
    tot_inv += temp
    print(left,right, tot_inv)
    inv, a_prime = merge(left,right)
    tot_inv+=inv
    return a_prime, tot_inv

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a))