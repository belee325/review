# python3
import sys

# python3
import sys
def sort_characters(text):
    #we want the order of the characters in the sorted string in the original string
    #$AACCGT -> ACATGC$ -> [6, 0, 2, 1, 5, 4, 3]
    order=[0]*len(text)
    count = []
    sort_dict = {'A':0, 'T':0, 'G':0, 'C':0, '$':0}
    for char in text:
        sort_dict[char]+=1
    sort_dict['A'] += sort_dict['$']
    sort_dict['C'] += sort_dict['A']
    sort_dict['G'] += sort_dict['C']
    sort_dict['T'] += sort_dict['G']
    for i in reversed(range(0,len(text))):
        sort_dict[text[i]]-=1
        order[sort_dict[text[i]]]=i
    return order
    
def compute_character_class(text, order):
    char_class = [0]*len(text)
    char_class[order[0]] = 0
    for i in range(1,len(text)):
        if text[order[i]] != text[order[i-1]]:
            char_class[order[i]] = char_class[order[i-1]]+1
        else:
            char_class[order[i]] = char_class[order[i-1]]
    return char_class

def sort_doubled(text, length, order, char_class):
    count = [0]*len(text)
    new_order = [0]*len(text)
    for i in range(0, len(text)):
        count[char_class[i]] +=1
    for i in range(1, len(text)):
        count[i]+=count[i-1]
    #print(count)
    for i in reversed(range(0,len(text))):
        start = (order[i] - length + len(text)) % len(text)
        cl = char_class[start]
        count[cl]-=1
        new_order[count[cl]]=start
    return new_order
def update_classes(new_order, char_class, length):
    new_class = [0]*len(new_order)
    for i in range(1,len(new_order)):
        cur = new_order[i]
        prev = new_order[i-1]
        mid = (cur + length)%len(new_order)
        mid_prev = (prev+length)%len(new_order)
        if char_class[cur]!=char_class[prev] or char_class[mid]!=char_class[mid_prev]:
            new_class[cur] =new_class[prev]+1
        else:
            new_class[cur] = new_class[prev]
    return new_class

def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    result = []
    order= sort_characters(text)
    char_class = compute_character_class(text, order)
    #print(char_class)
    L=1
    while L<len(text):
        order = sort_doubled(text, L, order, char_class)
        char_class = update_classes(order, char_class, L)
        L = 2*L
        #print(order,char_class,L)
    return order

def find_occurrences(text, patterns):
    occs = set()
    suffix_array = build_suffix_array(text)
    #print(suffix_array)
    for pat in patterns:
        min_idx = 0
        max_idx = len(text)
        while min_idx<max_idx:
            mid_idx = (min_idx+max_idx)//2
            #print(mid_idx)
            #print(mid_idx, pat >text[suffix_array[mid_idx]:], text[suffix_array[mid_idx]:])
            if pat > text[suffix_array[mid_idx]:]:
                min_idx = mid_idx +1
            else:
                max_idx = mid_idx
        start = min_idx
        #print(min_idx)
        max_idx = len(text)
        while min_idx<max_idx:
            mid_idx = (min_idx+max_idx)//2
            #print(max_idx, min_idx)
            #print(mid_idx, pat < text[suffix_array[mid_idx]:], text[suffix_array[mid_idx]:])
            if pat < text[suffix_array[mid_idx]:] and pat not in text[suffix_array[mid_idx]:] :
                max_idx = mid_idx
            else:
                min_idx = mid_idx +1
        end = max_idx
        #print(start,end)
        while start < end:
            if pat in text[suffix_array[start]:]:
                occs.add(suffix_array[start])
            start+=1
    return occs


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))