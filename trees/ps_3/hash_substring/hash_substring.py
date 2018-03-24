# python3

def read_input():
    #pattern, text
    return (input().rstrip(), input().rstrip())

def hash_func(s,multiplier, prime):
    ans = 0
    for c in reversed(s):
        ans = (ans * multiplier + ord(c)) % prime
        #print(ans)
    return ans

def precompute_hash(patt, text):
    _multiplier = 263
    _prime = 1000000007
    patt_len = len(patt)
    text_len = len(text)
    H = [0] * (text_len-patt_len + 1)
    last = text[-patt_len:]
    #print(last)
    H[-1] = hash_func(last, _multiplier, _prime)
    #print(H)
    y = 1
    for i in range(0,patt_len):
        y = (y*_multiplier) % _prime
    for i in reversed(range((text_len - patt_len))):
        H[i] = (_multiplier*H[i+1] + ord(text[i]) - (y*ord(text[i + patt_len])))%_prime
    #print(H)
    return H
        
def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    _multiplier = 263
    _prime = 1000000007
    ret=[]
    H = precompute_hash(pattern, text)
    p_hash = hash_func(pattern, _multiplier, _prime)
    for i,h in enumerate(H):
        if h == p_hash:
            if text[i:i+len(pattern)] == pattern:
                ret.append(i)
    return ret

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

