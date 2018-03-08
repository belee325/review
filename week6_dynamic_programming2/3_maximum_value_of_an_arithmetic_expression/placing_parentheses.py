# Uses python3
from numpy import zeros

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False
        
def minmax(i,j,min_arr,max_arr,ops):
    min_ret = 10**10
    max_ret = -10**10
    for k in range(i, j):
        if k != '+' and k != '-' and k != '*':
            a = evalt(max_arr[i,k],max_arr[k+1,j],ops[k])
            b = evalt(min_arr[i,k],max_arr[k+1,j],ops[k])
            c = evalt(max_arr[i,k],min_arr[k+1,j],ops[k])
            d = evalt(min_arr[i,k],min_arr[k+1,j],ops[k])
            min_ret = min(min_ret,a,b,c,d)
            max_ret = max(max_ret,a,b,c,d)
        else:
            k+=1
    return min_ret,max_ret

def get_maximum_value(dataset):
    if len(dataset)==1:
        return dataset
    digits =[]
    ops =[]
    j=1
    while(j<len(dataset)-1):
        digits.append(dataset[j-1])
        ops.append(dataset[j])
        if j == len(dataset)-2:
            digits.append(dataset[j+1])
        j+=2
    n = len(digits)
    min_arr = zeros((n,n))
    max_arr = zeros((n,n))
    for i in range(0,n):
        min_arr[i,i] = digits[i]
        max_arr[i,i] = digits[i]
    #print(min_arr)
    #print(max_arr)
    for s in range(1,n+1):
        for i in range(0, n-s):
            j = i+s
            min_arr[i,j],max_arr[i,j] = minmax(i,j,min_arr,max_arr, ops)
            #print(min_arr)
            #print(max_arr)
    #print(min_arr)
    #print(max_arr)
    return int(max_arr[0,n-1])


if __name__ == "__main__":
    print(get_maximum_value(input()))
